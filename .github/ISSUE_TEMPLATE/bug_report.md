---
name: Bug report
about: Create a report to help us improve
title: ''
labels: ''
assignees: ''

---

#### 🔖 Title (verb-first, e.g., "[Bug] Fix rotation reset after power cycle on FF1")

---

#### 🌍 Overview – Why does this matter?
<1-2 sentences on user/business impact. Tie to vision, e.g., "Breaks '5-minute setup' by requiring manual re-pairing, reducing joy and adoption.">

---

#### 🐞 Bug Details
- **Reproduction Steps**:  
  1. <Step 1, e.g., "Pair device via mobile app.">  
  2. <Step 2, e.g., "Turn off Samsung Frame overnight.">  
  3. <Repro rate, e.g., "Happens 80% of time on v1.2.0.">  

- **Expected Behavior**:  
  <What should happen, e.g., "Screen remains vertical on wake-up.">

- **Actual Behavior**:  
  <What happens instead, e.g., "Rotates to horizontal; requires app intervention.">

- **Environment**:  
  - FF OS: <e.g., v0.6>  
  - Mobile App Version: <e.g., v0.63.0(579) Android>  
  - Network: <e.g., Wi-Fi, no VPN>
  - Screen: <e.g., Samsung Frame 55" 2024>

- **Logs/Screenshots**:  
  <Paste logs from journalctl or runbook; attach images/videos. e.g., "See attached repro.mp4. Log: `sig verify failed` from pairing-api.">

---

#### 📌 Core Requirements (Triage Checklist)
- [ ] Reproducible locally? (Run on lab device per KMS Runbook.)  
- [ ] Tied to SLO? (e.g., p90 reconnect <2s from OSS Guidance.)  
- [ ] Scope Estimate: <e.g., "2d spike for debug + fix.">  
- [ ] Related Issues/PRs: <Link to cross-repo issues, e.g., #123 in ffos.>  
- [ ] Tests Needed: <e.g., Add to Firmware System Tests (OTA, Factory Reset).>  

---

(Internal use below)

#### ✅ Acceptance Criteria
| Scenario | Pass Condition |
|----------|----------------|
| Repro Attempt | Bug no longer occurs in 10/10 tests on lab device. |
| System Test | Passes OTA Update + Factory Reset from Firmware Process. |
| Visual/UI Check | Meets Component Done Checklist (e.g., visual diffs green). |
| Metrics | <e.g., Uptime >99% over 24h; log no errors in Grafana.> |
| Community Verify | <Optional: External tester confirms on public board.> |

_(Limit to 3-5; aim for <5 min local verify.)_

---

#### 🛰️ Meta 
| Field | Value |
|-------|-------|
| **Priority** | High/Med/Low (e.g., High if blocks FF1 launch). |
| **Labels** | `bug`, `ff1`, `device`, `orbit-1`, `@band: Device-Runtime`. |
| **Affected Repos** | <e.g., ffos, feralfile-device>. ||
| **Milestone** | <e.g., Orbit-1 (YYYY-MM-DD).> |
