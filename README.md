# Wool24 Wool Comparison Site

# Usage

```bash
docker compose build

# TODO: Populate DB with initial data

```

# Requirements

## Functional Features

0. Main

- The listed balls of wool are automatically searched for on the website using the brand and name
- If available, following information are stored in a file for each of the listed balls of wool:
  - price
  - availability
  - needle size
  - composition

1. Product lookup by User
   As a user, I want to easily lookup for price information by entering brand and model name of the desired product.

2. Add website by Moderator
   As Moderator/Admin, I want to easily add a new website as source for price comparison

# Specification

## Functional Features

0. Main
   TODO

1. Product lookup by user
   TODO

2. Add website by Moderator

- Moderator needs to add following things:
  - link to search on the website
  - parent element of the search result

## Non-Functional Features

- Lookup of uncached product will trigger scraping
- Once cached, background cron job should scrape and update the cache
- Product lookup will only return results from cache

## Components

- `main.py`: contains API endpoints
- `scraper.py`: scaper utilities
- `utils.py`: CLI util for:
  - populate DB with initial initial
  - trigger scraping and cache update

docker-compose:

- main app
  - mounts for:
    - database
- ophelia cron that calls utils.py to scrape and update cache periodically

## Flow

- user enters product name in lookup
- entry will be queried in database with `*string*`
- if query returns more than one, show list of link to the products
- if only one entry, show product prices page
- product prices page contains prices from different vendors
- if db query returns zero match, run scraper on upstream websites, then show product prices page

## Design Decisions

1. Simple scraping instead of finding out API endpoints
   for ease of adding new sites by the moderator

# Outlook

- use `decimal.Decimal` for money amount?
- error handling for various changes on upstream websites
- better mechanism to add new website
- better product name clustering and matching

# TODO

- trigger crawl from API
- from main page of the website to search result

Refs:

- https://docs.scrapy.org/en/latest/topics/practices.html
