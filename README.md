# sentiment-analyzer-test
Retrieves product reviews from https://argos.co.uk/, and provides sentiment analysis for a general overview of whether the product reviews are positive, negative, or neutral. May be expanded in future.

A combination webscraper and sentiment analyser using: pandas, selenium, nltk and matplotlib.

## Dependencies
This program uses [selenium](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/#quick-reference)
Firefox driver. specifically it uses the `geckodriver`. With the provided link, please ensure
the correct geckodriver is installed and the driver is in `$PATH` before proceeding.

## How to run
To run this program, first clone this repository, open a terminal, and navigate to the repository location, then run:
```bash
python main.py
```
**Note** A rare bug can occur where selenium reports `x obscures it` error, this can be
ignored. should this happen simply re-run the program.

## Features
* Selenium: This project uses selenium to scrape webpages headlessly.
* Matplotlib: This project displays a bar chart to show quantity of star ratings.
* NLTK: This project utilises Natural Language Processing to analyse sentiment of customer reviews.

## Collaborators
[Jamie Scollay](https://github.com/deltabrot/) collaborated with me on this project by providing
tutelage on HTML elements, as well as providing code review and assistance refactoring the finished code.

## License
MIT License