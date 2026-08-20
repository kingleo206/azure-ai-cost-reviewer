from __future__ import annotations

from azure_cost.calculator import calculate_vm_monthly_cost
from azure_cost.pricing import AzurePricingClient


def main() -> None:
    region = "westus3"
    sku = "Standard_D4s_v5"
    count = 3

    client = AzurePricingClient()
    prices = client.get_vm_prices(region, sku)
    region_prices = [price for price in prices if price.region.lower() == region.lower()]

    print(f"Found {len(region_prices)} matching pricing records for region={region}, sku={sku}.")
    for price in region_prices:
        print(
            f"SKU: {price.sku} | meter: {price.meter} | "
            f"price: {price.currency} {price.unit_price} | unit: {price.unit} | region: {price.region}"
        )

    if not region_prices:
        print("No pricing records returned for this VM configuration in the requested region.")
        return

    selected_price = region_prices[0]
    example_monthly_cost = calculate_vm_monthly_cost(selected_price.unit_price, count)
    print(
        "Temporary Day 1 demo note: using the first matching Azure price record for the "
        "example monthly estimate. This is not guaranteed to be the correct Linux "
        "consumption price and will be filtered more carefully in Day 2."
    )
    print(
        f"Example monthly estimate for {count} VM(s): {selected_price.currency} "
        f"{example_monthly_cost:.2f}"
    )


if __name__ == "__main__":
    main()
