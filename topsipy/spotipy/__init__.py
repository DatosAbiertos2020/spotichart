# -*- coding: utf-8 -*-

"""spotipy package."""

from __future__ import unicode_literals

from .__about__ import (
    __version__
)

from .top_charts import (
    get_charts
)

import tqdm
import pandas as pd
import requests

def generate_top_chart(start, end=None, region='en', freq='daily', chart='top200', sleep=1):
    chart = get_charts(start, end, region, freq, chart, sleep)
    chart['Track Id'] = chart['URL'].str.split("/",expand=True)[4]
    return chart