# DP-1 with FF1 Integration

## Quickstart
1. Generate playlist via [AI Commands](../llm-agents/quickstart.md).
2. POST to [Feral Feed Server](feed-server.md).
3. Assign to FF1 via [Command API](../api-reference/command-api.md).

## Best Practices
- Use `provenance` for NFT-gated exhibitions.
- Set `duration` ≤ 600s for smooth looping.
- Test with [Validator](https://github.com/display-protocol/dp1-validator).

## Troubleshooting
- Signature errors: Re-validate against public schemas.
- Render issues: Check [Player Behavior](player-behavior.md) for FF1 quirks.