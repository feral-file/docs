# Artwork JS Library
-----------------------------------
## What is the Feral File Artwork JS Library?

The Feral File Artwork JS Library is a lightweight, dependency-free JavaScript library for software artworks on Feral File, enabling software artwork developers to create variants by integrating this library.

### Key Features
- **Deterministic randomness** seeded by token ID
- **Provenance data** from blockchain transactions - essential building blocks for creating dynamic artworks that respond to their on-chain history
- **Blockchain data** access block height

### Installation

#### Self-hosted (recommended for production)

**For maximum stability and reliability, artists should download and host the library themselves.** This approach ensures:

- **Version stability**: Your artwork won't break if external URLs change
- **Performance**: Faster loading from your own domain
- **Reliability**: No dependency on external CDN availability
- **Control**: You decide when to update library versions

Download the latest release from [GitHub](https://github.com/feral-file/ffa-js/releases) and host it on your server:

```html
<script src="./path/to/feralfile-artwork.js"></script>
```

#### GitHub Releases (for testing only)

⚠️ **Not recommended for production artworks.** Use this method only during development and testing.

```html
<script src="https://github.com/feral-file/ffa-js/releases/latest/download/artwork_lib.min.js" type="text/javascript"></script>
```

The script attaches a global:
```js
window.FeralFile // { loadProvenance, loadBlockchainInfo, random, getVariables }
```

#### Browser Support
- Modern browsers (Chrome 60+, Firefox 55+, Safari 12+)
- ES6 support required
- No Internet Explorer support

### Quickstart

This example assumes you've downloaded and self-hosted the library (recommended approach):

  ```html
  <head>
    <!-- Self-hosted library - replace with your actual path -->
    <script src="./feralfile-artwork.js" type="text/javascript"></script>
  </head>
  <body>
    <!-- Always attach listeners before calling loaders (see Event Listeners guide) -->
    <script>
      window.addEventListener('feralfile:provenance-ready', onProv);
      window.addEventListener('feralfile:provenance-request-error', onProvErr);
      window.addEventListener('feralfile:blockchain-info-ready', onHeight);
      window.addEventListener('feralfile:blockchain-info-request-error', onHeightErr);
    </script>

    <script>
      // Load onchain data
      FeralFile.loadProvenance();
      FeralFile.loadBlockchainInfo();

      // Get variables and deterministic random number
      console.log(FeralFile.getVariables());
      console.log(FeralFile.random());
    </script>
  </body>
  ```

  > **Note**: This example uses the self-hosted approach. If you're still in development/testing phase, you can temporarily use the GitHub releases URL, but remember to switch to self-hosting before deploying your artwork.

  > See the [Event Listeners](event-listeners.md) documentation for detailed information about handling events

### Functions
  - `FeralFile.loadProvenance()`: void
    - Dispatches `feralfile:provenance-ready` or `feralfile:provenance-request-error` events
  - `FeralFile.loadBlockchainInfo()`: void
    - Dispatches `feralfile:blockchain-info-ready` or `feralfile:blockchain-info-request-error` events
  - `FeralFile.random()`: number. Returns a deterministic random number seeded by `token_id`
  - `FeralFile.getVariables()`: object. Returns configuration variables from URL parameters
    ```js
    {
      blockchain: string,
      contract: string,
      tokenID: string,
      editionNumber: number,
      artworkNumber: number
    }
    ```

### Events
The library uses a custom event system to notify your artwork when data is ready. See the [Event Listeners](event-listeners.md) documentation for detailed information about handling events, error cases, and advanced patterns.

### URL Parameters
The library reads these from `window.location.search`:

| Param            | Type   | Notes                                                                      |
| ---------------- | ------ | -------------------------------------------------------------------------- |
| `blockchain`     | string | `"ethereum"` or `"tezos"`                           |
| `contract`       | string | Contract address                                                |
| `token_id`       | string | Used as RNG seed; if missing, a random token is generated (dev-friendly)   |
| `edition_number` | number | The edition number of the artwork                                                   |
| `artwork_number` | number | The artwork number within the series                                         |

To access parsed values:
```js
const vars = FeralFile.getVariables();
```

### Deterministic Randomness
To provide randomness to generative artworks, we offer a random function based on sfc32. The function takes token_id (passed as a URL parameter) as the seed of the randomness. This ensures that the randomness is deterministic. If the token_id is not given, the snippet will create a random one so you can test locally.

Use `FeralFile.random()` to get a deterministic random value in [0,1), seeded by `token_id`. This is implemented with a cyrb128 hash → sfc32 PRNG.

> **Warning**: When designing your randomness, ensure it remains deterministic based on the given `token_id`; otherwise, the artwork may change with each page reload.

### Network endpoints

- Feral File Indexer, request to get provenances
(POST) — https://indexer.feralfile.com/v2/nft/query

- Ethereum height
(GET) — https://api.blockcypher.com/v1/eth/main

### Notes
- The HTTP helper uses XMLHttpRequest and JSON parsing; non-2xx responses reject with `"response is not ok"` and invalid JSON rejects with `"Invalid JSON response"`. 
- If any of blockchain, contract, or token_id is missing, the provenance request does not run and an error event is dispatched. 
- Only support Ethereum chain height.
