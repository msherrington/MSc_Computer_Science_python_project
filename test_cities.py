import pytest
from cities import *


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
def file_name():
    return 'test-city-data.txt'


@pytest.fixture
def road_map():
    """ Matches data in test-city-data.txt """
    return [
        ('California', 'Sacramento', 38.555605, -121.468926),
        ('Illinois', 'Springfield', 39.78325, -89.650373),
        ('Nevada', 'Carson City', 39.160949, -119.753877)
    ]


def check_for_raised_error(error_type, func, param, message):
    with pytest.raises(error_type) as e:
        func(param)
    assert str(e.value) == message


def test_round_coordinates(road_map):
    coord = road_map[0][2]
    city, state, coord_type = 'NY', 'NY', 'latitude'
    assert round_coordinates(12.3456789, city, state, coord_type) == pytest.approx(12.34, 0.01)
    assert round_coordinates(coord, city, state, coord_type) == round(coord, 2)
    assert round_coordinates(str(coord), city, state, coord_type) == round(coord, 2)
    assert round_coordinates(66, city, state, coord_type) == 66.0
    assert round_coordinates('text_string', city, state, coord_type) is None
    assert round_coordinates('abc4567', city, state, coord_type) is None


def test_compute_total_distance(road_map):
    """ REQUIRED """
    assert compute_total_distance(road_map) == pytest.approx(31.842+30.110+1.819, 0.01)
    assert isinstance(compute_total_distance(road_map), float)
    assert compute_total_distance([('California', 'Sacramento', 38.555605, -121.468926)]) == 0.0
    check_for_raised_error(IndexError, compute_total_distance, [], 'The road_map list cannot be empty')
    check_for_raised_error(TypeError, compute_total_distance, 'California', 'The road_map must be a list')
    check_for_raised_error(TypeError, compute_total_distance, ['California'], 'Each road_map element must be a tuple')
    check_for_raised_error(
        ValueError,
        compute_total_distance,
        [('California', 'Sacramento')],
        'Each tuple in the road_map must contain 4 elements'
    )
    check_for_raised_error(
        TypeError,
        compute_total_distance,
        [(38.555605, -121.468926, 'California', 'Sacramento')],
        'Coordinates must be of type float'
    )


def test_euclidean_distance(road_map):
    city1, city2 = road_map[0], road_map[1]
    assert euclidean_distance(city1[-2:], city2[-2:]) == pytest.approx(31.842, 0.01)


def test_swap_cities(road_map):
    index1, index2 = 0, 1
    swapped = swap_cities(road_map, index1, index2)[0]
    assert swapped[index1] == road_map[index2] and swapped[index2] == road_map[index1]


def test_shift_cities(road_map):
    assert shift_cities(road_map) == ([road_map[-1]] + road_map[:-1])


def test_get_random_index(road_map):
    assert 0 <= get_random_index(len(road_map)-1) <= len(road_map)


def test_read_cities(file_name, road_map):
    """
    Included this test (even though it's not required) to
    check test data is being read from the file correctly
    """
    cities = read_cities(file_name)
    assert set(cities).intersection(set(road_map))


def test_can_be_floated():
    assert can_be_floated(5)
    assert can_be_floated('5')
    assert can_be_floated(5.0)
    assert can_be_floated('5.0')
    assert not can_be_floated('text string')
    assert not can_be_floated([5])
