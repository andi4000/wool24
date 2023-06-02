# pylint: disable=missing-docstring

from dataclasses import dataclass
from typing import Optional


@dataclass
class UpstreamProductInfo:
    price: float
    available: bool
    vendor_product_url: str
    name: str
    variant_name: Optional[str] = None
    needle_size: Optional[str] = None
    composition: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
