# SBS on Demand Australia Scraper

Scrapes movie data from SBS on Demand into a JSON file

![image](https://github.com/muhashi/sbsondemand-scraper/assets/105213357/244dc2e5-f4ba-492c-86ad-677b3d056cf6)

# Installation

```
git clone https://github.com/muhashi/sbs-on-demand-scraper.git
cd sbs-on-demand-scraper
pip install -r requirements
python script.py --help
```

# Usage

```
python script.py --help
```

This will display the (very few) options

```yaml
usage: python script.py [-h] -o OUTPUT [-d DELAY]

Scrape SBS on Demand and save to JSON file

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Name of file to output JSON
  -d DELAY, --delay DELAY
                        Delay between requests in ms. Default is 1000ms
```
# Output

The output format depends on what [SBS's API](https://catalogue.pr.sbsod.com/collections/all-movies) returns, but here is an example of what the current output looks like:

```
[
  {
    "id": "123ecf45-dad9-58a4-8f40-3a45de6892dd",
    "entityType": "MOVIE",
    "title": "Teenage Mutant Ninja Turtles II: The Secret of the Ooze",
    "slug": "teenage-mutant-ninja-turtles-ii-the-secret-of-the-",
    "description": "The turtles team up with a news reporter against Shredder, who wants to create mutant monsters using the same radioactive material that created them.",
    "genres": [
      "Children",
      "Fantasy",
      "Adventure",
      "Film",
      "Action Adventure"
    ],
    "languages": [
      "English"
    ],
    "textTracks": [
      {
        "localeID": "en",
        "language": "English",
        "type": "SUBTITLE"
      }
    ],
    "availability": {
      "start": "2022-09-04T14:00:00Z",
      "end": "2023-08-31T13:59:59Z"
    },
    "hasAudioDescription": false,
    "classificationID": "PG",
    "images": [
      {
        "id": "2fc6d6a8-ea0d-5fb0-a644-2859d69331e2",
        "category": "2:3|960|1440|BANNER"
      }
    ],
    "distributors": [
      {
        "id": "137",
        "name": "Umbrella Entertainment"
      }
    ],
    "duration": "PT1H24M53S",
    "mpxMediaID": 2062068291765,
    "releaseYear": 1991
  },
  ...
]
```
