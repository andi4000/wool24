# pylint: disable=missing-docstring
import os
import traceback
from abc import ABC, abstractmethod
from importlib import util
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


def load_module(module_path: str):  # type: ignore
    name = os.path.split(module_path)[-1]
    spec = util.spec_from_file_location(name, module_path)
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


path = os.path.abspath(__file__)
dirpath = os.path.dirname(path)

for fname in os.listdir(dirpath):
    # load python files in this directory as module
    if (
        not fname.startswith(".")
        and not fname.startswith("__")
        and fname.endswith(".py")
    ):
        try:
            load_module(os.path.join(dirpath, fname))
        except Exception:
            traceback.print_exc()
