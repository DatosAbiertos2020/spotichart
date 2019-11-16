# -*- coding: utf-8 -*-

"""spotichart.spotipy.main entry point module."""

from .top_charts import (
    get_charts
)

from .audio_features import (
    get_audio_features
)

import tqdm
import pandas as pd


def generate_top_chart(access_token, start, end=None, region='en',
                       chart='top200', sleep=1):
    """Function to fetch the top chart for a given date, and request their audio features

    :param access_token: Spotify Web API Access token
    :type access_token: str
    :param start: Starting point for the scraper to get the top chart
    :type start: Date
    :param end: Interval for multi-chart table, defaults to None
    :type end: Date, optional
    :param region: Spotify Top 50 region code, defaults to 'en'
    :type region: str, optional
    :param chart: Spotify chart to get the data from, either top200 or viral, defaults to 'top200'
    :type chart: str, optional
    :param sleep: Sleep time for the scraper to rest, defaults to 1
    :type sleep: int, optional
    :return: Dataframe that stores the chart data, and the audio features for each track
    :rtype: pandas.DataFrame
    """

    print('Downloading Top Charts')
    chart = get_charts(start, end, region, chart, sleep)
    chart['Track Id'] = chart['URL'].str.split("/", expand=True)[4]
    # Reduce the requests by just searching for different tracks
    chart_unique = chart.drop_duplicates('Track Id')
    audio_features = []

    print('Fetching Audio Features')
    for index, row in tqdm.tqdm(chart_unique.iterrows(), total=chart_unique.shape[0]):
        audio_features.append(get_audio_features(access_token, row['Track Id']))

    features = pd.DataFrame(audio_features)
    chart = pd.merge(chart, features, on='Track Id', how='left')

    return chart
