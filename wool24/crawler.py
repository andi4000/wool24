# pylint: disable=missing-docstring
import logging
from typing import Optional

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

from wool24 import scrapers
from wool24.models import UpstreamProductInfo
from wool24.website_scraper import ProductNotFoundException, WebsiteScraper


class Crawler:
    def __init__(self) -> None:
        self.driver: Optional[WebDriver] = None
        scrapers.load_modules()

    def scrape(self, keyword: str) -> list[UpstreamProductInfo]:
        """Scrape keyword and write to database."""
        logging.info("Booting up browser instance")
        opts = Options()
        opts.headless = True
        self.driver = webdriver.Firefox(options=opts)

        scraper_results: list[UpstreamProductInfo] = []
        for scraper in WebsiteScraper.scrapers:
            inst = scraper(self.driver)
            try:
                product_details = inst.get_product_details(keyword)
                scraper_results.append(product_details)
            except ProductNotFoundException:
                pass

        self.driver.close()
        logging.info("Browser instance closed.")

        return scraper_results
