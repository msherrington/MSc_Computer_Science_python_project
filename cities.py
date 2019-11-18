from math import sqrt


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
            four_tuple = tuple(city_details)
            road_map.append(four_tuple)

    infile.close()
    return road_map


def print_cities(road_map):
    # TODO: check done
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    :param road_map: List of Quadruples
    :return rounded_road_map: List of Quadruples
    """
    rounded_road_map = []
    for city_details in road_map:
        state, city, lat, long = city_details
        lat = round(lat, 2)
        long = round(long, 2)
        quad = (state, city, lat, long)
        rounded_road_map.append(quad)
    print(rounded_road_map)
    return


def compute_total_distance(road_map):
    # TODO: check logic, update docstring
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
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
    """
    Calculate the Euclidean distance between 2 cities
    The distance between any two cities with the coordinates (x1, y1) and (x2,y2) is the standard Euclidean distance
    sqrt((x1-x2)^2 + (y1-y2)^2)
    :param coords1: Tuple containing longitude, latitude
    :param coords2: Tuple containing longitude, latitude
    :return: Float
    """
    long1, lat1 = coords1
    long2, lat2 = coords2
    return sqrt((long1 - long2)**2 + (lat1 - lat2)**2)


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
    # TODO: everything
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """

    return road_map


def print_map(road_map):
    # TODO: everything (and print, not return?)
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    return road_map


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
