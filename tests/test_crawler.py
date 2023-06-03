# pylint: disable=missing-docstring

from wool24.crawler import Crawler


def test_product_found() -> None:
    crawler = Crawler()
    results = crawler.scrape("Drops Safran")
    assert len(results) == 1
    assert results[0].brand.lower() == "drops"
    assert "baumwolle" in results[0].composition.lower()
    assert "drops" in results[0].variant_name.lower()


def test_product_not_found() -> None:
    crawler = Crawler()
    results = crawler.scrape("nonexistent product")
    assert len(results) == 0
