from azure_cost.calculator import HOURS_PER_MONTH, calculate_vm_monthly_cost


def test_calculate_vm_monthly_cost() -> None:
    hourly_price = 0.50
    instance_count = 2

    expected = hourly_price * instance_count * HOURS_PER_MONTH

    assert calculate_vm_monthly_cost(hourly_price, instance_count) == expected
    assert calculate_vm_monthly_cost(hourly_price, instance_count) == 730.0
