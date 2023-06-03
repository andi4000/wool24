# pylint: disable=missing-docstring
from abc import ABC, abstractmethod
from typing import ClassVar, Optional, Type

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from wool24.models import UpstreamProductInfo


class ProductNotFoundException(Exception):
    pass


class WebsiteScraper(ABC):
    """Base class for all scrapers"""

    scrapers: ClassVar[list[Type["WebsiteScraper"]]] = []
    website_url = ""

    def __init_subclass__(cls: Type["WebsiteScraper"], **kwargs) -> None:  # type: ignore
        super().__init_subclass__(**kwargs)
        cls.scrapers.append(cls)

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    @abstractmethod
    def search_product_url(self, keywords: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_product_details(self, keywords: str) -> UpstreamProductInfo:
        raise NotImplementedError

    def get_optional_detail(self, xpath: str) -> Optional[str]:
        try:
            return self.driver.find_element(By.XPATH, xpath).text
        except NoSuchElementException:
            return None
