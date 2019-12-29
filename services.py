import random

from math import sqrt


def can_be_floated(value):
    """
    Check if a datatype can be floated without errors
    :param value: any datatype
    :return: Boolean
    """

    if not isinstance(value, (str, int, float)):
        return False
    try:
        float(value)
        return True
    except ValueError:
        return False


def euclidean_distance(location1, location2):
    """
    Calculate the Euclidean distance between 2 cities
    Accept lat/lon coordinates of (x1,y1) and (x2,y2)
    Return formula sqrt((x1-x2)**2 + (y1-y2)**2)
    :param location1: Tuple containing 2 Float elements
    :param location2: Tuple containing 2 Float elements
    :return: Float
    """

    locations = [location1, location2]
    if not all(isinstance(x, (tuple, list)) for x in locations):
        raise TypeError('Coordinates must be packed in tuples or lists')
    if not all(len(x) == 2 for x in locations):
        raise ValueError('Exactly two elements required in location tuple')
    lat1, lon1 = location1
    lat2, lon2 = location2
    if not all(isinstance(x, (float, int)) for x in [lat1, lon1, lat2, lon2]):
        raise TypeError('Coordinates must be a number')
    return sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)


def random_index(maximum):
    """
    Return random integers in the range 0 to maximum
    :param maximum: integer
    :return integer
    """

    if not isinstance(maximum, int):
        raise TypeError('Maximum must be an integer')
    if maximum < 0:
        raise ValueError('Maximum must be a positive integer')
    return random.randint(0, maximum)


def round_coordinates(coord):
    """
    Takes a latitude or longitude
    Return a float rounded to 2 decimal places
    :param coord: Number or String
    :return: Float (rounded to 2 decimal places)
    """

    if not isinstance(coord, (str, int, float)):
        raise TypeError('Coordinate must be string or number')
    if not can_be_floated(coord):
        raise ValueError('Cannot float coordinate')
    return round(float(coord), 2)


def validate_road_map(road_map):
    """
    Check road_map is a list with at least one element
    Raise errors otherwise

    :param road_map: List of Quadruples
    :return: road_map: List of Quadruples
    """

    if not isinstance(road_map, list):
        raise TypeError('The road_map must be a list')
    if len(road_map) == 0:
        raise IndexError('The road_map list cannot be empty')
    return road_map


def validate_road_map_data(road_map):
    """
    Check elements of road_map are tuples of four elements
    Check the last two elements of each tuple are floats
    Raise errors otherwise

    :param road_map: List of Quadruples
    :return: road_map: List of Quadruples
    """

    if not all(isinstance(city, tuple) for city in road_map):
        raise TypeError('Each road_map element must be a tuple')
    if not all(len(city) == 4 for city in road_map):
        raise ValueError('Each tuple in the road_map must contain 4 elements')
    for state, city, lat, lon in road_map:
        if not all(isinstance(coord, str) for coord in [state, city]):
            raise TypeError('City and State must be strings')
        if not all(isinstance(coord, float) for coord in [lat, lon]):
            raise TypeError('Coordinates must be of type float')
    return road_map
