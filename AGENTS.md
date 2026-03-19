# AGENTS.md

## Mission

This repo powers docs.feralfile.com, the canonical technical home for Feral File.

Help three lanes succeed fast:

1. Developers integrating DP-1 or FF1 CLI
2. Agent / Claw builders using OpenAPI, schemas, and deterministic tool flows
3. Partners / institutions evaluating or integrating the open protocol

## Product map

- feralfile.com = story, exhibitions, product framing
- docs.feralfile.com = canonical technical docs
- GitHub repos = source of truth for code, specs, schemas, and contributor workflows

## IA rules

- Keep Exhibitions and The Digital Art System distinct
- Bridge them only where it reduces confusion
- Mini-sites live inside docs.feralfile.com, not on separate doc domains unless explicitly requested
- Prefer curated entry routes over sprawling reference trees

## Canonical terminology

- Feral File = cultural institution and technology company
- The Digital Art System = the hardware family
- FF1 = art computer
- FFP = panel / art panel, never "canvas"
- DP-1 = protocol only, never a device
- Public-facing surfaces: prefer "play"
- Developer-facing surfaces: "run" is acceptable
- Hardware is an instrument, not a gadget

## Documentation principles

- First success in under 5 minutes for the primary flow
- One obvious next step per page
- Link to canonical schemas / OpenAPI / reference files; do not duplicate truth
- Rewrite or recompose existing content before adding new sprawl
- Deletion-first: remove friction before adding explanation
- Reliability before novelty
- No invented claims, roadmap, integrations, benchmarks, or support promises
- State what was tested and what was not

## Audience lanes

### FF1 CLI

Audience:

- Developers
- Creative technologists
- Ambitious terminal users who may not identify as developers

Goal:

- install
- build
- validate / sign
- send / play

### DP-1

Audience:

- Developers
- Partners
- Institutions
- Technical collaborators

Goal:

- understand the protocol quickly
- validate a sample
- run or connect to a feed
- play on FF1 or another compatible player

### Agents

Audience:

- Agent / Claw builders

Goal:

- discover OpenAPI and tool-compatible docs without duplicating FF1 CLI or DP-1 onboarding

## Writing style

- Plain language
- Short paragraphs
- Verb-first headings
- Calm, credible, human
- No hype
- Start with why it matters, then show the next concrete step
- End pages with one obvious next action

## Build and validation

- Respect the existing MkDocs / Material setup
- Prefer editing existing sections for DP-1, FF1 CLI, and LLM / Agents
- Run the docs build in strict mode
- Ensure commands are copy-pastable
- Prefer smaller coherent changes over sprawling rewrites
