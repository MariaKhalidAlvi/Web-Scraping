# Web-Scraping

This repository includes python projects on web-scraping using [Scrapy](https://scrapy.org/). It contains following projects
### 1. Amazon Scrapping:
This is a python project that scrapes data on books on Amazon from last thirty days. Scraped data includes Name of book, Name of author, Price Formates, Prices and Rating. The data is extracted from all the pages available using pagination technique. This also includes a Jupyter notebook that performes data cleaning. 

### 2. JavaScriptPagesScraping:
This is a python project that scrapes quotes data from [Quotes to Scrape]( http://quotes.toscrape.com/) JavaScript pages. It uses [Scrapy-Splash Plugin](https://github.com/scrapy-plugins/scrapy-splash) with help of Docker to render JavaScript code on webpages in order to scrape data using scrapy. Scraped data includes Quote, Author, and tags and is extracted from all available pages using pagination. The jupyter notebook displays the scraped data
 
### 3. QuotesScrapingWithLoggingIn:
This is a python project that scrapes quotes data from [Quotes to Scrape]( http://quotes.toscrape.com/) with required Login. Scraped data includes Quote, Author, and tags and is extracted from all available pages using pagination. The jupyter notebook displays the scraped data

### 4. TableDataScraping:
This is a python project that scrapes table data on cricket test series from [Espncricinfo](https://stats.espncricinfo.com/ci/engine/stats/index.html?class=1;template=results;type=batting). Scraped data includes Name. conuntry, span, runs, innings, average,notOuts ,matchesPlayes and inningsBatted is extracted from all available pages using pagination. The jupyter notebook displays the scraped data.
