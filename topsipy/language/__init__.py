# -*- coding: utf-8 -*-

"""language detector package."""

from __future__ import unicode_literals

from guess_language import guess_language

def detect_language(text):
    language = guess_language(text)
    if language == 'UNKNOWN' or len(language) > 5:
        language = ''
    return language