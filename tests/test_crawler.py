# pylint: disable=missing-docstring

from wool24.crawler import Crawler
from wool24.models import UpstreamProductInfo


def test_product_found() -> None:
    crawler = Crawler()
    expected = UpstreamProductInfo(
        price=1.3,
        available=True,
        vendor_product_url="https://www.wollplatz.de/wolle/drops/drops-safran",
        brand="Drops",
        composition="100% Baumwolle",
        model=None,
        name="Drops Safran",
        needle_size="3 mm",
        variant_name="Drops Safran 1 Light-pink",
    )
    results = crawler.scrape("Drops Safran")
    assert len(results) == 1
    assert expected == results[0]


def test_product_not_found() -> None:
    crawler = Crawler()
    results = crawler.scrape("To be, or not to be")
    assert len(results) == 0
