# ff-cli

ff-cli is a command-line tool that builds DP-1 playlists from a URL, a wallet, a set of tokens, or a feed, and displays them on an Art Computer. It needs no LLM API key.

```bash
# 1) Install (needs Node.js 22 or newer)
npm i -g @feralfile/cli

# 2) Register your Art Computer. The device ID (FF1-XXXXXXXX) is in the
#    Feral File app's device info.
ff-cli setup --non-interactive --device-host http://<device-id>.local:1111 --device-name "Living Room"

# 3) Build a playlist from an artwork or collection URL and display it
ff-cli find https://www.artblocks.io/collection/ringers-by-dmitri-cherniak --display -y
```

You are successful when the works are on display on your Art Computer.

With a coding agent, the [home page](../index.md) has the prompt to paste and the full setup the agent runs.

## Commands by job

| Job | Command |
| :-- | :-- |
| Build a playlist from an artwork or collection URL, or `ethereum:` / `tezos:` coordinates | `ff-cli find <input>` |
| Build a playlist from parameters, including what a wallet owns | `ff-cli build [params.json]` |
| Display a playlist file, a playlist URL, a media file, or a web page | `ff-cli display <source>` |
| Validate or sign a playlist | `ff-cli validate <file-or-url>`, `ff-cli sign <file>` |
| Publish to a feed, replace, save, or delete what you published | `ff-cli publish <file>`, `publish --replace`, `fetch`, `unpublish` |
| Add, list, or remove Art Computers | `ff-cli device <add\|list\|remove>` |
| Open SSH on your Art Computer | `ff-cli ssh <enable\|disable>` |
| Tell Feral File support what broke | `ff-cli report --file <report.txt>` |

`ff-cli <command> --help` has every flag. In scripts and agents, pass `-y` to `find`: without a terminal, a question fails with exit 1 and names the flag that answers it.

A web page can declare its DP-1 playlist, and `ff-cli display` then displays the playlist instead of the page. Feral File exhibition pages do. To add it to your own pages, see [Declare your page's playlist](../art-computer/display.md#declare-your-pages-playlist).

On a managed network (a museum or an office), see [Network Requirements](../art-computer/network-requirements.md).

## Reference

The ff-cli repository has the rest:

- [Usage and workflows](https://github.com/feral-file/ff-cli/blob/main/docs/README.md), including remote maintenance for owners
- [Configuration](https://github.com/feral-file/ff-cli/blob/main/docs/CONFIGURATION.md)
- [Examples](https://github.com/feral-file/ff-cli/blob/main/docs/EXAMPLES.md)
- [The `ff-control` agent skill](https://github.com/feral-file/ff-cli/blob/main/skills/ff-control/SKILL.md)
