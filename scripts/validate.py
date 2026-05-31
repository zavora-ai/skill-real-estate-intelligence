#!/usr/bin/env python3
"""Estimate property value using comparable sales approach."""
import json, sys

def estimate_value(data):
    comparables = data.get("comparables", [])
    subject_sqm = data.get("subject_sqm", 0)
    subject_bedrooms = data.get("bedrooms", 3)

    if not comparables or not subject_sqm:
        return {"error": "Need comparables[] and subject_sqm"}

    # Price per sqm from comparables, adjusted for bedroom count
    prices_per_sqm = []
    for comp in comparables:
        price_sqm = comp["price"] / comp["sqm"] if comp.get("sqm") else 0
        bed_adj = 1 + (subject_bedrooms - comp.get("bedrooms", 3)) * 0.05
        prices_per_sqm.append(price_sqm * bed_adj)

    avg_price_sqm = sum(prices_per_sqm) / len(prices_per_sqm)
    estimated = round(avg_price_sqm * subject_sqm, -3)

    return {
        "estimated_value": estimated,
        "price_per_sqm": round(avg_price_sqm, 2),
        "comparables_used": len(comparables),
        "confidence": "high" if len(comparables) >= 5 else "moderate" if len(comparables) >= 3 else "low"
    }

if __name__ == "__main__":
    print(json.dumps(estimate_value(json.loads(sys.argv[1])), indent=2))
