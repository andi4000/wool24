# Wool24 Wool Comparison Site

# Usage

```bash
docker build . -t wool24
docker run wool24 -h

docker run wool24 -v "Drops Safran"
```

# Overview

- To extend scraping to new website, create subclass from `wool24.scraper.WebsiteScraper`, and
  implement the `get_product_details()` function.
- [Scrapy](https://scrapy.org/) seemed nice, but interacting with dynamic websites with it was
  very challenging. In the end I went with good ol' Selenium.
