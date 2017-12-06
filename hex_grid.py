'''hex_grid.py'''

import re


class Hex(object):
    '''
    Hex object. Specify as one of:
    - Hex(ColRow) where ColRow is string in range '0000'-'9999'
    - Hex((x, y, z)) where (x, y, z) is tuple and x, y, z are integers
    '''

    def __init__(self, value="0000"):
        self.row = 0
        self.col = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.__directions = [
            ((0, 1, -1)), ((-1, 1, 0)), ((-1, 0, 1)),
            ((0, -1, 1)), ((1, -1, 0)), ((1, 0, -1))]

        # Check input
        if isinstance(value, Hex):
            self.row = value.row
            self.col = value.col
            self.x = value.x
            self.y = value.y
            self.z = value.z
        elif isinstance(value, str):
            if re.match('^[0-9][0-9][0-9][0-9]$', value):
                self.col = int(value[:2])
                self.row = int(value[2:])
                self.offset_to_cube()
            else:
                raise ValueError(
                    '%s must be in range 0000-9999 (or use tuple (x, y, z)',
                    value)
        elif isinstance(value, tuple):
            ok = False
            if len(value) == 3:
                ok = True
                for i in value:
                    if not isinstance(i, int):
                        ok = False
            if ok is True:
                self.x = value[0]
                self.y = value[1]
                self.z = value[2]
                assert (self.x + self.y + self.z == 0), 'Invalid co-ordinates'
                self.cube_to_offset()
            else:
                raise ValueError(
                    'input must be tuple (x, y, z) where x, y, z are integer ',
                    '(or use offset 0000-9999')
        else:
            raise ValueError(
                'input must be either string 0000-9999 ',
                'or tuple (x, y, z) where x, y, z are integer')

    def __repr__(self):
        return('{:02d}{:02d} / ({}, {}, {})'.format(
            self.col, self.row,
            self.x, self.y, self.z))

    def cube(self):
        '''Cubic co-ordinates'''
        return (self.x, self.y, self.z)

    def offset(self):
        '''Offset co-ordinates'''
        return('{:02d}{:02d}'.format(self.col, self.row))

    def offset_to_cube(self):
        '''Generate cubic co-ords from offset co-ords'''
        self.x = self.col
        self.z = int(self.row - (self.col + (self.col & 1)) / 2)
        self.y = -self.x - self.z
        assert (self.x + self.y + self.z == 0), 'Invalid co-ordinates'

    def cube_to_offset(self):
        '''Generate offset co-ords from cubic co-ords'''
        self.col = self.x
        self.row = int(self.z + (self.x + (self.x & 1)) / 2)

    def neighbour(self, direction):
        '''
        Generate neighbour hex in direction d
        Directions:
           0
        1     5
           C
        2     4
           3
        '''
        assert (isinstance(direction, int)), 'Direction must be integer'
        assert (direction in range(0, 6)), \
            'Invalid direction {}'.format(direction)
        return Hex((
            self.x + self.__directions[direction][0],
            self.y + self.__directions[direction][1],
            self.z + self.__directions[direction][2]))

    def __eq__(self, other):
        assert (isinstance(other, Hex)), 'Can only add Hex to Hex'
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        assert (isinstance(other, Hex)), 'Can only add Hex to Hex'
        return self.x != other.x or self.y != other.y or self.z != other.z

    def __add__(self, other):
        '''Add hex to hex (vector add)'''
        assert (isinstance(other, Hex)), 'Can only add Hex to Hex'
        return Hex((self.x + other.x, self.y + other.y, self.z + other.z))

    def __sub__(self, other):
        '''Subtract hex from hex (vector subtract)'''
        assert (isinstance(other, Hex)), 'Can only subtract Hex from Hex'
        return Hex((self.x - other.x, self.y - other.y, self.z - other.z))

    def __mul__(self, mult):
        '''Multiply hex vector by int'''
        assert (isinstance(mult, int)), 'Can only multiply by integer'
        return Hex((self.x * mult, self.y * mult, self.z * mult))


def distance(h1, h2):
    '''Calculate distance between hex h1 and hex h2'''
    hex1 = Hex(h1)
    hex2 = Hex(h2)

    return max(
        abs(hex1.x - hex2.x),
        abs(hex1.y - hex2.y),
        abs(hex1.z - hex2.z))


def hexes_within_range(hhex, dist, fmt='offset'):
    '''
    Return a list of hexes within range dist of hhex
    - hhex = offset or cubic co-ords or Hex object
    - dist = int distance
    - fmt = 'offset' or 'cubic' - specifies output format
    '''
    if fmt not in ['offset', 'cubic']:
        raise ValueError('format must be "offset" or "cubic"')
    hexes = []
    h_centre = Hex(hhex)
    for dx in range(-dist, dist + 1):
        for dy in range(-dist, dist + 1):
            for dz in range(-dist, dist + 1):
                if dx + dy + dz == 0:
                    found_hex = Hex(
                        (h_centre.x + dx, h_centre.y + dy, h_centre.z + dz))
                    if fmt == 'offset':
                        hexes.append(found_hex.offset())
                    else:
                        hexes.append(found_hex.cube())
    return sorted(hexes)


def hexes_at_range(hhex, dist, fmt="offset"):
    '''
    Return a list of hexes at range dist of hhex
    - hhex = offset or cubic co-ords or Hex object
    - dist = int distance
    - fmt = 'offset' or 'cubic' - specifies output format
    '''
    if fmt not in ['offset', 'cubic']:
        raise ValueError('format must be "offset" or "cubic"')
    hexes = []
    h_centre = Hex(hhex)

    h_next = h_centre.neighbour(4) * dist
    for direction in range(0, 6):
        for j in range(0, dist):
            if fmt == 'offset':
                hexes.append(h_next.offset())
            else:
                hexes.append(h_next.cube())
            h_next = h_next.neighbour(direction)
    return sorted(hexes)
