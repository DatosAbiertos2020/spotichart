topsipy package
===============

Subpackages
-----------

.. toctree::

   topsipy.language
   topsipy.lyrics
   topsipy.spotipy

Module contents
---------------

.. automodule:: topsipy
   :members:
   :undoc-members:
   :show-inheritance:

Domain Model
------------


.. image:: /_static/res/domain_model.png
   :target: /_static/res/domain_model.png
   :alt: Domain Model


Attributes involved in the scope of this package. Provided from `Spotify Top Charts <https://spotifycharts.com/>`_\ , `Spotify Web API <https://developer.spotify.com/documentation/web-api/reference/tracks/>`_\ , `Genius API <https://docs.genius.com/>`_\ , and Genius itself (by web scraping the lyrics).

Model View
----------

Therefore, the providers and the inner modules would look this way, using the ``Model View with Use Style``.


.. image:: /_static/res/modules_view_uses_style.png
   :target: /_static/res/modules_view_uses_style.png
   :alt: Model View


Additionaly, the ``guess-language-spirit`` `package <https://pypi.org/project/guess_language-spirit/>`_ is used to detect the lyrics language. The ``language package`` and its dependency are structured that way, so is easier to switch the language-detecting provider.