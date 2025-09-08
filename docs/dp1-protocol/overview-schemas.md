# DP-1 Protocol Overview

## Introduction

The DP-1 is a standardized protocol designed to facilitate reliable and interoperable data exchange between digital display systems, particularly in the context of digital art, exhibitions, and blockchain-based content distribution. The protocol addresses key challenges in the digital display ecosystem, including data consistency, validation, and seamless integration across diverse platforms.

### Why DP-1 Was Introduced

The digital display landscape faces several critical challenges:

- **Fragmented Standards**: Different display systems use incompatible data formats, making content distribution complex and error-prone
- **Data Integrity Issues**: Without standardized validation, corrupted or malformed data can break display systems
- **Interoperability Gaps**: Content creators struggle to distribute their work across multiple platforms due to format inconsistencies
- **Trust and Verification**: In blockchain-based digital art, there's a need for verifiable content authenticity and metadata

DP-1 solves these problems by providing a unified framework for data exchange, validation, and content distribution.

## Key Terminologies

Understanding these core concepts will help you navigate the DP-1 ecosystem:

- **Feed Server**: A core entity of DP-1 that serves as a registry for playlists. It stores, validates, and distributes playlists. It's the central authority for playlist management in the DP-1 ecosystem.

- **Validator**: A component that validates playlists against the DP-1 schema specifications. It ensures data integrity and compliance before playlists are stored or distributed.

- **Schema**: A structured definition that specifies the format, data types, and constraints for content metadata and display instructions.

- **Display Client**: Any device or application that renders content according to DP-1 specifications.

## Feed Server and Validator

The Feed Server and Validator are the backbone components of the DP-1 protocol:

### Feed Server
The Feed Server is a core entity of DP-1 that serves as a registry for playlists. It:

- Stores validated playlists in a centralized registry
- Validates playlists against DP-1 schema specifications
- Distributes playlists to display clients and other consumers
- Maintains playlist metadata and versioning information
- Acts as the authoritative source for playlist data

### Validator
The Validator ensures playlist compliance with DP-1 standards by:

- Validating playlist structure against the DP-1 schema
- Checking required fields and data types
- Verifying playlist metadata completeness
- Rejecting non-compliant playlists with detailed error messages
- Ensuring data integrity before playlist storage and distribution

For detailed information about Feed Server implementation and configuration, see the dedicated [Feed Server section](feed-server.md).

## Playlist Schema

The Playlist Schema is the core entity of the DP-1 protocol, defining the standardized structure for organizing and distributing digital content. It ensures consistency and interoperability across different display systems and platforms.

### Schema Structure

The DP-1 Playlist Schema defines the following key components:

- **Playlist Metadata**: Unique identifier, title, description, and creation information
- **Content Items**: Array of media items with their respective metadata
- **Display Instructions**: Rendering parameters, timing, and presentation settings
- **Validation Rules**: Required fields, data types, and format constraints

### Schema Components

A typical DP-1 playlist schema includes:

* **Playlist ID**: Unique identifier for the playlist
* **Title**: Display name of the playlist
* **Items**: Array of content items, each containing:
    - Media URL or reference
    - Duration and timing information
    - Metadata (title, artist, description)
    - Display parameters
* **Metadata**: Creation timestamp, DP-1 version, and administrative information

## DP-1 Schema Specification

The DP-1 playlist schema is formally defined in the [DP-1 specification document](https://github.com/display-protocol/dp1/blob/main/docs/spec.md), with detailed field requirements and API specifications available in the [Feed Server OpenAPI specification](https://github.com/display-protocol/dp1/blob/main/docs/feed-api.yaml).

### Playlist Structure

Based on the official DP-1 specification, a Playlist consists of the following components:

**Note**: For the most accurate and up-to-date field definitions, data types, and requirements (required vs optional), please refer directly to the [Feed Server OpenAPI specification](https://github.com/display-protocol/dp1/blob/main/docs/feed-api.yaml) which contains the authoritative schema definitions.

Key playlist fields include:

- Unique playlist identifier
- Protocol version information  
- Creation timestamp
- Optional display title
- Default display settings
- Array of playlist items
- Cryptographic signature for authenticity

### Playlist Item Structure

Each item within a playlist contains:

- Unique item identifier
- Creation timestamp
- Display duration
- Optional licensing information
- Optional metadata reference.
- Optional override block.
- Optional blockchain provenance data
- Optional display references.
- Optional reproduction block.

### Detailed Schema Fields

Based on the DP-1 specification and API documentation, here are the detailed field specifications:

#### Playlist Fields

* **`dpVersion`** (string, required): The DP-1 protocol version identifier (e.g., "1.0.0")
* **`id`** (string, required): Unique identifier for the playlist
* **`created`** (string, required): RFC3339 timestamp of playlist creation
* **`title`** (string, optional): Human-readable name for the playlist
* **`defaults`** (object, optional): Default display settings applied to all items
    - **`display`** (object): Display configuration
        - **`scaling`** (string): How content should be scaled (e.g., "fit")
        - **`background`** (string): Background color (e.g., "#111")
        - **`margin`** (string): Margin settings (e.g., "5%")
* **`items`** (array, required): Array of playlist item objects
* **`signature`** (string, required): Ed25519 cryptographic signature for authenticity verification

#### Playlist Item Fields

Each item in the `items` array contains:

* **`id`** (string, required): Unique identifier for the content item
* **`slug`** (string, required): URL-friendly identifier for the content item
* **`title`** (string, optional): Human-readable title for the content item
* **`source`** (string, optional): URL to the content source (e.g., HTML, video, image)
* **`duration`** (integer, required): Display duration in seconds
* **`license`** (string, required): Licensing information for the content (e.g., "open", "token", "subscription")
* **`ref`** (string, optional): Reference to external metadata (e.g., IPFS URI to manifest)
* **`override`** (object, optional): Override settings for this specific item
* **`display`** (object, optional): Display settings specific to this item
    - **`scaling`** (string): How content should be scaled (e.g., "fit")
    - **`background`** (string): Background color (e.g., "#000000")
    - **`margin`** (string): Margin settings (e.g., "5%", "5px")
* **`repro`** (object, optional): Reproduction-specific settings (implementation-defined)
* **`provenance`** (object, optional): Blockchain provenance information
    - **`type`** (string): Type of provenance (e.g., "onChain", "seriesRegistry", "offChainURI")
    - **`contract`** (object): Smart contract details
        - **`chain`** (string): Blockchain network identifier (e.g., "evm", "tezos")
        - **`standard`** (string): Token standard (e.g., "erc721", "erc1155", "fa2")
        - **`address`** (string): Smart contract address
        - **`tokenId`** (string): Token identifier on the blockchain

### Schema Example

Here's a complete example from the DP-1 specification:

```json
{
  "dpVersion": "1.0.0",
  "id": "385f79b6-a45f-4c1c-8080-e93a192adccc",
  "title": "Sunset Collector Loop",
  "slug": "summer‑mix‑01",
  "created": "2025-06-03T17:01:00Z",
  "defaults": {
    "display": {
      "scaling": "fit",
      "background": "#000000",
      "margin": "5%"
    },
    "license": "open",
    "duration": 300
  },
  "items": [
    {
      "id": "385f79b6-a45f-4c1c-8080-e93a192adccc",
      "slug": "payphone‑v2",
      "title": "Payphone",
      "source": "https://cdn.feralfile.com/payphone/index.html",
      "duration": 300,
      "license": "open",
      "ref": "ipfs://bafybeigd…/manifest.json",
      "override": {
        "duration": 180
      },
      "display": {
        "scaling": "fit",
        "background": "#000000",
        "margin": "5%"
      },
      "repro": {},
      "provenance": {
        "type": "onChain",
        "contract": {
          "chain": "evm",
          "standard": "erc721",
          "address": "0x1234567890123456789012345678901234567890",
          "tokenId": "1234567890"
        }
      }
    }
  ],
  "signature": "ed25519:<hex>"
}
```

This example demonstrates both the playlist structure and a minimal playlist item with only required fields.

### Schema Validation

The DP-1 Validator is a standalone component that validates playlists against the DP-1 specification. For detailed implementation information and usage instructions, refer to the [DP-1 Validator documentation](https://github.com/display-protocol/dp1-validator/blob/main/README.md).

The validator performs comprehensive validation including:

- **Schema Compliance**: Ensures playlists conform to the DP-1 JSON schema
- **Field Validation**: Verifies required fields are present and optional fields are properly formatted
- **Data Type Checking**: Confirms all fields match their expected data types
- **Signature Verification**: Validates Ed25519 cryptographic signatures for authenticity
- **Reference Validation**: Checks external references and URIs are properly formatted

The validation process helps maintain data integrity and ensures interoperability across different DP-1 implementations and display systems.

## Benefits of DP-1

- **Interoperability**: Content works across different display systems and platforms
- **Data Integrity**: Validation ensures only properly formatted content is displayed
- **Scalability**: Standardized schemas make it easy to add new content sources and display clients
- **Trust**: Blockchain integration provides verifiable content authenticity
- **Flexibility**: Extensible schemas support various content types and display requirements

## Next Steps

Now that you understand the basics of DP-1, you can explore:

- [Feed Server Implementation](#feed-server.md) - Detailed guide to setting up and configuring Feed Servers
- [Player Behavior](player-behavior.md) - How display clients interpret and render content
