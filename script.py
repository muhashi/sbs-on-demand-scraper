import argparse
import base64
import json
import math
import os
from time import sleep

import requests
from rich import print
from rich.progress import Progress

url = "https://catalogue.pr.sbsod.com/collections/all-movies"

def get_num_movies() -> int:
    default_value = 1000
    try:
        res = requests.get(url)
        json_results = res.json()
        has_total = json_results and "meta" in json_results and "total" in json_results["meta"] and json_results["meta"]["total"]
        return json_results["meta"]["total"] if has_total else default_value
    except Exception as e:
        return default_value

def scrape(max_pages: int = math.inf, delay_seconds: float = 1) -> list[dict]:
    i = 1
    items = []
    num_movies = get_num_movies()
    num_per_page = 100
    num_pages = math.ceil(num_movies / num_per_page)

    print(f"Found [green]{num_movies}[/green] movies across [green]{num_pages}[/green] pages")

    with Progress() as progress:
        task = progress.add_task("[blue]Scraping SBS on Demand...", total=num_pages)

        while True:
            if i > max_pages:
                break

            data = {
                "genre": "",
                "language": "",
                "limit": str(num_per_page),
                "page": str(i),
                "sort": "",
                "subtitle": "",
                "type": ""
            }

            encoded_data = base64.b64encode(json.dumps(data).encode("utf-8"))
            params = {
                "cursor": encoded_data.decode("utf-8")
            }

            try:
                res = requests.get(url, params=params)
                json_results = res.json()
            except Exception as e:
                print(f"[red]Request error: {e}[/red]")
                break

            if not json_results or not json_results.get("items") or len(json_results["items"]) == 0:
                break

            items.extend(json_results["items"])

            i += 1
            sleep(delay_seconds)
            progress.update(task, advance=1)

        return items

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="python script.py", description="Scrape SBS on Demand and save to JSON file")
    parser.add_argument("-o", "--output", type=str, help="Name of file to output JSON", required=True)
    parser.add_argument("-d", "--delay", type=int, help="Delay between requests in ms. Default is 1000ms", default=1000)

    args = parser.parse_args()

    save_filename = args.output

    delay_seconds = args.delay / 1000

    try:
        if not os.path.exists(os.path.dirname(save_filename)) and not os.path.dirname(save_filename) == "":
            os.makedirs(os.path.dirname(save_filename))
    except Exception as e:
        print(f"[red]Error creating directory: {e}[/red]")

    items = scrape(delay_seconds=delay_seconds)

    with (open(save_filename, "w")) as f:
        json.dump(items, f)
