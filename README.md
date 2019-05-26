## pystocknewsapi

This is an Unofficial Wrapper for Pystocknewsapi

## Install

#### Install Locally

This has been tested with Python 2.7, 3.3, 3.4, 3.5, 3.6 and 3.6-dev

```shell
$ git clone https://github.com/khmurakami/pystocknewsapi
$ cd pystocknewsapi
$ python setup.py install
```

#### Install inside a Virtualenv

```shell
$ pip install virtualenv
$ python -m virutalenv env
$ source env/bin/activate
$ git clone https://github.com/khmurakami/pystocknewsapi
$ cd pystocknewsapi
$ python setup.py install
```

## Using the Python Wrapper

Descriptions of files can be found inside pystocktwits.py

## Samples

Code samples can be found in example_code/python_scripts
JSON sample outputs can be found in example_code/example_json_files

Get General Market News

```python
from pystocknewsapi import NewsStreamer

news_client = NewsStreamer("Insert API Key Here")

raw_json = news_client.get_general_market_news()
print(raw_json)
```

Result (Edited so save space)
```json
{
    "data": [
        {
            "date": "Fri, 24 May 2019 00:54:38 +0000",
            "image_url": "https://stocknewsapi.com/images/v1/m/0/m02d20190524t2i1390316997rlynxnpef4n00lw640.jpg",
            "news_url": "http://feeds.reuters.com/~r/reuters/businessNews/~3/dqn7aJC0ts4/oil-prices-stabilize-after-sharp-falls-earlier-in-week-idUSKCN1SU01P",
            "sentiment": "Neutral",
            "source_name": "Reuters",
            "tags": [],
            "text": "Oil markets stabilized on Friday amid OPEC supply cuts and tensions in the Middle East, after posting their steepest falls since the start of the year earlier in the week on the back of a global economic slowdown and swelling fuel inventories.",
            "title": "Oil prices stabilize after sharp falls earlier in week",
            "type": "Article"
        },
        {
            "date": "Thu, 23 May 2019 23:00:59 +0000",
            "image_url": "https://stocknewsapi.com/images/v1/g/e/gettyimages-141807344jpgw600.jpg",
            "news_url": "http://feedproxy.google.com/~r/Techcrunch/~3/l59Kf2c7RdE/",
            "sentiment": "Neutral",
            "source_name": "TechCrunch",
            "tags": [],
            "text": "Cars are here to stay, whether they have drivers or not. Automakers can ensure their seat at the table by implementing strategies better suited for the digital age.",
            "title": "Automakers have a choice: Become data companies or become irrelevant",
            "type": "Article"
        },
        {
            "date": "Thu, 23 May 2019 22:49:00 +0000",
            "image_url": "https://stocknewsapi.com/images/v1/x/g/103653654-ap-100111129746.jpg",
            "news_url": "https://www.cnbc.com/2019/05/23/ex-jc-penney-ceo-trade-deal-needed-by-end-of-year-or-retail-in-trouble.html",
            "sentiment": "Neutral",
            "source_name": "CNBC",
            "tags": [
                "CEO"
            ],
            "text": "\"If the tariffs don't get solved this year then you've got a real problem,\" former J.C. Penney CEO Allen Questrom says.",
            "title": "Former JC Penney CEO: China trade deal needed by end of year or retail's 'got a real problem'",
            "type": "Article"
        },
      ]
}
```

## Testing using Unit Tests

Run test script to test if it works properly

```shell
$ python tests/pystocknewsapi_test.py
```

## Links/Credits

- Git Ignore Used in this Repo: https://github.com/github/gitignore/blob/master/Python.gitignore
