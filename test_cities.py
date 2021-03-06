import pytest
from cities import compute_total_distance, shift_cities, swap_cities
from services import (
    can_be_floated,
    euclidean_distance,
    random_index,
    round_coordinates,
    validate_road_map,
    validate_road_map_data
)


# ___ FIXTURES _____

@pytest.fixture
def road_map():
    """ Reusable test data """
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


# ___ UTILITY FUNCTIONS _____

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


# ___ TESTS FOR REQUIRED FUNCTIONS _____

def test_compute_total_distance(road_map, road_map_errors):
    assert compute_total_distance(road_map) == pytest.approx(31.842+30.110+1.819, 0.01)
    assert isinstance(compute_total_distance(road_map), float)
    assert compute_total_distance([('California', 'Sacramento', 38.555605, -121.468926)]) == 0.0
    assert_for_raised_error(IndexError, compute_total_distance, [[]], road_map_errors['empty'])
    assert_for_raised_error(TypeError, compute_total_distance, ['California'], road_map_errors['type'])
    assert_for_raised_error(TypeError, compute_total_distance, [['California']],
                            'Each road_map element must be a tuple')
    assert_for_raised_error(ValueError, compute_total_distance, [[('California', 38.555605, -121.468926)]],
                            'Each tuple in the road_map must contain 4 elements')
    assert_for_raised_error(TypeError, compute_total_distance, [[('California', 'Sacramento', 'string', 'string')]],
                            'Coordinates must be of type float')
    assert_for_raised_error(TypeError, compute_total_distance, [[(38.555605, -121.468926, 38.555605, -121.468926)]],
                            'City and State must be strings')


def test_swap_cities(road_map, road_map_errors):
    index1, index2 = 0, 1
    swapped = swap_cities(road_map, index1, index2)[0]
    assert swapped[index1] == road_map[index2] and swapped[index2] == road_map[index1]
    assert isinstance(swapped, list)
    assert len(swapped) == len(road_map)
    assert isinstance(swapped[0], tuple)
    assert len(swapped[0]) == 4
    swap_same_index = swap_cities(road_map, 0, 0)[0]
    assert swap_same_index == road_map
    assert len(swap_same_index) == len(road_map)
    assert_for_raised_error(TypeError, swap_cities, ['string', index1, index2], road_map_errors['type'])
    assert_for_raised_error(TypeError, swap_cities, [index2, index1, index2], road_map_errors['type'])
    assert_for_raised_error(IndexError, swap_cities, [[], index1, index2], road_map_errors['empty'])
    assert_for_raised_error(TypeError, swap_cities, [road_map, 'string', index2], 'Index must be an integer')
    assert_for_raised_error(IndexError, swap_cities, [road_map, index1, -2],
                            'Index cannot be negative, or higher than length of road_map list')
    assert_for_raised_error(IndexError, swap_cities, [road_map, index1, len(road_map)+3],
                            'Index cannot be negative, or higher than length of road_map list')


def test_shift_cities(road_map, road_map_errors):
    shifted = shift_cities(road_map)
    assert shifted == ([road_map[-1]] + road_map[:-1])
    assert shifted[0] == road_map[-1]
    assert isinstance(shifted, list)
    assert len(shifted) == len(road_map)
    assert isinstance(shifted[0], tuple)
    assert len(shifted[0]) == 4
    assert_for_raised_error(TypeError, shift_cities, ['string'], road_map_errors['type'])
    assert_for_raised_error(TypeError, shift_cities, [0], road_map_errors['type'])
    assert_for_raised_error(IndexError, shift_cities, [[]], road_map_errors['empty'])


# ___ TESTS FOR ADDITIONAL FUNCTIONS _____

def test_can_be_floated():
    assert can_be_floated(5)
    assert can_be_floated('5')
    assert can_be_floated(5.0)
    assert can_be_floated('5.0')
    assert not can_be_floated('text string')
    assert not can_be_floated([5])


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


def test_random_index(road_map):
    maximum = len(road_map)-1
    random = random_index(maximum)
    assert random <= len(road_map)
    assert 0 <= random
    assert isinstance(random, int)
    assert_for_raised_error(TypeError, random_index, [23.0], 'Maximum must be an integer')
    assert_for_raised_error(TypeError, random_index, ['string'], 'Maximum must be an integer')
    assert_for_raised_error(ValueError, random_index, [-2], 'Maximum must be a positive integer')


def test_validate_road_map(road_map, road_map_errors):
    validated = validate_road_map(road_map)
    assert isinstance(validated[0], tuple)
    assert len(validated[0]) == 4
    assert isinstance(validated, list)
    assert len(validated) == len(road_map)
    assert_for_raised_error(TypeError, validate_road_map, ['string'], road_map_errors['type'])
    assert_for_raised_error(TypeError, validate_road_map, [0], road_map_errors['type'])
    assert_for_raised_error(IndexError, validate_road_map, [[]], road_map_errors['empty'])


def test_validate_road_map_data(road_map):
    validated_data = validate_road_map_data(road_map)
    assert isinstance(validated_data[0], tuple)
    assert len(validated_data[0]) == 4
    assert isinstance(validated_data, list)
    assert len(validated_data) == len(road_map)
    assert_for_raised_error(TypeError, validate_road_map_data, [['string']], 'Each road_map element must be a tuple')
    assert_for_raised_error(ValueError, validate_road_map_data, [[(1, 2, 3)]],
                            'Each tuple in the road_map must contain 4 elements')
    assert_for_raised_error(TypeError, validate_road_map_data, [[(1, 2, 3, 4)]], 'City and State must be strings')
    assert_for_raised_error(TypeError, validate_road_map_data, [[('1', '2', '3', '4')]],
                            'Coordinates must be of type float')
