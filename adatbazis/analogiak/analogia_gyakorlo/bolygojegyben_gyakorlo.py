import json
import os


def read_file():

    with open("../../web_scraping/adat_tarolas/package.json", encoding="utf8") as f:
        bolygojegyben = json.load(f)["analogiak"]["bolygoJegyben"]
        return bolygojegyben



def main():
    analogiak = read_file()

if __name__ == '__main__':
    main()