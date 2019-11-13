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


def test_compute_total_distance():
    assert compute_total_distance() == pytest.approx(9.386+18.496+10.646, 0.01)

    '''add your further tests'''


def test_swap_cities(road_map):
    index1 = 0
    index2 = 1
    swapped = road_map
    swapped[index1], swapped[index2] = swapped[index2], swapped[index1]
    assert swap_cities(road_map, index1, index2) == swapped


def test_shift_cities(road_map):
    assert shift_cities(road_map) == ([road_map[-1]] + road_map[:-1])


def test_read_cities(road_map):
    assert read_cities(road_map) == road_map


def test_print_cities(road_map):
    assert print_cities(road_map) == road_map


def test_find_best_cycle(road_map):
    assert find_best_cycle(road_map) == road_map


def test_print_map(road_map):
    assert print_map(road_map) == road_map


def test_main():
    assert isinstance(main(), str)
