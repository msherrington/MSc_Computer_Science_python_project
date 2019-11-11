import pytest
from cities import *


@pytest.fixture
def road_map():
    return [
        ("Kentucky", "Frankfort", 38.197274, -84.86311),
        ("Delaware", "Dover", 39.161921, -75.526755),
        ("Minnesota", "Saint Paul", 44.95, -93.094)
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
