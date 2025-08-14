export const onRequest = async ({ request, env, next }) => {
  const h = request.headers.get("Authorization") || "";
  if (!h.startsWith("Basic ")) {
    return new Response("Auth required", {
      status: 401,
      headers: { "WWW-Authenticate": 'Basic realm="Restricted"', "Cache-Control": "no-store" },
    });
  }

  // decode "Basic base64(user:pass)"
  const creds = atob(h.slice(6));
  const [user, ...rest] = creds.split(":");
  const pass = rest.join(":");

  // constant-time compare
  const equal = (a, b) => {
    if (a.length !== b.length) return false;
    let r = 0;
    for (let i = 0; i < a.length; i++) r |= a.charCodeAt(i) ^ b.charCodeAt(i);
    return r === 0;
  };

  if (!equal(user, env.BASIC_USER || "") || !equal(pass, env.BASIC_PASS || "")) {
    return new Response("Unauthorized", { status: 401, headers: { "Cache-Control": "no-store" } });
  }

  return next();
};