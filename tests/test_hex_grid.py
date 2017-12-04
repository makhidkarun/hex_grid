'''hex_grid tests'''

import os
import sys
import unittest

sys.path.insert(
    0,
    os.path.dirname(os.path.abspath(__file__)) + '/../')

from hex_grid import Hex
import hex_grid

VERSION_INFO = '{0}.{1}'.format(
    sys.version_info[0],
    sys.version_info[1])


class TestHexCreate(unittest.TestCase):
    '''Test create methods'''
    def test_create_offset(self):
        '''Test create with offset co-ordinates'''
        hhex = Hex('2411')
        self.assertTrue(hhex.offset() == '2411')

    def test_create_cube(self):
        '''Test create with cube co-ordinates'''
        hhex = Hex((24, -23, -1))
        self.assertTrue(hhex.cube() == (24, -23, -1))

    def test_create_hex(self):
        '''Test create with Hex object'''
        hex1 = Hex('2411')
        try:
            hex2 = Hex(hex1)
            self.assertTrue(hex1.offset() == hex2.offset())
        except ValueError:
            self.fail('Unexpected error')

    def test_create_fail(self):
        '''Test create with invalid value'''
        if VERSION_INFO >= '2.7':
            for test_value in [1234, [12, 34], {}]:
                with self.assertRaises(ValueError):
                    Hex(test_value)
        else:
            for test_value in [1234, [12, 34], {}]:
                self.assertRaises(ValueError, Hex, test_value)


class TestHexConversions(unittest.TestCase):
    '''Test basic conversion methods'''
    offset = '2411'
    cube = (24, -23, -1)

    def test_offset_to_cube(self):
        '''Test offset to cube co-ordinates'''
        hhex = Hex(self.offset)
        self.assertTrue(hhex.cube() == self.cube)

    def test_cube_to_offset(self):
        '''Test cube to offset co-ordinates'''
        hhex = Hex(self.cube)
        self.assertTrue(hhex.offset() == self.offset)


class TestDistance(unittest.TestCase):
    '''Test distance between two hexes'''
    def test_distance_cube(self):
        '''Test distance between two hexes (cubic co-ords)'''
        h1 = (24, -23, -1)
        h2 = (25, -25, 0)
        self.assertTrue(hex_grid.distance(h1, h2) == 2)

    def test_distance_offset(self):
        '''Test distance between two hexes (offset co-ords)'''
        h1 = '2411'
        h2 = '2512'
        self.assertTrue(hex_grid.distance(h1, h2) == 1)


class TestHexesWithinRange(unittest.TestCase):
    '''Test hexes within range'''
    def test_hexes_within_range_cube(self):
        '''Test hexes within range (cubic co-ords)'''
        self.assertTrue(
            hex_grid.hexes_within_range(
                Hex((23, -22, -1)), 1, 'cubic') == [
                    (22, -22, 0),
                    (22, -21, -1),
                    (23, -23, 0),
                    (23, -22, -1),
                    (23, -21, -2),
                    (24, -23, -1),
                    (24, -22, -2)])

    def test_hexes_within_range_offset(self):
        '''Test hexes within range (offset co-ords)'''
        self.assertTrue(
            hex_grid.hexes_within_range(Hex('2311'), 1, 'offset') ==
            ['2210', '2211', '2310', '2311', '2312', '2410', '2411'])
