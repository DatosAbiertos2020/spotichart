.. Spotichart documentation master file, created by
   sphinx-quickstart on Mon Oct  7 11:46:42 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Spotichart's documentation!
======================================

Contents:

.. toctree::
   :maxdepth: 3

   spotichart


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`



Spotichart
==========


.. image:: https://github.com/Manolomon/spotichart/workflows/Spotichart/badge.svg
   :target: https://github.com/Manolomon/spotichart/workflows/Spotichart/badge.svg
   :alt: Badge
 
.. image:: https://readthedocs.org/projects/spotichart/badge/?version=latest
   :target: https://spotichart.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
 
.. image:: https://api.codacy.com/project/badge/Grade/28b8089c9d9a4ea6ab4acb9c7407d54c
   :target: https://www.codacy.com/manual/Manolomon/spotichart?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Manolomon/spotichart&amp;utm_campaign=Badge_Grade
   :alt: Codacy Badge


Collector Module for Spotify National Trending Analysis

Introduction
------------

The Spotichart module makes it easy for data scientist and programmers get the features from the trending songs on Spotify. You can define period of time and a region and get the main characteristics of the top songs.

Documentation
-------------

The oficial documentations is available on: `Read The Docs <https://spotichart.readthedocs.io/en/latest/>`_

Installation
------------

TODO: Not Yet Published

.. code-block:: bash

   $ pip install spotichart

Requirements
------------


* **Python** >= 3.6
* **Spotify Web API Access Token**\ , you can request yours `here <https://developer.spotify.com/console/get-audio-features-track/>`_ and click on ``GET TOKEN``. Then copy the token on the ``OAuth Token`` field.
* (Optional) **Genius Web API Access Token**. From `the official docs page <https://docs.genius.com/#/search-h2>`_ you can just select ``Authenticate wih the Docs App To Try``\ , and copy the ``Authorization Bearer`` provided after logging in.

Synopsis
--------

Usage
^^^^^

Just to get the audio features, given a date (or period) and a region

.. code-block:: python

   import spotichart

   spotify_token = 'YOUR-ACCESS-TOKEN-FROM-THE-WEB-API'

   chart = spotichart.generate_top_chart(spotify_token, start='2019-01-01', end='2019-10-13', region='mx')

To additionally retrieve each song's lyrics, Genius ID an auto-detect the language, you can do as well:

.. code-block:: python

   import spotichart

   spotify_token = 'YOUR-SPOTIFY-ACCESS-TOKEN-FROM-THE-WEB-API'
   genius_token = 'YOUR-GENIUS-ACCESS-TOKEN-FROM-THE-WEB-API'

   chart = spotichart.generate_top_chart(spotify_token, start='2019-01-01',
                                      end='2019-10-13', region='mx', sleep=0.5)

   chart_with_lyrics = spotichart.get_lyrics_from_chart(genius_token, chart, sleep=0.1)

**Note:** Since these functions imply web requests to get the data, the ``sleep`` parameter is meant to make the algorithm rest and avoid the server to refuse the requests. By default ``sleep`` is set to 1 second.

The DataFrame
^^^^^^^^^^^^^

A ``pandas.DataFrame`` will be generated with the data of interest:

.. code-block:: python

   >>> chart
          Position                                      Track Name           Artist  Streams  ... speechiness    tempo time_signature  valence
   0             1                                   Calma - Remix       Pedro Capó   737894  ...      0.0524  126.899              4    0.761
   1             2                                      Adan y Eva     Paulo Londra   415066  ...      0.3360  171.993              4    0.720
   2             3  Taki Taki (with Selena Gomez, Ozuna & Cardi B)         DJ Snake   409061  ...      0.2290   95.948              4    0.591
   3             4                               MIA (feat. Drake)        Bad Bunny   377855  ...      0.0621   97.062              4    0.158
   4             5                               A Través Del Vaso    Grupo Arranke   346975  ...      0.0297  143.851              3    0.920
   ...         ...                                             ...              ...      ...  ...         ...      ...            ...      ...
   14295        46                                       Con Calma     Daddy Yankee   141397  ...      0.0593   93.989              4    0.656
   14296        47                          La Escuela No Me Gustó    Adriel Favela   139350  ...      0.0371  112.548              4    0.844
   14297        48                          De Los Besos Que Te Di  Christian Nodal   139294  ...      0.0422  195.593              4    0.709
   14298        49                                   Pa Mí - Remix            Dalex   137812  ...      0.2200  170.018              4    0.727
   14299        50                                         Circles      Post Malone   131109  ...      0.0395  120.042              4    0.5

   [14300 rows x 20 columns]
