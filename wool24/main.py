# pylint: disable=missing-docstring
import argparse
import logging
import sys
from dataclasses import asdict
from io import TextIOWrapper

from wool24.crawler import Crawler

KEYWORDS_MIN_LENGTH = 4

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Scrape wool prices from various vendors"
    )
    parser.add_argument("keywords", type=str, help="Search keywords i.e. product name")
    parser.add_argument(
        "-o",
        "--out",
        nargs="?",
        type=argparse.FileType("w"),
        default=sys.stdout,
        help="Output file. Writes to stdout if not defined.",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Turn on verbosity"
    )

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.INFO)

    if len(args.keywords) < KEYWORDS_MIN_LENGTH:
        logging.error("Search keyword too short.")
        sys.exit()

    keywords: str = args.keywords
    outfile: TextIOWrapper = args.out

    crawler = Crawler()
    results = crawler.scrape(keywords)
    for result in results:
        outfile.write(str(asdict(result)))
        outfile.write("\n")
