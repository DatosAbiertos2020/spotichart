# -*- coding: utf-8 -*-

"""
spotichart.lyrics.track_features module.

"""

import requests
import urllib.parse


def request_song_info(access_token, track_name, artist):
    """Search the track's metadata in Genius

    :param access_token: Genius API access token
    :type access_token: str
    :param track_name: Track Name
    :type track_name: str
    :param artist: Track's Artist or Performer
    :type artist: str
    :return: Genius API response
    :rtype: json
    """

    query = urllib.parse.quote(track_name + ' ' + artist, safe='')
    JSONContent = requests.get("https://api.genius.com/search?q=" + query,
                               headers={
                                   "User-Agent": "CompuServe Classic/1.22",
                                   "Accept": "application/json",
                                   "Host": "api.genius.com",
                                   "Authorization": "Bearer " + access_token,
                               },
                               cookies={},
                               ).json()

    return JSONContent


def search_song(access_token, track_name, artist):
    """Locate the song's lyrics in Genius, to know its url

    :param access_token: Genius API Access Token
    :type access_token: str
    :param track_name: Track Name
    :type track_name: str
    :param artist: Track's Artist or Performer
    :type artist: str
    :raises ValueError: Error on response
    :return: Track's lyrics and id on Genius
    :rtype: str
    """
    response = request_song_info(access_token, track_name, artist)
    json = response
    if json['meta']['status'] != 200:
        raise ValueError(json['meta']['status']['message'])
    if not json['response']['hits']:
        return None, None
    lyrics_url = json['response']['hits'][0]['result']['url']
    lyrics_id = json['response']['hits'][0]['result']['id']

    return lyrics_url, lyrics_id
