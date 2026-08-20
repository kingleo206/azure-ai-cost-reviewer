from __future__ import annotations

HOURS_PER_MONTH = 730


def calculate_vm_monthly_cost(
    hourly_price: float,
    instance_count: int,
    hours_per_month: int = HOURS_PER_MONTH,
) -> float:
    """Calculate a deterministic monthly VM compute cost."""
    if hourly_price < 0:
        raise ValueError("hourly_price must be non-negative")
    if instance_count < 0:
        raise ValueError("instance_count must be non-negative")
    if hours_per_month <= 0:
        raise ValueError("hours_per_month must be greater than zero")

    return float(hourly_price * instance_count * hours_per_month)
