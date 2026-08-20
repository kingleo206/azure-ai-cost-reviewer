# AGENTS.md

## Project mission

This repository is the Day 1 foundation for an Azure AI Cost Reviewer. The long-term goal is to analyze Terraform infrastructure changes in Azure, calculate before/after cost impact, and use an LLM for cost explanations and engineering recommendations.

## Architectural rules

- Pricing calculations must be deterministic.
- LLMs must never invent Azure prices.
- Azure pricing API logic belongs in the pricing layer.
- Cost calculators should not perform HTTP requests.
- Add tests for cost calculation changes.
- Never commit Azure credentials, tokens, or secrets.

## Current scope

Day 1 intentionally focuses on:

- querying the Azure Retail Prices API
- looking up VM pricing records for a SKU
- representing Azure pricing values using typed Python models
- calculating estimated monthly VM compute cost
- providing a basic pytest test and CLI demo

This repository does not implement AI reasoning, Terraform parsing, GitHub integration, or non-VM Azure services yet.
