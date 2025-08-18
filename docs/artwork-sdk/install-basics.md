# Artwork JS Library
-----------------------------------
## What is the Feral File Artwork JS Library?

The Feral File Artwork JS Library is a lightweight, dependency-free JavaScript library for software artworks on Feral File, enabling software artwork developers to create variants by integrating this library.

### Key Features
- **Deterministic randomness** seeded by token ID
- **Provenance data** from blockchain transactions - essential building blocks for creating dynamic artworks that respond to their on-chain history
- **Blockchain data** access block height

### Installation

#### CDN (Recommended)

Load the library via CDN by adding the script tag to your HTML:
```html
<script src="https://ipfs.feralfile.com/ipfs/Qmc4zwYthfKRNMgoMJN16DEyjoxmZmjikLBzA1yVB7reDr" type="text/javascript"></script>
```

The script attaches a global:
```js
window.FeralFile // { loadProvenance, loadBlockchainInfo, random, getVariables }
```

#### Self-hosted

Download the latest release from [GitHub](https://github.com/feral-file/ffa-js/releases) and host it yourself:
```html
<script src="./path/to/feralfile-artwork.js"></script>
```

#### Browser Support
- Modern browsers (Chrome 60+, Firefox 55+, Safari 12+)
- ES6 support required
- No Internet Explorer support

### Quickstart
  ```html
  <head>
    <script src="https://ipfs.feralfile.com/ipfs/Qmc4zwYthfKRNMgoMJN16DEyjoxmZmjikLBzA1yVB7reDr" type="text/javascript"></script>
  </head>
  <body>
    <script>
      // Listen for results:
      window.addEventListener('feralfile:provenance-ready', (e) => {
        console.log('Provenance:', e.detail.provenances);
      });

      window.addEventListener('feralfile:blockchain-info-ready', (e) => {
        console.log('Block height:', e.detail.height);
      });

       window.addEventListener('feralfile:provenance-request-error', (e) => {
        console.log('Provenance request error:', e.detail.error);
      });

      window.addEventListener('feralfile:blockchain-info-request-error', (e) => {
        console.log('Blockchain info request error:', e.detail.error);
      });

      // Load data, Kick off requests:
      FeralFile.loadProvenance();
      FeralFile.loadBlockchainInfo();

      // Get variables and deterministic random number
      console.log(FeralFile.getVariables());
      console.log(FeralFile.random());
    </script>
  </body>
  ```

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
The SDK uses a custom event system to notify your artwork when data is ready. See the [Event Listeners](event-listeners.md) documentation for detailed information about handling events, error cases, and advanced patterns.

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
