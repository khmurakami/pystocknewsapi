#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pystocknewsapi import NewsStreamer
from pystocknewsapi.utils import return_json_file

news_client = NewsStreamer("Insert API Key Here")

# Types of variables that you can pass in
section = "alltickers"
items = 50
date = "03152019-03252019"
type = "article"
source = "CNBC"
sentiment = "positive"
tag = "CEO"
tagexclude = "CEO"
sector = "technology"
ipodate = "01012018-12312018"
page = 3
sortby = "trending"
datatype = "csv"

raw_json = news_client.get_all_ticker_news(section=section, items=items,
                                           date=date, type=type, source=source,
                                           sentiment=sentiment, tag=tag,
                                           tagexclude=taxexclude, sector=sector,
                                           ipodate=ipodate, page=page,
                                           sortby=sortby, datatype=datatype)

return_json_file(raw_json, "../example_json_files/get_all_ticker_news.json")
