# LLM & Agents – Quickstart

## Introduction

This guide explains how to set up a Large Language Model (LLM) that can call APIs to fetch real-time data from **Feralfile**. The goal is to enable your AI agent to answer questions based on live data from exhibitions, series, and artworks.

### Quick Demo

Try our preconfigured GPT right away: **[Feralfile Data GPT](https://chatgpt.com/g/g-6894c9f2dfec8191a94e3ae0a7fe82dc-feralfile-data)**

---

## Setup Guide

### Step 1: Create Custom GPT

Start by creating your own GPT instance in ChatGPT.

### Step 2: Configure API Action

Add an action to enable your GPT to call Feralfile APIs directly (no authentication required).

### Step 3: Import OpenAPI Schema

Use our predefined schema:

```
https://feralfile.com/.well-known/openapi.json
```

> **Note:** This schema follows the OpenAPI standard, making it directly compatible with GPT custom actions and describes all available Feralfile API endpoints.

### Step 4: System Instructions

Configure your GPT with these system instructions:

```markdown
This LLM can fetch Feralfile data to answer user requests about exhibitions, series, and artworks.

Data Structure:

- An exhibition contains multiple series
- A series contains multiple artworks

Special Rules:

- Keep API limits small to avoid oversized responses
- Follow artwork naming conventions based on settings.maxArtwork
```

---

## API Endpoints

### Search Exhibitions

Find exhibitions by keyword:

**Endpoint:**

```http
GET /api/llm/exhibitions?keyword=<name>&sortBy=relevance&limit=2
```

**Parameters:**

- `keyword`: Search term
- `sortBy`: `relevance` (recommended)
- `limit`: **Maximum 2**

> **⚠️ Important:** Keep limit ≤ 2 to prevent context window overflow and parsing errors.

### Get Series in Exhibition

Retrieve series within an exhibition:

**Endpoint:**

```http
GET /api/llm/series?exhibitionID=<id>&sortBy=displayIndex&sortOrder=ASC&limit=5&offset=0
```

**Parameters:**

- `exhibitionID`: Exhibition UUID
- `sortBy`: `displayIndex`
- `sortOrder`: `ASC`
- `limit`: **Maximum 5**
- `offset`: Pagination offset

### Get Artworks in Series

Retrieve artworks within a series:

**Endpoint:**

```http
GET /api/artworks?seriesID=<id>&limit=20&offset=0&sortBy=index&sortOrder=ASC
```

**Parameters:**

- `seriesID`: Series UUID
- `limit`: **Maximum 20**
- `offset`: Pagination offset
- `sortBy`: `index`
- `sortOrder`: `ASC`

---

## Special Rules

### Artwork Naming Convention

The artwork naming follows specific logic based on `settings.maxArtwork`:

- **If `settings.maxArtwork = 1`:**
  Artwork name = `series.title`

- **Otherwise:**
  Artwork name = `series.title + " " + artwork.name`

### Data Limits (Mandatory)

Always respect these limits to ensure smooth operation:

| Endpoint    | Maximum Limit | Reason                                                    |
| ----------- | ------------- | --------------------------------------------------------- |
| Exhibitions | 2             | Prevents context overflow                                 |
| Series      | 5             | Prevents context overflow                                 |
| Artworks    | 20            | Prevents context overflow and optimal parsing performance |

---

## Example Usage

### Prompt

```
Show me the name of the newest exhibition on Feralfile
```

### GPT Function Call

```json
{
  "domain": "feralfile.com",
  "method": "get",
  "path": "/api/llm/exhibitions",
  "operation": "getExhibitionList",
  "operation_hash": "a387f38a2b8a40df3263c75d3e1d22e697233c6c",
  "is_consequential": false,
  "params": {
    "limit": 1,
    "offset": 0,
    "sortBy": "openAt",
    "sortOrder": "DESC"
  }
}
```

### API Response (truncated)

```json
{
  "response_data": {
    "result": [
      {
        "id": "96a205cc-3e5c-46a7-9662-478dbec8209d",
        "title": "Net Evil",
        "slug": "net-evil-das",
        "exhibitionStartAt": "2025-08-26T16:00:00Z",
        "previewDuration": 0,
        "curatorAlumniAccountID": "d900e15b-2510-42f5-b832-18f9ffe46471",
        "setReservation": 0,
        "noteTitle": "Dark Patterns",
        "noteBrief": "<p>In Net Evil, seven artists use the seven deadly sins to explore how evil inhabits the internet. By reflecting how the web enables misdeeds, each work reveals how the occurrence of nefarious behavior on the internet is not a new phenomenon, but part of a long history of human indecency.</p>",
        "note": "",
        "coverURI": "exhibition-thumbnails/96a205cc-3e5c-46a7-9662-478dbec8209d/1755593015",
        "highlightOrder": 10000,
        (etc),
      }
    ]
  }
}
```

### GPT Response

```
The newest exhibition on Feralfile is "Net Evil", curated by Mackenzie Davenport.
```
