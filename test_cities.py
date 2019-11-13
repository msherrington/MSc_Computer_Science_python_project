import pytest
from cities import *


@pytest.fixture
def file_name():
    """ Matches data in test-city-data.txt """
    return 'test-city-data.txt'


@pytest.fixture
def road_map():
    """ Matches data in test-city-data.txt """
    return [
        ('California', 'Sacramento', 38.555605, -121.468926),
        ('Illinois', 'Springfield', 39.78325, -89.650373),
        ('Nevada', 'Carson City', 39.160949, -119.753877)
    ]


def test_compute_total_distance(road_map):
    assert compute_total_distance(road_map) == pytest.approx(9.386+18.496+10.646, 0.01)


def test_swap_cities(road_map):
    index1, index2 = 0, 1
    swapped = swap_cities(road_map, index1, index2)[0]
    assert swapped[index1] == road_map[index2] and swapped[index2] == road_map[index1]


def test_shift_cities(road_map):
    assert shift_cities(road_map) == ([road_map[-1]] + road_map[:-1])


def test_read_cities(file_name, road_map):
    cities = read_cities(file_name)
    assert set(cities[0]).intersection(set(road_map[0]))


def test_print_cities(road_map):
    rounded_road_map = [tuple((state, city, round(lat, 2), round(long, 2))) for state, city, lat, long in road_map]
    assert print_cities(road_map) == rounded_road_map


def test_find_best_cycle(road_map):
    assert find_best_cycle(road_map) == road_map


def test_print_map(road_map):
    assert print_map(road_map) == road_map


def test_main(file_name):
    assert isinstance(main(file_name), str)
