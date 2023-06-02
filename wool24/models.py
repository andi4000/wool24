# pylint: disable=missing-docstring

from typing import Optional

from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class UpstreamProductInfo(BaseModel):
    price: float
    available: bool
    vendor_product_url: str
    fullname: str
    needle_size: Optional[str] = None
    composition: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fullname: str = Field(index=True)
    brand: Optional[str]
    model: Optional[str]


class ProductDetails(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: Optional[int] = Field(default=None, foreign_key="product.id")
    price: float
    available: bool
    needle_size: Optional[str]
    composition: Optional[str]
    vendor_product_url: str
