# pylint: disable=missing-docstring
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from wool24.models import UpstreamProductInfo
from wool24.scrapers import ProductNotFoundException, WebsiteScraper


class WollPlatz(WebsiteScraper):
    website_url = "https://wollplatz.de"

    def search_product_url(self, keywords: str) -> str:
        self.driver.get(self.website_url)
        search_box = self.driver.find_element(By.ID, "searchSooqrTop")
        search_box.click()
        search_box.send_keys(keywords)

        # TODO: handle TimeoutException
        search_result = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "productlist-mainholder"))
        )

        product_url: str = search_result.find_element(
            By.XPATH, ".//h3/a"
        ).get_attribute("href")

        if not product_url:
            raise ProductNotFoundException

        return product_url

    def get_product_details(self, keywords: str) -> UpstreamProductInfo:
        product_url: str = self.search_product_url(keywords)
        self.driver.get(product_url)

        price_str: str = self.driver.find_element(
            By.XPATH,
            "//div[contains(@class, 'buy-price')]//span[contains(@class, 'product-price-amount')]",
        ).text

        price: float = float(price_str.replace(",", "."))

        availability_el: str = self.driver.find_element(
            By.XPATH,
            "//tr[contains(@class, 'pbuy-voorraad')]"
            "//span[contains(@class, 'stock')]",
        ).text
        available: bool = availability_el.lower() == "lieferbar"

        product_fullname: str = self.driver.find_element(
            By.XPATH, "//h1[contains(@id, 'pageheadertitle')]"
        ).text

        needle_size = self.get_optional_detail(
            "//td[.='Nadelstärke']/following-sibling::td[1]"
        )
        composition = self.get_optional_detail(
            "//td[.='Zusammenstellung']/following-sibling::td[1]"
        )
        brand = self.get_optional_detail("//td[.='Marke']/following-sibling::td[1]")

        return UpstreamProductInfo(
            price=price,
            available=available,
            vendor_product_url=product_url,
            fullname=product_fullname,
            brand=brand,
            composition=composition,
            needle_size=needle_size,
        )
