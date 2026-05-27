# Real Estate Examples

## Example 1: "What's this property worth?"
```
us_get_valuation(address: "456 Oak Ave, San Francisco") → {estimate: 1250000, range: [1100000, 1400000]}
us_sales_history(address) → [{date: "2019", price: 980000}]
```
Response: "Estimated value: $1.25M (range: $1.1M-$1.4M). Last sold 2019 for $980k (+28% appreciation)."

## Example 2: "Compare Kenya vs Nigeria real estate markets"
```
compare_markets(countries: ["KE", "NG"]) → {KE: {mortgage: 12.5%, gdp: 5.1%}, NG: {mortgage: 18%, gdp: 3.2%}}
```
Response: "Kenya: lower rates (12.5% vs 18%), faster growth (5.1% vs 3.2%). More favorable for investment."
