from __future__ import annotations

from typing import Any

import requests

from azure_cost.models import AzurePrice


class AzurePricingClient:
    """Client for the Azure Retail Prices API."""

    BASE_URL = "https://prices.azure.com/api/retail/prices"

    def query_prices(self, filters: dict[str, str] | None = None) -> list[AzurePrice]:
        params = dict(filters or {})
        response = requests.get(self.BASE_URL, params=params, timeout=10)
        response.raise_for_status()

        payload = response.json() or {}
        items = payload.get("Items") or []
        if not isinstance(items, list):
            return []

        prices: list[AzurePrice] = []
        for item in items:
            if not isinstance(item, dict):
                continue

            try:
                price = AzurePrice(
                    service=str(item.get("serviceName", "")),
                    sku=str(item.get("armSkuName", "")),
                    region=str(item.get("armRegionName", "")),
                    meter=str(item.get("meterName", "")),
                    unit_price=float(item.get("unitPrice", 0.0)),
                    unit=str(item.get("unitOfMeasure", "")),
                    currency=str(item.get("currencyCode", "USD")),
                )
            except (TypeError, ValueError):
                continue

            prices.append(price)

        return prices

    def get_vm_prices(self, region: str, sku: str) -> list[AzurePrice]:
        filters = {
            "serviceName": "Virtual Machines",
            "armRegionName": region,
            "armSkuName": sku,
        }
        return self.query_prices(filters)
