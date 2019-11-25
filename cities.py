from math import sqrt
import random


# CHECKLIST
# You must implement all the required functions and the implementation must handle all the permitted inputs correctly.
# You must provide good code coverage to catch any errors before we do.
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

# Style...
# Use proper indentation and spacing, (check PEP8)
# Don't repeat code if you can put it in a function and just call the function.
# Try to avoid redundancy (such as the beginner's if better == True).

# REQUIRED FUNCTIONS X 8:
# def read_cities(file_name) - no test
# def print_cities(road_map) - no test
# def compute_total_distance(road_map)
# def swap_cities(road_map, index1, index2)
# def shift_cities(road_map):
# def find_best_cycle(road_map) - no test
# def print_map(road_map) - no test
# def main() - no test

def read_cities(file_name):
    # TODO: check done
    """
    Reads in the cities from the given `file_name`
    Returns the cities data as a list of quadruples (4-element tuples)
    :param file_name: String
    :return road_map: List of Quadruples
    """

    try:
        infile = open(file_name, 'r')
    except FileNotFoundError:
        return 'File not found, please check the name and try again'

    running = True
    road_map = []

    while running:
        line = infile.readline()
        if line == '':
            running = False
        else:
            city_details = line.replace('\n', '').split('\t')
            (state, city, lat, lon) = city_details
            lat = float(lat)
            lon = float(lon)
            road_map.append((state, city, lat, lon))

    infile.close()
    return road_map


def print_cities(road_map):
    # TODO: check done
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    :param road_map: List of Quadruples
    """
    for city_details in road_map:
        (state, city, lon, lat) = city_details
        lon = round(lon, 2)
        lat = round(lat, 2)
        print('{}, {}: {}, {}'.format(city, state, lon, lat))


def compute_total_distance(road_map):
    # TODO: check done
    """
    Sum and return the total euclidean distance between
    each consecutive coordinate in the road_map cycle
    (including distance from last to first location)
    :param road_map: List of Quadruples
    :return total_distance: Float
    """
    total_distance = 0
    for i, city1 in enumerate(road_map):
        coords1 = city1[-2:]
        city2 = road_map[(i + 1) % len(road_map)]
        coords2 = city2[-2:]
        distance = euclidean_distance(coords1, coords2)
        total_distance += distance

    return total_distance


def euclidean_distance(coords1, coords2):
    # TODO: check done
    """
    Calculate the Euclidean distance between 2 cities
    Given coordinates of (x1,y1) and (x2,y2)
    Formula is sqrt((x1-x2)**2 + (y1-y2)**2)
    :param coords1: Tuple containing latitude, longitude
    :param coords2: Tuple containing latitude, longitude
    :return: Float
    """
    lon1, lat1 = coords1
    lon2, lat2 = coords2
    return sqrt((lon1 - lon2)**2 + (lat1 - lat2)**2)


def swap_cities(road_map, index1, index2):
    # TODO: check done
    """
    Swap the elements at index1 and index2 in the road_map
    Calculate total distance of amended road_map
    :param road_map: List of Quadruples
    :param index1: Integer
    :param index2: Integer
    :return new_tuple: Tuple containing a List of Quadruples and a Float
    """
    new_road_map = road_map[:]
    if index1 != index2:
        new_road_map[index1], new_road_map[index2] = new_road_map[index2], new_road_map[index1]

    distance = compute_total_distance(new_road_map)
    new_tuple = (new_road_map, distance)
    return new_tuple


def shift_cities(road_map):
    # TODO: check done
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """
    return [road_map[-1]] + road_map[:-1]


def find_best_cycle(road_map):
    # TODO: check logic and update docstring
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    current_road_map = road_map
    best_cycle = None
    count = 10000
    # choices = ['swap', 'shift']
    while count > 0:
        if count % 2 == 0:
            # if random.choice(choices) == 'shift':
            print('shift')
            current_road_map = shift_cities(current_road_map)
        else:
            print('swap')
            index1, index2 = get_two_random_indices(maximum=len(current_road_map)-1)
            cycle = swap_cities(current_road_map, index1, index2)
            if not best_cycle or cycle[1] < best_cycle[1]:
                current_road_map = cycle[0]
                best_cycle = cycle
        print(best_cycle[1]) if best_cycle else None
        count -= 1

    return best_cycle[0]


def get_two_random_indices(maximum):
    one = random.randint(1, maximum)
    two = random.randint(1, maximum)
    return one, two


def print_map(road_map):
    # TODO: everything (and print, not return)
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    print('visual grid')
    return


def visualise(road_map):
    """ either graphically print the given road_map or will open a GUI window with the drawing
    of the road_map. Also, extend the functionality of your main function so that it provides
    visualisation of the best route  when found. You do not need to test the visualise function.
    """
    print('grid')


def main(file_name=None):
    # TODO: check done
    """
    Open specified file by name
    Print out city data
    Calculate "best" cycle and print it out
    :param file_name: String (optional)
    :return String
    """
    if not file_name:
        file_name = input('Enter the name of the file to read from: ')
    suffix = '.txt'
    if suffix not in file_name:
        file_name += suffix

    road_map = read_cities(file_name)
    print_cities(road_map)

    best_cycle = find_best_cycle(road_map)
    print_map(best_cycle)
    return


if __name__ == "__main__":  # keep this in
    main()
