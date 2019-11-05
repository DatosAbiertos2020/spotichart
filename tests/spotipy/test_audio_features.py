# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from spotichart.spotipy import audio_features

import os
import unittest
import json

# Import spotify access token from environment variable
access_token = os.environ.get("SPOTIFY_ACCESS_TOKEN", None)
assert access_token is not None, "Must declare environment variable: SPOTIFY_ACCESS_TOKEN"

# Import expired access token from environment variable
expired_token = os.environ.get("SPOTIFY_EXPIRED_TOKEN", None)
assert expired_token is not None, "Must declare environment variable: SPOTIFY_EXPIRED_TOKEN"

class TestAudioFeatures(unittest.TestCase):
    def test_successfull_query(self):
        with open('./tests/res/example.json') as file:
            example = json.load(file)
        self.assertDictEqual(example, audio_features.get_audio_features(access_token, '1PKNKessUE10zYclDWNRfE'))

    def test_not_found(self):
        with self.assertRaises(ValueError):
            list(audio_features.get_audio_features(access_token, '1PKNKessUE10zYclDWNRfH'))

    def test_no_access_token(self):
        with self.assertRaises(ValueError):
            list(audio_features.get_audio_features('', '1PKNKessUE10zYclDWNRfE'))

    def test_expired_access_token(self):
        with self.assertRaises(ValueError):
            list(audio_features.get_audio_features(expired_token, '1PKNKessUE10zYclDWNRfE'))

if __name__ == '__main__':
    unittest.main()
