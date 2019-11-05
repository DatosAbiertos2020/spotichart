# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from spotichart.spotipy import top_charts

import unittest

class TestTopChart(unittest.TestCase):

    def test_wrong_date_format(self):
        with self.assertRaises(ValueError):
            list(top_charts.get_charts('2019-03-25', '2018-03-12', region='mx'))

    def test_not_in_charts_boundaries(self):
        with self.assertRaises(ValueError):
            list(top_charts.get_chart('2016-03-25', region='mx'))


if __name__ == '__main__':
    unittest.main()
