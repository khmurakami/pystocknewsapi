#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file grabs all general market news by the StockNewsAPI Wrapper

from pystocknewsapi import NewsStreamer
from pystocknewsapi.utils import return_json_file

news_client = NewsStreamer("Insert API KEY")

# Possible variables that you can pass in
section = "general"
items = 50
type = "article"
source = "CNBC"
sourceexclude = "benzinga"
sentiment = "positive"
datatype = "csv"

raw_json = news_client.get_general_market_news(section=section, items=items,
                                               type=type, source=source,
                                               sourceexclude=sourceexclude,
                                               sentiment=sentiment,
                                               datatype=datatype)

return_json_file(raw_json, "../example_json_files/get_general_market_news.json")
