# SBS on Demand Australia Scraper

Scrapes movie data from SBS on Demand into a JSON file

![image](https://github.com/muhashi/sbsondemand-scraper/assets/105213357/b374589b-e1e2-46c6-b1b6-9ba0a4aafb4a)

# Installation

```
git clone https://github.com/muhashi/sbsondemand-scraper.git
cd sbsondemand-scraper
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
