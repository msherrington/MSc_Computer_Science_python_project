import pytest
from cities import *
from services import (
    can_be_floated,
    random_index,
    round_coordinates,
    validate_road_map
)


# We expect to see at least 5 tests for each function that needs to be tested (see above).
# Test types:
# test output matches whats expected from input
# test output type matches expected data type
# test passing nothing in creates a certain error type
# test number of elements in returned result
# test element types in returned tuple
# test different ways to break the function
# test passing the same variable in twice to a function which takes two discrete arguments
# test against hardcoded results and against dynamic results
# Test for single element lists
# Test for single element tuples
# test negative numbers
# REQUIRED FUNCTIONS X 8:
# def read_cities(file_name) - no test
# def print_cities(road_map) - no test
# def compute_total_distance(road_map)
# def swap_cities(road_map, index1, index2)
# def shift_cities(road_map):
# def find_best_cycle(road_map) - no test
# def print_map(road_map) - no test
# def main() - no test




@pytest.fixture
def road_map():
    """ Matches data in test-city-data.txt """
    return [
        ('California', 'Sacramento', 38.555605, -121.468926),
        ('Illinois', 'Springfield', 39.78325, -89.650373),
        ('Nevada', 'Carson City', 39.160949, -119.753877)
    ]


@pytest.fixture
def road_map_errors():
    """ Dictionary of common road_map error messages """
    return {
        'empty': 'The road_map list cannot be empty',
        'type': 'The road_map must be a list'
    }


def assert_for_raised_error(error_type, func, params, message):
    """
    Reusable function to assert raised errors

    :param error_type: Python Error Type
    :param func: Function being tested
    :param params: List of parameters to pass to the function
    :param message: expected String of error message
    """
    with pytest.raises(error_type) as e:
        func(*params)
    assert str(e.value) == message


def test_round_coordinates(road_map):
    coord = road_map[0][2]
    rounded = round(coord, 2)
    assert round_coordinates(coord) == rounded
    assert round_coordinates(str(coord)) == rounded
    assert round_coordinates(66) == 66.0
    assert isinstance(round_coordinates(66), float)
    assert round_coordinates(12.3456789) == pytest.approx(12.34, 0.01)
    assert_for_raised_error(ValueError, round_coordinates, ['string'], 'Cannot float coordinate')
    assert_for_raised_error(TypeError, round_coordinates, [[]], 'Coordinate must be string or number')


def test_compute_total_distance(road_map, road_map_errors):
    """ REQUIRED """
    assert compute_total_distance(road_map) == pytest.approx(31.842+30.110+1.819, 0.01)
    assert isinstance(compute_total_distance(road_map), float)
    assert compute_total_distance([('California', 'Sacramento', 38.555605, -121.468926)]) == 0.0
    assert_for_raised_error(IndexError, compute_total_distance, [[]], road_map_errors['empty'])
    assert_for_raised_error(TypeError, compute_total_distance, ['California'], road_map_errors['type'])
    assert_for_raised_error(TypeError, compute_total_distance, [['California']],
                            'Each road_map element must be a tuple')
    assert_for_raised_error(ValueError, compute_total_distance, [[('California', 38.555605, -121.468926)]],
                            'Each tuple in the road_map must contain 4 elements')
    assert_for_raised_error(TypeError, compute_total_distance, [[(38.555605, -121.468926, 'California', 'Sacramento')]],
                            'Coordinates must be of type float')


def test_euclidean_distance(road_map):
    coord_one, coord_two = road_map[0][-2:], road_map[1][-2:]
    assert isinstance(euclidean_distance(coord_one, coord_two), float)
    assert euclidean_distance(coord_one, coord_two) == pytest.approx(31.842, 0.01)
    assert euclidean_distance(coord_one, coord_one) == 0.0
    assert_for_raised_error(TypeError, euclidean_distance, [coord_one, 'string'],
                            'Coordinates must be packed in tuples or lists')
    assert_for_raised_error(ValueError, euclidean_distance, [coord_one, (38.6, 45.2, 38.4)],
                            'Exactly two elements required in location tuple')
    assert_for_raised_error(TypeError, euclidean_distance, [coord_one, (38.6, '45.2',)],
                            'Coordinates must be a number')


def test_swap_cities(road_map, road_map_errors):
    """ REQUIRED """
    index1, index2 = 0, 1
    swapped = swap_cities(road_map, index1, index2)[0]
    assert swapped[index1] == road_map[index2] and swapped[index2] == road_map[index1]
    assert isinstance(swapped, list)
    assert len(swapped) == len(road_map)
    assert isinstance(swapped[0], tuple)
    assert len(swapped[0]) == 4
    assert_for_raised_error(IndexError, swap_cities, [[], index1, index2], road_map_errors['empty'])
    assert_for_raised_error(TypeError, swap_cities, ['string', index1, index2], road_map_errors['type'])
    assert_for_raised_error(TypeError, swap_cities, [road_map, 'index1', index2], 'Index must be an integer')
    assert_for_raised_error(IndexError, swap_cities, [road_map, index1, -2],
                            'Index cannot be negative, or higher than length of road_map list')
    assert_for_raised_error(IndexError, swap_cities, [road_map, index1, len(road_map)+3],
                            'Index cannot be negative, or higher than length of road_map list')


def test_shift_cities(road_map, road_map_errors):
    """ REQUIRED """
    shifted = shift_cities(road_map)
    assert shifted == ([road_map[-1]] + road_map[:-1])
    assert shifted[0] == road_map[-1]
    assert isinstance(shifted, list)
    assert len(shifted) == len(road_map)
    assert isinstance(shifted[0], tuple)
    assert len(shifted[0]) == 4
    assert_for_raised_error(IndexError, shift_cities, [[]], road_map_errors['empty'])
    assert_for_raised_error(TypeError, shift_cities, ['string'], road_map_errors['type'])


def test_get_random_index(road_map):
    assert 0 <= get_random_index(len(road_map)-1) <= len(road_map)


def test_read_cities(road_map):
    """
    Included this test (even though it's not required) to
    check test data is being read from the file correctly
    """
    cities = read_cities('test-city-data.txt')
    assert set(cities).intersection(set(road_map))


def test_can_be_floated():
    assert can_be_floated(5)
    assert can_be_floated('5')
    assert can_be_floated(5.0)
    assert can_be_floated('5.0')
    assert not can_be_floated('text string')
    assert not can_be_floated([5])
