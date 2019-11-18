import pytest
from cities import *


@pytest.fixture
def file_name():
    return 'test-city-data.txt'


@pytest.fixture
def road_map():
    """ Matches data in test-city-data.txt """
    return [
        ('California', 'Sacramento', '38.555605', '-121.468926'),
        ('Illinois', 'Springfield', '39.78325', '-89.650373'),
        ('Nevada', 'Carson City', '39.160949', '-119.753877')
    ]


def test_compute_total_distance(road_map):
    assert compute_total_distance(road_map) == pytest.approx(31.842+30.110+1.819, 0.01)


def test_euclidean_distance(road_map):
    city1, city2 = road_map[0], road_map[1]
    assert euclidean_distance(city1[-2:], city2[-2:]) == pytest.approx(31.842, 0.01)


def test_swap_cities(road_map):
    index1, index2 = 0, 1
    swapped = swap_cities(road_map, index1, index2)[0]
    assert swapped[index1] == road_map[index2] and swapped[index2] == road_map[index1]


def test_shift_cities(road_map):
    assert shift_cities(road_map) == ([road_map[-1]] + road_map[:-1])


def test_read_cities(file_name, road_map):
    """
    Included this test (even though it's not required) to
    check test data is being read from the file correctly
    """
    cities = read_cities(file_name)
    assert set(cities[0]).intersection(set(road_map[0]))
