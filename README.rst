hex_grid
========

This module provides class(es) and methods for manipulating hex grids (e.g. subsector maps).

Requirements
------------

* Python 2.7
* Python 3.5
* Python 3.6

Status
------

Project code is hosted on GitHub_ as part of the Makhidkarun collection.

.. _GitHub: https://github.com/makhidkarun/hex_grid

.. image:: https://travis-ci.org/makhidkarun/hex_grid.svg?branch=master
    :target: https://travis-ci.org/makhidkarun/hex_grid



Usage
-----

hex_grid has (currently) two methods:

* distance - return distance between two hexes
* hexes_within_range - return hexes within range N of hex

Internally it uses a Hex() object, but you don't need to set up specific Hex() objects to use the methods.

>>> from hex_grid import distance, hexes_within_range
>>> distance('2244', '2141')
4
>>> hexes_within_range('2244', 1)
['2144', '2145', '2243', '2244', '2245', '2344', '2345']
