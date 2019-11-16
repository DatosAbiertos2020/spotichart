# -*- coding: utf-8 -*-

"""
spotichart.spotipy.audio_features module.


"""

import pandas as pd
import requests

spotify_attr = ['Track Id', 'acousticness', 'danceability',
                'duration_ms', 'energy', 'instrumentalness',
                'key', 'liveness', 'loudness', 'mode',
                'speechiness', 'tempo', 'time_signature',
                'valence']


def get_audio_features(access_token, track_id):
    """Function to fetch the audio features of a song

    :param access_token: Spotify Web API Access Token
    :type access_token: str
    :param track_id: Spotify Track identifier
    :type track_id: str
    :raises ValueError: Spotify Request Error
    :raises ValueError: Http Request Error
    :return: Track's audio features
    :rtype: dict
    """

    track_data = []
    features = pd.DataFrame
    global spotify_attr
    try:
        JSONContent = requests.get("https://api.spotify.com/v1/audio-features/" + track_id,
                                   headers={
                                       "Accept": "application/json",
                                       "Authorization": "Bearer " + access_token,
                                       "Content-Type": "application/json"
                                   },
                                   cookies={},
                                   ).json()
        track_data.append(track_id)
        for attr in spotify_attr[1:]:
            track_data.append(JSONContent[attr])
    except KeyError:
        if JSONContent['error']:
            raise ValueError(JSONContent['error']['message'])
    except requests.exceptions.RequestException:  # This is the correct syntax
        raise ValueError('\nError during request')

    features = dict(zip(spotify_attr, track_data))
    return features
