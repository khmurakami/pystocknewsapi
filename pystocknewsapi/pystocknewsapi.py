#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is the wrapper for the Stocknewsapi

import os
import requests


# Insert your own key as a string here
# API_KEY = os.environ['STOCK_NEWS_API_KEY']

class NewsStreamer():

    def __init__(self, API_KEY):

        if API_KEY is None:
            raise Exception("No API KEY was passed in")

        self.root_url = "https://stocknewsapi.com/api/v1"
        self.client_id = API_KEY

    # https://www.mapillary.com/developer/api-documentation/#pagination
    def get_ticker_news(self, tickers="", items=20, date="", type="article",
                        source="CNBC", sentiment="neutral", tag="CEO",
                        tagexclude="CEO", fallback="true", page=1,
                        sortby="trending"):

        """Get news based on the specified company('s')

        Args:
            tickers (string): Name of the specified company
            items (int): Number of news items returned 1-50
            date (string): Format, DDMMYYYY - DDMMYYYY
            type (string): Video or Article
            source (string): Name of news source
            sentiment (string): positive, negative or neutral sentiment
            tag (string): Name of the tag you want to include
            tagexclude (string): Name of the you want to exclude
            page (int): Amount of pages you want
            sortby (string): Sort by this parameter

        Return:
            raw_json (dict): Dictionary of the result json requested

        Raises:
            Exception error: Uses HTTP error handler to check status code

        """

        url = self.root_url

        data = {
                 'tickers' : '{}'.format(tickers),
                 'items' : '{}'.format(items),
                 'date': '{}'.format(date),
                 'type': '{}'.format(type),
                 'source': '{}'.format(source),
                 'sentiment': '{}'.format(sentiment),
                 'tag': '{}'.format(tag),
                 'tagexclude': '{}'.format(tagexclude),
                 'page': '{}'.format(page),
                 'sortby': '{}'.format(sortby),
                 'token': '{}'.format(self.client_id)
                }

        r = requests.get(url, params=data)
        #http_error_handler(r.status_code)
        raw_json = r.json()
        return raw_json

    def get_all_ticker_news():

        pass

    def get_general_market_news(self, section="general", items=20,
                                type="article", source="CNBC",
                                sourceexclude="benzinga", sentiment="neutral"):

        """Get general market news

        Args:
            section (string): Section of the market news you want
            items (int): Number of news items returned 1-50
            type (string): Video or Article
            source (string): Name of news source
            sourceexclude (string): Name of the source you want to exclude
            sentiment (string): positive, negative or neutral sentiment

        Return:
            raw_json (dict): Dictionary of the result json requested

        Raises:
            Exception error: Uses HTTP error handler to check status code

        """

        url = self.root_url + '/category'

        data = {
                 'section' : '{}'.format(section),
                 'items' : '{}'.format(items),
                 'type': '{}'.format(type),
                 'source': '{}'.format(source),
                 'sourceexclude': '{}'.format(sourceexclude),
                 'sentiment': '{}'.format(sentiment),
                 'token': '{}'.format(self.client_id)
                }

        r = requests.get(url, params=data)
        #http_error_handler(r.status_code)
        raw_json = r.json()
        return raw_json
