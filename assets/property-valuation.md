# Property Valuation Template

Use this structure when presenting property analysis results.

---

## 🏠 {property_address}

**Type:** {property_type} | **Listed:** ${listing_price} | **Status:** {listing_status}

### Property Details

| Field | Value |
|-------|-------|
| Bedrooms | {bedrooms} |
| Bathrooms | {bathrooms} |
| Sq Ft | {square_feet} |
| Lot Size | {lot_size} |
| Year Built | {year_built} |
| Zoning | {zoning} |

### Valuation

| Method | Estimate |
|--------|----------|
| Comparable Sales | ${comp_value} |
| Income Approach | ${income_value} |
| Assessed Value | ${assessed_value} |
| **Estimated FMV** | **${fair_market_value}** |

### Market Context

| Metric | Value |
|--------|-------|
| Days on Market | {dom} |
| Price/Sq Ft | ${price_per_sqft} |
| Neighborhood Avg | ${neighborhood_avg} |
| YoY Appreciation | {appreciation_pct}% |

{if listing_price > fair_market_value: "⚠️ Listed above estimated FMV — negotiate down"}
{if dom > 60: "⚠️ Extended time on market — seller may accept lower offer"}
{if appreciation_pct > 10: "🌟 Strong appreciation market"}

---

*Generated from mcp-real-estate | {timestamp}*
