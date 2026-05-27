# Real Estate Intelligence Skill

> Global property intelligence for AI agents — transactions, valuations, market comparisons, and geocoding across US, UK, EU, Africa, Middle East, and Asia-Pacific.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--real--estate-green)](https://github.com/zavora-ai/mcp-real-estate)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Calls | What It Achieves |
|----------|-------|------------------|
| Property Valuation | 2-3 | Estimate + comparables + context |
| Market Comparison | 2 | Side-by-side country indicators |
| Property Search | 1-2 | Find listings by location |
| Transaction History | 1 | Past sales for a property/area |

### Global Coverage

| Region | Data Source | Capabilities |
|--------|-----------|-------------|
| US | Zillow/Redfin APIs | Valuations, sales history, search |
| UK | Land Registry | Transactions, average prices |
| UAE/ME | Listings APIs | Sale/rent listings |
| Global | World Bank + OSM | Market indicators, geocoding |

## Installation

```bash
git clone https://github.com/zavora-ai/skill-real-estate-intelligence.git \
  ~/.skills/skills/real-estate-intelligence
```

## Requirements

**Required:** `mcp-real-estate` (11 tools)
**Cross-MCP:** `mcp-finance` (ROI calculations), `mcp-crm` (client research)

## Success Criteria

| Metric | Target |
|--------|--------|
| Valuation quality | Always include comparables |
| Market context | Lending rates + trends with every valuation |
| Global coverage | US, UK, UAE, and 200+ country macro data |

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)
