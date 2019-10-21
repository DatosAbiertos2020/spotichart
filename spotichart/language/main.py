# -*- coding: utf-8 -*-
"""language detector main module"""

from __future__ import unicode_literals

from guess_language import guess_language


def detect_language(text):
    """Detect the language of a given text

    :param text: The text to identify the language
    :type text: str
    :return: Language code identified
    :rtype: str
    """

    language = guess_language(text)
    if language == 'UNKNOWN' or len(language) > 5:
        language = ''
    return language
