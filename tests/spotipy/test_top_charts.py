# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from spotichart.spotipy import top_charts

import unittest
import pandas as pd


class TestTopChart(unittest.TestCase):

    def test_not_in_charts_boundaries(self):
        with self.assertRaises(ValueError):
            list(top_charts.get_chart('2016-03-25', region='mx'))

    def test_empty_set(self):
        not_found_chart = top_charts.get_chart('2019-01-01', region='xx', chart='top200')  # Resource not found
        self.assertEqual(not_found_chart, None)

    def test_success_unique_chart(self):
        success_chart = pd.read_csv('./tests/res/regional-global-daily-2019-01-01.csv')
        retrieved_chart = top_charts.get_chart('2019-01-01', region='global', chart='top200')
        pd.testing.assert_frame_equal(success_chart, retrieved_chart)

    def test_wrong_date_format(self):
        with self.assertRaises(ValueError):
            list(top_charts.get_charts('2019-03-25', '2018-03-12', region='mx'))

    def test_empty_unique_charts(self):
        not_found_chart = top_charts.get_charts('2019-01-01', region='xx', chart='top200')  # Resource not found
        self.assertEqual(not_found_chart, None)

    def test_success_unique_charts(self):
        dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')  # noqa
        success_chart = pd.read_csv('./tests/res/regional-global-daily-2019-01-01-chart.csv',
                                    parse_dates=['Date'], date_parser=dateparse).head(50)
        retrieved_chart = top_charts.get_charts('2019-01-01', region='global', chart='top200')
        pd.testing.assert_frame_equal(success_chart, retrieved_chart)


if __name__ == '__main__':
    unittest.main()
