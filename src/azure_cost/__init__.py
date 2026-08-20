"""Azure AI Cost Reviewer Day 1 package."""

from .calculator import HOURS_PER_MONTH, calculate_vm_monthly_cost
from .models import AzurePrice, VirtualMachineConfig

__all__ = [
    "AzurePrice",
    "HOURS_PER_MONTH",
    "VirtualMachineConfig",
    "calculate_vm_monthly_cost",
]
