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
    # TODO: make it print, not return ?
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
        tup = (state, city, lat, long)
        rounded_road_map.append(tup)

    return rounded_road_map


def compute_total_distance(road_map):
    # TODO: everything
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    :param road_map: List of Quadruples
    :return Float
    """
    flt = 9.386+18.496+10.646
    return flt


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
    # TODO: finish logic
    """
    Opens specified file by name,
    Prints out city data # TODO
    Calculates "best" cycle and prints it out. # TODO
    :param file_name: String (optional)
    :return String
    """
    if not file_name:
        file_name = input('Enter the name of the file to read from: ')
    suffix = '.txt'
    if suffix not in file_name:
        file_name += suffix
    road_map = read_cities(file_name)

    print_map(road_map)

    # TODO:  more logic here

    return 'best city data'


if __name__ == "__main__":  # keep this in
    main()
