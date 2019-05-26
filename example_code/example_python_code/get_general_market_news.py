#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pystocknewsapi import NewsStreamer
from pystocknewsapi.utils import return_json_file

news_client = NewsStreamer("Insert API Key Here")

raw_json = news_client.get_general_market_news()
return_json_file(raw_json, "../example_json_files/get_general_market_news.json")
