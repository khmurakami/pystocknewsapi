#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pystocknewsapi import NewsStreamer
from pystocknewsapi.utils import return_json_file

news_client = NewsStreamer("Insert API KEY HERE")

raw_json = news_client.get_ticker_news()
return_json_file(raw_json, "../example_json_files/get_ticker_news.json")
