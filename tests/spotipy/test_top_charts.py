# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

import unittest

from topsipy.spotipy import audio_features


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertFalse(sum((1, 2, 2)) == 6, "Should be 6")


if __name__ == '__main__':
    unittest.main()
