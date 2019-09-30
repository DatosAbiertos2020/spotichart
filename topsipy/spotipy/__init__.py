# -*- coding: utf-8 -*-

"""spotipy package."""

from __future__ import unicode_literals

from .__about__ import (
    __version__
)

from .top_charts import (
    get_charts
)

from .audio_features import (
    get_audio_features,
    get_several_audio_features
)

import tqdm
import time
import pandas as pd

spotify_attr = ['Track Id', 'acousticness', 'danceability',
                    'duration_ms', 'energy', 'instrumentalness',
                    'key', 'liveness', 'loudness', 'mode',
                    'speechiness', 'tempo', 'time_signature',
                    'valence']

def generate_top_chart(access_token, start, end=None, region='en', freq='daily', chart='top200', sleep=1):
    chart = get_charts(start, end, region, freq, chart, sleep)
    chart['Track Id'] = chart['URL'].str.split("/",expand=True)[4]
    # Reduce the requests by just searching for different tracks
    chart_unique = chart.drop_duplicates('Track Id')
    audio_features = []
    for index, row in tqdm.tqdm(chart_unique.iterrows(), total=chart_unique.shape[0]):
        audio_features.append(get_audio_features(access_token, row['Track Id']))
    features = pd.DataFrame(audio_features)
    chart = pd.merge(chart, features, on='Track Id', how='left')
        
    return chart