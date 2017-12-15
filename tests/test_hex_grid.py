'''hex_grid tests'''

import os
import sys
import unittest
import logging

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

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

    def test_hex_create_offset(self):
        '''Test create with offset co-ordinates'''
        hhex = Hex('2411')
        self.assertTrue(hhex.offset() == '2411')

    def test_hex_create_cube(self):
        '''Test create with cube co-ordinates'''
        hhex = Hex((24, -23, -1))
        self.assertTrue(hhex.cube() == (24, -23, -1))

    def test_hex_create_hex(self):
        '''Test create with Hex object'''
        hex1 = Hex('2411')
        try:
            hex2 = Hex(hex1)
            self.assertTrue(hex1.offset() == hex2.offset())
        except ValueError:
            self.fail('Unexpected error')

    def test_hex_create_cube_bad_coords(self):
        '''Test create with invalid cube co-ordinates (x+y+z != 0)'''
        test_value = (1, 1, 1)
        if VERSION_INFO >= '2.7':
            with self.assertRaises(AssertionError):
                Hex(test_value)
        else:
            self.assertRaises(AssertionError, Hex, test_value)

    def test_hex_create_fail(self):
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

    def test_hex_offset_to_cube(self):
        '''Test offset to cube co-ordinates'''
        hhex = Hex(self.offset)
        self.assertTrue(hhex.cube() == self.cube)

    def test_hex_cube_to_offset(self):
        '''Test cube to offset co-ordinates'''
        hhex = Hex(self.cube)
        self.assertTrue(hhex.offset() == self.offset)


class TestHexArithmetic(unittest.TestCase):
    '''Test addition'''

    def test_hex_addition_valid(self):
        '''Test addition Hex to Hex'''
        hex1 = Hex('0101')
        hex2 = Hex((0, 1, -1))
        self.assertTrue(hex1 + hex2 == Hex('0100'))

    def test_hex_addition_invalid_arg(self):
        '''Test addition Hex to not-Hex'''
        if VERSION_INFO >= '2.7':
            with self.assertRaises(AssertionError):
                Hex('1010') + 1
        else:
            self.assertRaises(AssertionError, lambda: Hex('1010') + 1)

    def test_hex_subtraction_valid(self):
        '''Test subtraction Hex from Hex'''
        hex1 = Hex('0101')
        hex2 = Hex((0, 1, -1))
        self.assertTrue(hex1 - hex2 == Hex('0102'))

    def test_hex_subtract_invalid_arg(self):
        '''Test subtraction Hex from not-Hex'''
        if VERSION_INFO >= '2.7':
            with self.assertRaises(AssertionError):
                Hex('1010') - 1
        else:
            self.assertRaises(AssertionError, lambda: Hex('1010') - 1)

    def test_hex_multiply(self):
        '''Test Hex multiplication'''
        self.assertTrue(Hex('0001') * 3 == Hex('0003'))

    def test_hex_multiply_invalid_args(self):
        '''Test Hex multiplication (invalid args)'''
        if VERSION_INFO >= '2.7':
            for mult in [1.5, Hex('0001')]:
                with self.assertRaises(AssertionError):
                    Hex('1010') * mult
        else:
            for mult in [1.5, Hex('0001')]:
                self.assertRaises(AssertionError, lambda: Hex('0001') * mult)


class TestHexComparison(unittest.TestCase):
    '''Test equality, inequality, lt, le, gt, ge'''

    def test_hex_eq_success(self):
        '''Test Hex equality (success)'''
        hex1 = Hex('0101')
        hex2 = Hex('0101')
        self.assertTrue(hex1 == hex2)

    def test_hex_eq_fail(self):
        '''Test Hex equality (failure)'''
        hex1 = Hex('0101')
        hex2 = Hex('0102')
        self.assertFalse(hex1 == hex2)

    def test_hex_ne_success(self):
        '''Test Hex inequality (success)'''
        hex1 = Hex('0101')
        hex2 = Hex('0102')
        self.assertTrue(hex1 != hex2)

    def test_hex_ne_fail(self):
        '''Test Hex inequality (failure)'''
        hex1 = Hex('0101')
        hex2 = Hex('0101')
        self.assertFalse(hex1 != hex2)

    def test_hex_lt_success(self):
        '''Test Hex less than (success)'''
        hex1 = Hex('0101')
        hex2 = Hex('0102')
        self.assertTrue(hex1 < hex2)

    def test_hex_lt_fail(self):
        '''Test Hex less than (fail)'''
        hex1 = Hex('0101')
        hex2 = Hex('0102')
        self.assertFalse(hex2 < hex1)

    def test_hex_le_success(self):
        '''Test Hex less than/equal (success)'''
        hex1 = Hex('0101')
        hex2 = Hex('0102')
        self.assertTrue(hex1 <= hex2)

    def test_hex_le_fail(self):
        '''Test Hex less than (fail)'''
        hex1 = Hex('0101')
        hex2 = Hex('0102')
        self.assertFalse(hex2 <= hex1)

    def test_hex_gt_success(self):
        '''Test Hex greater than (success)'''
        hex1 = Hex('0101')
        hex2 = Hex('0102')
        self.assertTrue(hex2 > hex1)

    def test_hex_gt_fail(self):
        '''Test Hex greater than (fail)'''
        hex1 = Hex('0101')
        hex2 = Hex('0102')
        self.assertFalse(hex1 > hex2)

    def test_hex_ge_success(self):
        '''Test Hex greater than/equal (success)'''
        hex1 = Hex('0101')
        hex2 = Hex('0102')
        self.assertTrue(hex2 >= hex1)

    def test_hex_ge_fail(self):
        '''Test Hex greater than/equal (fail)'''
        hex1 = Hex('0101')
        hex2 = Hex('0102')
        self.assertFalse(hex1 >= hex2)

    def test_hex_eq_invalid_args(self):
        '''Test equality failure Hex == not-Hex'''
        if VERSION_INFO >= '2.7':
            with self.assertRaises(AssertionError):
                Hex('1010') == 4
        else:
            self.assertRaises(AssertionError, lambda: Hex('1010') == 4)

    def test_hex_ne_invalid_args(self):
        '''Test equality failure Hex == not-Hex'''
        if VERSION_INFO >= '2.7':
            with self.assertRaises(AssertionError):
                Hex('1010') != 4
        else:
            self.assertRaises(AssertionError, lambda: Hex('1010') != 4)

    def test_hex_lt_invalid_args(self):
        '''Test lt failure Hex == not-Hex'''
        if VERSION_INFO >= '2.7':
            with self.assertRaises(AssertionError):
                Hex('1010') < 4
        else:
            self.assertRaises(AssertionError, lambda: Hex('1010') < 4)

    def test_hex_le_invalid_args(self):
        '''Test lt failure Hex == not-Hex'''
        if VERSION_INFO >= '2.7':
            with self.assertRaises(AssertionError):
                Hex('1010') <= 4
        else:
            self.assertRaises(AssertionError, lambda: Hex('1010') <= 4)

    def test_hex_gt_invalid_args(self):
        '''Test lt failure Hex == not-Hex'''
        if VERSION_INFO >= '2.7':
            with self.assertRaises(AssertionError):
                Hex('1010') < 4
        else:
            self.assertRaises(AssertionError, lambda: Hex('1010') > 4)

    def test_hex_ge_invalid_args(self):
        '''Test lt failure Hex == not-Hex'''
        if VERSION_INFO >= '2.7':
            with self.assertRaises(AssertionError):
                Hex('1010') <= 4
        else:
            self.assertRaises(AssertionError, lambda: Hex('1010') >= 4)


class TestHexNeighbours(unittest.TestCase):
    '''Test neigbour'''

    def test_hex_neighbour(self):
        '''Test hex neighbours (direction 0..5)'''
        hcen = Hex('0202')
        neighbours = [
            Hex('0201'), Hex('0102'), Hex('0103'),
            Hex('0203'), Hex('0303'), Hex('0302')]
        for direction, hhex in enumerate(neighbours):
            self.assertTrue(hcen.neighbour(direction) == hhex)

    def test_hex_neighbours(self):
        '''Test hex neighbours method'''
        hcen = Hex('0202')
        neighbours = [
            Hex('0201'), Hex('0102'), Hex('0103'),
            Hex('0203'), Hex('0303'), Hex('0302')]
        self.assertTrue(hcen.neighbours() == sorted(neighbours))

    def test_hex_neighbours_offset(self):
        '''Test hex neighbours method (offset format)'''
        hcen = Hex('0303')
        neighbours = ['0202', '0203', '0302', '0304', '0402', '0403']
        self.assertTrue(hcen.neighbours_offset() == sorted(neighbours))

    def test_hex_neighbours_cube(self):
        '''Test hex neighbours method (offset format)'''
        hcen = Hex('0303')
        neighbours = [
            (2, -4, 2), (2, -3, 1), (3, -5, 2),
            (3, -3, 0), (4, -5, 1), (4, -4, 0)]
        self.assertTrue(hcen.neighbours_cube() == sorted(neighbours))

    def test_hex_neighbour_invalid_dir(self):
        '''Test hex neighbour (invalid direction)'''
        hcen = Hex('0201')
        if VERSION_INFO >= '2.7':
            for test_value in [1234, [12, 34], {}]:
                with self.assertRaises(AssertionError):
                    hcen.neighbour(test_value)
        else:
            for test_value in [1234, [12, 34], {}]:
                self.assertRaises(ValueError, hcen.neighbour, test_value)


class TestDistance(unittest.TestCase):
    '''Test distance between two hexes'''

    def test_distance_cube(self):
        '''Test distance between two hexes (cubic co-ords)'''
        hex1 = (24, -23, -1)
        hex2 = (25, -25, 0)
        self.assertTrue(hex_grid.distance(hex1, hex2) == 2)

    def test_distance_offset(self):
        '''Test distance between two hexes (offset co-ords)'''
        hex1 = '2411'
        hex2 = '2512'
        self.assertTrue(hex_grid.distance(hex1, hex2) == 1)


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


class TestHexesAtRange(unittest.TestCase):
    '''Test hexes at range'''

    def test_hexes_at_range_offset(self):
        '''Test hexes at range (offset co-ords)'''
        self.assertTrue(
            hex_grid.hexes_at_range('0202', 1, 'offset') ==
            ['0102', '0103', '0201', '0203', '0302', '0303'])
        LOGGER.debug(
            'hexes_at_range("%s", 2) = %s',
            '0708',
            hex_grid.hexes_at_range('0708', 2, 'offset'))
        self.assertTrue(
            hex_grid.hexes_at_range('0708', 2, 'offset') == [
                '0507', '0508', '0509', '0606', '0609', '0706',
                '0710', '0806', '0809', '0907', '0908', '0909'])
