# -*- coding: utf-8 -*-

"""
spotichart.lyrics.lyrics_scraper module.

"""

import re
import requests
from bs4 import BeautifulSoup


def scrap_lyrics(lyrics_url, headers=False, ad_libs=False):
    """Download the lyrics from a resorce located on Genius,
    by web scraping.

    :param lyrics_url: Link to the Genius lyrics
    :type lyrics_url: str
    :param headers: Whether keep section headers or not.
        Section headers explained on: https://genius.com/9250687, defaults to False
    :type headers: bool, optional
    :param ad_libs: Keep the ad-libs sound effects (surrounded by parenthesis).
        Explained on https://genius.com/9257397, defaults to False
    :type ad_libs: bool, optional
    :return: Lyrics found
    :rtype: str
    """

    page = requests.get(lyrics_url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics = html.find('div', class_='lyrics').get_text()
    if not headers:
        lyrics = lyrics = re.sub('[\[].*?[\]]', '', lyrics)  # noqa: W605
    if not ad_libs:
        lyrics = lyrics = re.sub('\([^)]*\)', '', lyrics)  # noqa: W605
    return lyrics.replace('\n', ' ').replace('\r', '')
