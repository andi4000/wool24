# Wool24 Wool Comparison Tool

# Usage

```bash
docker build . -t wool24
docker run wool24 -h

docker run wool24 -v "Drops Safran"  # writes to stdout
```

# Overview

- To extend scraping from a new website, create a new module in the directory
  `wool24/wool24/scrapers/`, subclass from `wool24.website_scraper.WebsiteScraper`, and implement
  the `get_product_details()` function.
- [Scrapy](https://scrapy.org/) seemed nice, but interacting with dynamic websites with it was
  very challenging. In the end I went with good ol' Selenium.
- Currently unit test is executed by crawling the actual live upstream website. This is bad
  practice for many reasons, but could be mitigated by having a local or cached site to be scraped.
