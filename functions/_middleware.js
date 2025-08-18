export const onRequest = async ({ request, env, next }) => {
  const url = new URL(request.url);
  const cookies = request.headers.get("Cookie") || "";
  
  // Check if request comes from app or has app cookie
  const fromApp = url.searchParams.get("from") === "app";
  const hasAppCookie = cookies.includes("app_access=true");
  
  // If coming from app or has valid app cookie, bypass authentication
  if (fromApp || hasAppCookie) {
    const response = await next();
    
    // Set app cookie if coming from app (lasts 30 days)
    if (fromApp) {
      const cookieValue = "app_access=true; Max-Age=2592000; Path=/; HttpOnly; Secure; SameSite=Strict";
      response.headers.set("Set-Cookie", cookieValue);
    }
    
    return response;
  }
  
  // Original basic auth logic for non-app users
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