# -*- coding: utf-8 -*-

"""spotichart.lyrics.track_features entry module."""

from .track_features import (
    search_song
)

from .lyrics_scraper import (
    scrap_lyrics
)

from ..language import detect_language

import tqdm
import time
import pandas as pd


def get_lyrics_from_chart(access_token, chart, sleep=1):
    """Get track lyrics from a DataFrame with 'Track Id',
    'Track Name' and 'Artist' columns

    :param access_token: Genius API Access Token
    :type access_token: str
    :param chart: Pandas DataFrame to know Artist and Track Name
    :type chart: pandas.DataFrame
    :param sleep: Sleep timer to rest the scraper, defaults to 1
    :type sleep: int, optional
    :return: Dataframe with Lyrics and Language identified
    :rtype: pandas.DataFrame
    """
    lyrics_data = chart[['Track Id', 'Track Name', 'Artist']]
    lyrics_unique = lyrics_data.drop_duplicates('Track Id')
    lyrics_features = []

    print('Fetching Lyrics')
    for index, row in tqdm.tqdm(lyrics_unique.iterrows(), total=lyrics_unique.shape[0]):
        lyrics_features.append(get_lyrics(access_token, row['Track Id'],
                                          row['Track Name'], row['Artist']))
        time.sleep(sleep)

    features = pd.DataFrame(lyrics_features)
    return pd.merge(chart, features, on='Track Id', how='left')


def get_lyrics(access_token, track_id, track_name, artist):
    """Get the Lyrics for an individual track

    :param access_token: Genius API Access Token
    :type access_token: str
    :param track_id: Spotify Track Id, to identify different tracks
    :type track_id: str
    :param track_name: Track Name to search
    :type track_name: str
    :param artist: Track's Artist or Performer
    :type artist: str
    :return: Dictionary with the song Lyrics, Genius ID an Language identified
    :rtype: dict
    """
    lyrics_url, lyrics_id = search_song(access_token, track_name, artist)
    attributes = ['Track Id', 'Genius ID', 'Lyrics', 'Language']
    if lyrics_id and lyrics_url:
        lyrics = scrap_lyrics(lyrics_url)
        lang = detect_language(lyrics)
        features = dict(zip(attributes, [track_id, lyrics_id, lyrics, lang]))
        return features
    else:
        return dict()
