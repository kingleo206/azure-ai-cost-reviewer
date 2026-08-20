from __future__ import annotations

from typing import Any

from azure_cost.pricing import AzurePricingClient


def test_query_prices_handles_pagination(monkeypatch) -> None:
    client = AzurePricingClient()
    calls: list[tuple[str, dict[str, str] | None]] = []

    class FakeResponse:
        def __init__(self, payload: dict) -> None:
            self._payload = payload

        def raise_for_status(self) -> None:
            return None

        def json(self) -> dict:
            return self._payload

    def fake_get(url: str, params: dict[str, str] | None = None, timeout: int = 10):
        calls.append((url, params))

        if url == client.BASE_URL:
            return FakeResponse(
                {
                    "Items": [
                        {
                            "serviceName": "Virtual Machines",
                            "armSkuName": "Standard_D2s_v5",
                            "armRegionName": "westus3",
                            "meterName": "D2s v5",
                            "unitPrice": 0.10,
                            "unitOfMeasure": "1 Hour",
                            "currencyCode": "USD",
                        }
                    ],
                    "NextPageLink": "https://prices.azure.com/api/retail/prices?$skiptoken=abc123",
                }
            )

        if url == "https://prices.azure.com/api/retail/prices?$skiptoken=abc123":
            return FakeResponse(
                {
                    "Items": [
                        {
                            "serviceName": "Virtual Machines",
                            "armSkuName": "Standard_D2s_v5",
                            "armRegionName": "westus3",
                            "meterName": "D2s v5",
                            "unitPrice": 0.20,
                            "unitOfMeasure": "1 Hour",
                            "currencyCode": "USD",
                        }
                    ]
                }
            )

        raise AssertionError(f"Unexpected URL requested: {url}")

    monkeypatch.setattr("azure_cost.pricing.azure_client.requests.get", fake_get)

    prices = client.query_prices({"serviceName": "Virtual Machines"})

    assert len(prices) == 2
    assert [price.unit_price for price in prices] == [0.10, 0.20]
    assert calls[0] == (client.BASE_URL, {"serviceName": "Virtual Machines"})
