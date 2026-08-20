# Azure AI Cost Reviewer

Day 1 foundation for deterministic Azure VM cost analysis.

## Goals

- Query the official Azure Retail Prices API.
- Look up Azure VM SKU pricing records.
- Represent pricing data using typed Python models.
- Calculate monthly VM compute cost deterministically.
- Keep cost calculations separate from HTTP-based pricing retrieval.
- Provide a simple CLI demo using a real Azure VM SKU.

## Project structure

```text
azure-ai-cost-reviewer/
├── README.md
├── AGENTS.md
├── .gitignore
├── pyproject.toml
├── src/
│   └── azure_cost/
│       ├── __init__.py
│       ├── main.py
│       ├── models.py
│       ├── calculator.py
│       └── pricing/
│           ├── __init__.py
│           └── azure_client.py
├── tests/
│   └── test_calculator.py
└── examples/
```

## Quick start

```bash
python -m pip install -e .[dev]
python -m azure_cost.main
pytest
```

## Important architecture rules

- AI must never invent Azure prices.
- Pricing retrieval and cost calculation are deliberately separate layers.
- The Azure Retail Prices API is the pricing source of truth.
- Day 1 uses the first matching price record only for a temporary demo scenario.
- Future work will add explicit OS, meter, and pricing-type filtering.
