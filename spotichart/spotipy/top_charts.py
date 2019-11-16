# -*- coding: utf-8 -*-

"""
spotichart.spotipy.top_charts module.
Based upon the repo by fbkarsdorp
Located on https://github.com/fbkarsdorp/spotify-chart
"""

import io
import pandas as pd
import requests
import time
import tqdm


def get_chart(date, region='en', chart='top200'):
    """Download an individual chart

    :param date: Specific date for a Top Chart
    :type date: Date
    :param region: Spotify Top 50 region code, defaults to 'en'
    :type region: str, optional
    :param chart: Spotify chart to get the data from, either top200 or viral, defaults to 'top200'
    :type chart: str, optional
    :raises ValueError: Unavailable data requested
    :return: Top 50 Chart
    :rtype: pandas.DataFrame
    """

    chart = 'regional' if chart == 'top200' else 'viral'
    date = pd.to_datetime(date)
    if date.year < 2017:
        raise ValueError('No chart data available from before 2017')
    date = f'{date.date()}'
    url = f'https://spotifycharts.com/{chart}/{region}/daily/{date}/download'
    try:
        data = io.StringIO(requests.get(url).text)
        df = pd.read_csv(data, skiprows=1)  # Fix Spotify's Note
    except pd.errors.ParserError:
        df = None
        tqdm.tqdm.write(f'Empty set {chart}/{region}/daily/{date}')
    return df


def get_charts(start, end=None, region='global', chart='top200', sleep=1):
    """Fetch multiple Charts

    :param start: Starting date to download the chart
    :type start: Date
    :param end: End date for an interval of top charts, defaults to None
    :type end: Date, optional
    :param region: Spotify Top 50 region code, defaults to 'global'
    :type region: str, optional
    :param chart: Spotify chart to get the data from, either top200 or viral, defaults to 'top200'
    :type chart: str, optional
    :param sleep: Sleep time for the scraper to rest, defaults to 1
    :type sleep: int, optional
    :raises ValueError: Invalid date interval format
    :return: Chart with the Top 50 basic data
    :rtype: pandas.DataFrame
    """

    if end and (end < start):
        raise ValueError('Invalid Date format')
    end_date = start if end is None else end
    dfs = []
    for date in tqdm.tqdm(pd.date_range(start=start, end=end_date, freq='D')):
        df = get_chart(date, region=region, chart=chart)
        if df is not None:
            df['Date'] = date
            df = df.head(50)  # Just the Top 50 playlist
            dfs.append(df)
            time.sleep(sleep)
    if dfs:
        return pd.concat(dfs, ignore_index=True)
    else:
        return None
