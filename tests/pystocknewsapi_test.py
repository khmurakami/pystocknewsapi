#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file does a unittest of the Pystocknewsapi

# System Libraries
import unittest
import os

from pystocknewsapi import NewsStreamer

# Insert your own key as a string here
API_KEY = os.environ['STOCK_NEWS_API_KEY']

class TestPyStockNewsAPI(unittest.TestCase):

    def test_get_ticker_news():

        news = NewsStreamer(API_KEY)

        raw_json = news.get_ticker_news()

        self.assertEqual(type({}), raw_json)

   def test_get_all_ticker_news():

       news = NewsStreamer(API_KEY)

       raw_json = news.get_all_ticker_news()

       self.assertEqual(type({}), raw_json)

   def test_get_general_market_news():

       news = NewsStreamer(API_KEY)

       raw_json = news.get_general_market_news()

       self.assertEqual(type({}), raw_json)


if __name__ == '__main__':
    unittest.main()
