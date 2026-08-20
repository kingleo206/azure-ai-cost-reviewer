from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class VirtualMachineConfig:
    region: str
    sku: str
    count: int
    os: str


@dataclass(frozen=True)
class AzurePrice:
    service: str
    sku: str
    region: str
    meter: str
    unit_price: float
    unit: str
    currency: str
