# Event Listeners

The Feral File Artwork JS Library uses a custom event system to notify your artwork when data is ready or errors occur. All events are dispatched on the `window` object.

Attach listeners before calling the loaders—events may fire shortly after the request resolves.

## Event Types

### Provenance Events

#### `feralfile:provenance-ready`
Fired when provenance data has been successfully loaded from the blockchain.

**Event Detail:**
```javascript
{
  detail: { 
    provenances: Array<ProvenanceRecord> 
  }
}
```

**Example Usage:**
```javascript
window.addEventListener('feralfile:provenance-ready', (event) => {
  const provenances = event.detail.provenances;
  console.log(`Found ${provenances.length} transactions`);

  if (!Array.isArray(provenances)) return;
  
  // Example: Change artwork based on number of transfers
  const transfers = provenances.filter(p => p.type === 'transfer');
  if (transfers.length > 5) {
    // This is a well-traveled artwork!
    addSpecialEffect();
  }
  
  // Example: Use first owner's address to influence design
  const mintRecord = provenances.find(p => p.type === 'mint');
  if (mintRecord) {
    const firstOwner = mintRecord.owner;
    const ownerInfluence = parseInt(firstOwner.slice(-4), 16) / 65535;
    adjustColorSaturation(ownerInfluence);
  }
});
```

#### `feralfile:provenance-request-error`
Fired when provenance data fails to load.

**Event Detail:**
```javascript
{
  detail: { 
    error: Error 
  }
}
```

**Example Usage:**
```javascript
window.addEventListener('feralfile:provenance-request-error', (event) => {
  console.error('Provenance failed:', event.detail.error);
  
  // Provide fallback behavior
  useDefaultProvenance();
  showOfflineIndicator();
});
```

### Blockchain Events

#### `feralfile:blockchain-info-ready`
Fired when blockchain information (like current block height) is available.

Note: the library exposes Ethereum block height; Tezos height is not fetched.

**Event Detail:**
```javascript
{
  detail: { 
    height: number 
  }
}
```

**Example Usage:**
```javascript
window.addEventListener('feralfile:blockchain-info-ready', (event) => {
  const blockHeight = event.detail.height;
  console.log(`Current block: ${blockHeight}`);
  
  // Example: Use block height to create time-based variations
  const timeVariation = blockHeight % 100;
  if (timeVariation < 10) {
    enableNightMode();
  } else if (timeVariation > 90) {
    enableDayMode();
  }
  
  // Example: Create periodic changes
  const cycle = Math.floor(blockHeight / 1000);
  setCycleTheme(cycle % 4);
});
```

#### `feralfile:blockchain-info-request-error`
Fired when blockchain data fails to load.

**Event Detail:**
```javascript
{
  detail: { 
    error: Error 
  }
}
```

**Example Usage:**
```javascript
window.addEventListener('feralfile:blockchain-info-request-error', (event) => {
  console.error('Blockchain info failed:', event.detail.error);
  
  // Use local time as fallback
  const fallbackHeight = Date.now() / 1000; // Rough block simulation
  useFallbackBlockHeight(fallbackHeight);
});
```

## Provenance Data Structure

Each provenance record has this structure:
```typescript
interface ProvenanceRecord {
    type: 'mint' | 'transfer';
    owner: string;           // Wallet address
    blockchain: string;      // 'ethereum' or 'tezos'
    blockNumber: number;     // Block where transaction occurred
    timestamp: string;       // ISO 8601 timestamp
    txid: string;           // Transaction hash
    txURL: string;          // Link to blockchain explorer
}
```

Provenance Data Example:
```json
  [
    {
      "type": "transfer",
      "owner": "0x5151f4b48CeE4f7dcB7714E7b4b836aa847Bf4e8",
      "blockchain": "ethereum",
      "blockNumber": 20134677,
      "timestamp": "2024-06-20T18:18:23Z",
      "txid": "0x52750ea1b7efeece11e8d10f2b5c0e3f4db854b6e8eac8e82f89b03a2b39f52f",
      "txURL": "https://etherscan.io/tx/0x52750ea1b7efeece11e8d10f2b5c0e3f4db854b6e8eac8e82f89b03a2b39f52f"
    },
    {
      "type": "mint",
      "owner": "0x457ee5f723C7606c12a7264b52e285906F91eEA6",
      "blockchain": "ethereum",
      "blockNumber": 18582877,
      "timestamp": "2023-11-16T07:12:59Z",
      "txid": "0xedfc4eca7c95911ee7c07cdfda14361998d84e5ea812404d42279665c0c74cf1",
      "txURL": "https://etherscan.io/tx/0xedfc4eca7c95911ee7c07cdfda14361998d84e5ea812404d42279665c0c74cf1"
    }
  ]
```

## Best Practices

### 1. Always Set Up Listeners First
```javascript
// ✅ Correct: Set up listeners before loading data
window.addEventListener('feralfile:provenance-ready', handleProvenance);
window.addEventListener('feralfile:blockchain-info-ready', handleBlockchain);

FeralFile.loadProvenance();
FeralFile.loadBlockchainInfo();

// ❌ Wrong: Race condition possible
FeralFile.loadProvenance();
window.addEventListener('feralfile:provenance-ready', handleProvenance);
```

### 2. Handle All Event Types
Always provide handlers for both success and error events:
```javascript
// Handle success
window.addEventListener('feralfile:provenance-ready', (event) => {
    // Use the data
});

// Handle failure
window.addEventListener('feralfile:provenance-request-error', (event) => {
    // Provide fallback behavior
});
```

### 3. Implement Progressive Enhancement
```javascript
// Show base artwork immediately
renderBaseArtwork();

// Enhance when data becomes available
window.addEventListener('feralfile:provenance-ready', () => {
    addProvenanceVisualization();
});

window.addEventListener('feralfile:blockchain-info-ready', () => {
    addBlockchainVisualization();
});
```

### 4. Clean Up Event Listeners
If you're creating dynamic artworks or single-page applications:
```javascript
function destroyArtwork() {
    window.removeEventListener('feralfile:provenance-ready', handleProvenance);
    window.removeEventListener('feralfile:provenance-request-error', handleProvenanceError);
    window.removeEventListener('feralfile:blockchain-info-ready', handleBlockchain);
    window.removeEventListener('feralfile:blockchain-info-request-error', handleBlockchainError);
}
```

### 5. Timeout Handling
Don't wait indefinitely for external data:
```javascript
const DATA_TIMEOUT = 10000; // 10 seconds

const timeoutId = setTimeout(() => {
    if (!hasAllData()) {
        console.log('Proceeding without complete data');
        proceedWithFallback();
    }
}, DATA_TIMEOUT);

// Clear timeout when all data is loaded
function onAllDataLoaded() {
    clearTimeout(timeoutId);
    proceedWithFullData();
}
```
