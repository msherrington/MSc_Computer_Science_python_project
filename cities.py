def read_cities(file_name):
    """
    Reads in the cities from the given `file_name`
    Returns the cities data as a list of four-tuples
    :param file_name: string
    :return road_map: list of tuples
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
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """
    return road_map


def compute_total_distance():
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    return 9.386+18.496+10.646


def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    if index1 != index2:
        road_map[index1], road_map[index2] = road_map[index2], road_map[index1]
    return road_map


def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """
    return [road_map[-1]] + road_map[:-1]


def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    return road_map


def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    return road_map


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    file_name = input('Enter the name of the file to read from: ')
    suffix = '.txt'
    if suffix not in file_name:
        file_name += suffix
    road_map = read_cities(file_name)
    print(road_map)

    # more logic here

    return 'best city data'


if __name__ == "__main__": #keep this in
    main()
