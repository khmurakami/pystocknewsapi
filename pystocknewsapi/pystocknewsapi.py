#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is the wrapper for the Stocknewsapi

import os
import requests


# Insert your own key as a string here
# API_KEY = os.environ['STOCK_NEWS_API_KEY']

class NewsStreamer():

    def __init__(self, API_KEY):

        # Require an API Key
        if API_KEY is None:
            raise Exception("No API KEY was passed in")

        # Root URL. Subject to change
        self.root_url = "https://stocknewsapi.com/api/v1"
        self.client_id = API_KEY

    # https://www.mapillary.com/developer/api-documentation/#pagination
    def get_ticker_news(self, tickers="", items=20, date="", type="article",
                        source="CNBC", sentiment="neutral", tag="CEO",
                        tagexclude="CEO", fallback="true", page=1,
                        sortby="trending", datatype="csv"):

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
            datatype (string): Specify if you want to download as a CSV

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
                 'token': '{}'.format(self.client_id),
                 'datatype': '{}'.format(datatype)
                }

        r = requests.get(url, params=data)
        if r.status_code != 200:
            raise Exception('Unable to Return Request {}'
                            .format(r.status_code))

        raw_json = r.json()
        return raw_json

    def get_all_ticker_news(self, section="alltickets", items=50, data="", type="article", source="CNBC",
                            sentiment="positive", tag="CEO", tagexclude="CEO", sector="technology",
                            ipodate="", page=3, sortby="trending", datatype="csv"):

        """Retrive all news posted on all tickers

        Args:
            section (string): Leave this parameter as is
            items (int): Number of news items returned 1-50
            date (string): Format, DDMMYYYY - DDMMYYYY
            type (string): Video or Article
            source (string): Name of news source
            sentiment (string): positive, negative or neutral sentiment
            tag (string): Name of the tag you want to include
            tagexclude (string): Name of the you want to exclude
            sector (string): Filter by the sector. Example technology
            ipodate (string): Retrive news on companies that wnt ipo on a specific date
            page (int): Amount of pages you want
            sortby (string): Sort by this parameter
            datatype (string): Specify if you want to download as a CSV

        Return:
            raw_json (dict): Dictionary of the result json requested

        Raises:
            Exception error: Uses HTTP error handler to check status code

        """

        url = self.root_url + '/category'

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
        if r.status_code != 200:
            raise Exception('Unable to Return Request {}'
                             .format(r.status_code))

        raw_json = r.json()
        return raw_json


    def get_general_market_news(self, section="general", items=20,
                                type="article", source="CNBC",
                                sourceexclude="benzinga", sentiment="neutral",
                                datatype="csv"):

        """Get general market news

        Args:
            section (string): Section of the market news you want
            items (int): Number of news items returned 1-50
            type (string): Video or Article
            source (string): Name of news source
            sourceexclude (string): Name of the source you want to exclude
            sentiment (string): positive, negative or neutral sentiment
            datatype (string): Specify if you want to download as a CSV

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

        if r.status_code != 200:
            raise Exception('Unable to Return Request {}'
                             .format(r.status_code))

        raw_json = r.json()
        return raw_json
