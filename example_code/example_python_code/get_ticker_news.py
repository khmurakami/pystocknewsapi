#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pystocknewsapi import NewsStreamer
from pystocknewsapi.utils import return_json_file

news_client = NewsStreamer("Insert API KEY HERE")

# Types of variables that you can pass in
tickers = "FB,AMZN"
items = 50
date = "03152019-03252019"
type = "article"
source = "CNBC"
sourceexclude = "benzinga"
sentiment = "positive"
tag = "CEO"
tagexclude = "CEO"
fallback = "true"
page = 3
sortby = "trending"
datatype = "csv"

# Get ticker news by these parameters and return as JSON
raw_json = news_client.get_ticker_news(tickers=tickers, items=items, date=date,
                                       type=type, source=source,
                                       sourceexclude=sourceexclude,
                                       sentiment=sentiment, tag=tag,
                                       tagexclude=tagexclude, fallback=fallback,
                                       page=page, sortby=sortby,
                                       datatype=datatype)

# Download the JSON file
return_json_file(raw_json, "../example_json_files/get_ticker_news.json")
