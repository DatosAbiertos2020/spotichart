# -*- coding: utf-8 -*-

"""
spotichart.spotipy.top_charts module.
Based upon the repo by fbkarsdorp
Located on https://github.com/fbkarsdorp/spotify-chart
"""

import io
import sys
import pandas as pd
import requests
import time
import tqdm


def week_dates(date, weekday=0):
    """Calculate the starting date of a weekday

    :param date:  Staring point to calculate week members
    :type date: Date
    :param weekday: Weeks in a month, defaults to 0
    :type weekday: int, optional
    :return: Days intervale in that week
    :rtype: Date
    """

    week_start = date - pd.DateOffset(weekday=weekday, weeks=1)
    week_end = date + pd.DateOffset(weekday=weekday, weeks=0)
    return week_start, week_end


def get_chart(date, region='en', freq='daily', chart='top200'):
    """Download an individual chart

    :param date: Specific date for a Top Chart
    :type date: Date
    :param region: Spotify Top 50 region code, defaults to 'en'
    :type region: str, optional
    :param freq: Date frequency, either daily, weekly or monthly, defaults to 'daily'
    :type freq: str, optional
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
    if freq == 'weekly':
        start, end = week_dates(date, weekday=4)
        date = f'{start.date()}--{end.date()}'
    else:
        date = f'{date.date()}'
        if freq == 'monthly':
            freq = 'daily'
    url = f'https://spotifycharts.com/{chart}/{region}/{freq}/{date}/download'
    try:
        data = io.StringIO(requests.get(url).text)
        df = pd.read_csv(data, skiprows=1)  # Fix Spotify's Note
    except pd.errors.ParserError:
        df = None
        print(data)

    return df


def get_charts(start, end=None, region='en', freq='daily', chart='top200', sleep=1):
    """Fetch multiple Charts

    :param start: Starting date to download the chart
    :type start: Date
    :param end: End date for an interval of top charts, defaults to None
    :type end: Date, optional
    :param region: Spotify Top 50 region code, defaults to 'en'
    :type region: str, optional
    :param freq: Date frequency, either daily, weekly or monthly, defaults to 'daily'
    :type freq: str, optional
    :param chart: Spotify chart to get the data from, either top200 or viral, defaults to 'top200'
    :type chart: str, optional
    :param sleep: Sleep time for the scraper to rest, defaults to 1
    :type sleep: int, optional
    :raises ValueError: Invalid date interval format
    :raises ValueError: Wrong Date Frequency, should be daily, weekly or monthly
    :return: Chart with the Top 50 basic data
    :rtype: pandas.DataFrame
    """

    if end and (end < start):
        raise ValueError('Invalid Date format')
    if freq == 'daily':
        sample = 'D'
    elif freq == 'weekly':
        sample = 'W'
    elif freq == 'monthly':
        sample = 'MS'
    else:
        raise ValueError('Wrong frequency')
    end_date = start if end is None else end
    dfs = []
    for date in tqdm.tqdm(pd.date_range(start=start, end=end_date, freq=sample)):
        df = get_chart(date, region=region, freq=freq, chart=chart)
        if df is not None:
            df['Date'] = date
            df = df.head(50)
            dfs.append(df)
            time.sleep(sleep)
    return pd.concat(dfs, ignore_index=True)
