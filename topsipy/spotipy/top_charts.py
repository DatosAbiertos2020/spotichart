"""
topsipy.spotipy.top_charts module.
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
    week_start = date - pd.DateOffset(weekday=weekday, weeks=1)
    week_end = date + pd.DateOffset(weekday=weekday, weeks=0)
    return week_start, week_end


def get_chart(date, region='en', freq='daily', chart='top200'):
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
        df = pd.read_csv(data, skiprows=1) # Fix Spotify's Note
    except pd.errors.ParserError:
        df = None
        print(data)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print('\nError during request')
        sys.exit(1)
    return df


def get_charts(start, end=None, region='en', freq='daily', chart='top200', sleep=1):
    if freq == 'daily':
        sample = 'D'
    elif freq == 'weekly':
        sample = 'W'
    elif freq == 'monthly':
        sample = 'MS'
    else:
        raise ValueError('Wrong frequency')
    end_date = start if end == None else end
    dfs = []
    for date in tqdm.tqdm(pd.date_range(start=start, end=end_date, freq=sample)):
        df = get_chart(date, region=region, freq=freq, chart=chart)
        if df is not None:
            df['Date'] = date
            df = df.head(50)
            dfs.append(df)
            time.sleep(sleep)
    return pd.concat(dfs, ignore_index=True)