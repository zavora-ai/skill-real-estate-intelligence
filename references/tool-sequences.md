# Real Estate Tool Sequences (11 tools)

## UK (2): uk_search_transactions, uk_average_price
## Geocoding (3): geocode_search, reverse_geocode, search_properties_nearby
## Markets (2): get_market_indicators, compare_markets
## US (3): us_search_properties, us_get_valuation, us_sales_history
## Middle East (1): me_search_listings

## Sequence: Property Valuation (3 calls)
```
1. us_get_valuation(address: "123 Main St, Austin TX") → {estimate: 450000, confidence: "high"}
2. us_sales_history(address) → [{date: "2020", price: 380000}, {date: "2018", price: 320000}]
3. search_properties_nearby(lat, lon, radius: "1km") → comparable listings
```

## Sequence: Market Comparison (2 calls)
```
1. get_market_indicators(country: "KE") → {mortgage_rate: 12.5%, gdp_growth: 5.1%, urbanization: 28%}
2. compare_markets(countries: ["KE", "NG", "ZA"]) → side-by-side table
```
