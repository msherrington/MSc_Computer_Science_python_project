import os.path

from matplotlib import pyplot as plt
from services import (
    can_be_floated,
    euclidean_distance,
    random_index,
    round_coordinates,
    validate_road_map,
    validate_road_map_data
)

# CHECKLIST

# You must provide good code coverage to catch any errors before we do.
# We expect to see at least 5 tests for each function that needs to be tested (see above).

# Style...
# Use proper indentation and spacing, (check PEP8)
# Don't repeat code if you can put it in a function and just call the function.

# REQUIRED FUNCTIONS X 8:
# def read_cities(file_name) - no test
# def print_cities(road_map) - no test
# ---------------can_be_floated ------------------
# ---------------round coords ------------------
# def compute_total_distance(road_map)
# ---------------euclidean ------------------
# def swap_cities(road_map, index1, index2)
# def shift_cities(road_map):
# def find_best_cycle(road_map) - no test
# ---------------get random index ------------------
# def print_map(road_map) - no test
# ---------------visualise ------------------
# def main() - no test


def read_cities(file_name):
    """
    Read in the data from the given `file_name`
    Return the data as a list of quadruples (4-element tuples)
    :param file_name: String
    :return road_map: List of Quadruples
    """

    if not isinstance(file_name, str):
        raise TypeError('File name must be a string, not a {}'.format(type(file_name)))
    if not os.path.exists(file_name):
        message = 'File "{}" not found.'.format(file_name)
        if '.' not in file_name:
            message += ' Remember to add the file suffix e.g. "file_name.txt"'
        raise FileNotFoundError(message)

    road_map = []
    with open(file_name) as infile:
        for line in infile:
            location = line.replace('\n', '').split('\t')
            if len(location) != 4:
                raise ValueError('Line {} of {} must contain 4 elements'.format(str(len(road_map)+1), file_name))
            state, city, lat, lon = location
            if not all(can_be_floated(x) for x in [lat, lon]):
                raise ValueError('Invalid data on line {} of {}'.format(str(len(road_map)+1), file_name))
            road_map.append((state, city, float(lat), float(lon)))
    return road_map


def print_cities(road_map):
    """
    Unpack city data from road_map
    Format latitude and longitude to 2 decimal places
    Print a list of cities and their coordinates
    :param road_map: List of Quadruples
    """

    road_map = validate_road_map(road_map)

    for location in road_map:
        if len(location) != 4:
            raise ValueError('Each road_map index must contain 4 elements')
        state, city, lat, lon = location
        lat = round_coordinates(lat)
        lon = round_coordinates(lon)
        if lat and lon:
            print('{}, {}: {}, {}'.format(city, state, lat, lon))
    print('='*40)


def compute_total_distance(road_map):
    """
    Iterate over road_map data, sum the distance between each
    consecutive city (including first and last cities, to form a cycle)
    Keep a running sum of the distances and return the total
    :param road_map: List of Quadruples
    :return total_distance: Float
    """

    road_map = validate_road_map(road_map)
    road_map = validate_road_map_data(road_map)

    total_distance = 0
    for i, city in enumerate(road_map):
        next_city = road_map[(i + 1) % len(road_map)]
        total_distance += euclidean_distance(city[-2:], next_city[-2:])
    return total_distance


def swap_cities(road_map, index1, index2):
    """
    Swap the elements at index1 and index2 in the road_map list
    Calculate total distance between cities in amended road_map
    :param road_map: List of Quadruples
    :param index1: Integer
    :param index2: Integer
    :return new_tuple: Tuple containing a List of Quadruples and a Float
    """

    road_map = validate_road_map(road_map)

    indices = [index1, index2]
    if not all(isinstance(i, int) for i in indices):
        raise TypeError('Index must be an integer')

    if not all(0 <= i <= len(road_map) for i in indices):
        raise IndexError('Index cannot be negative, or higher than length of road_map list')

    new_map = road_map[:]
    if index1 != index2:
        new_map[index1], new_map[index2] = new_map[index2], new_map[index1]
    distance = compute_total_distance(new_map)
    return tuple((new_map, distance))


def shift_cities(road_map):
    """
    Return a new version of the road_map list
    with the last index moved to index zero
    and all other elements moved to the next index along
    :param road_map: List of Quadruples
    :return List of Quadruples
    """

    road_map = validate_road_map(road_map)
    return [road_map[-1]] + road_map[:-1]


def find_best_cycle(road_map):
    """
    Perform 10,000 iterations of either shifting or swapping indices in road_map
    Swapping occurs using randomly generated indices
    Calculate the total distance after each shift
    Each iteration uses the shortest road_map found so far
    :param road_map: List of Quadruples
    :return best_road_map: List of Quadruples
    """

    current_road_map = validate_road_map(road_map)
    best_road_map = current_road_map
    shortest_distance = compute_total_distance(current_road_map)

    maximum = len(current_road_map) - 1

    count = 10000
    while count > 0:
        current_road_map = shift_cities(best_road_map)
        index1, index2 = random_index(maximum), random_index(maximum)
        swapped_road_map, swapped_distance = swap_cities(current_road_map, index1, index2)

        if swapped_distance < shortest_distance:
            best_road_map, shortest_distance = swapped_road_map, swapped_distance
        count -= 1
    return best_road_map


def print_map(road_map):
    """
    Print the connection and cost between each city
    Print the total cost for the entire cycle
    :param road_map: List of Quadruples
    """

    road_map = validate_road_map(road_map)
    road_map = validate_road_map_data(road_map)

    for i, city in enumerate(road_map):
        next_city = road_map[(i + 1) % len(road_map)]
        cost = euclidean_distance(city[-2:], next_city[-2:])
        print('{} to {}: {}'.format(city[0], next_city[0], cost))

    total_distance = compute_total_distance(road_map)
    print('*** TOTAL COST OF CYCLE: {}'.format(total_distance))


def main():
    """
    Open specified file by name
    Format and print city data
    Calculate "best" cycle and print it
    Display the best cycle as a plotted graph
    """

    file_name = input('Enter the name of the file to read from: ')

    road_map = read_cities(file_name)
    print_cities(road_map)

    best_road_map = find_best_cycle(road_map)
    print_map(best_road_map)

    visualise(best_road_map)


def visualise(road_map):
    """
    Graphically display the given road_map cycle
    as a popup display within the IDE and
    saved as road_map.png file within the project directory
    :param road_map: List of Quadruples
    """

    road_map = validate_road_map(road_map)

    plt.title('Travelling Salesman\'s Road Map')

    plt.xlabel('Longitude')
    x = [round_coordinates(rm[3]) for rm in road_map]
    x.append(x[0])

    plt.ylabel('Latitude')
    y = [round_coordinates(rm[2]) for rm in road_map]
    y.append(y[0])

    plt.plot(x, y, 'rD')  # vertices
    plt.plot(x, y, '-b')  # edges
    for i in range(len(x)-1):
        plt.annotate(str(i+1), (x[i], y[i]))  # vertex labels

    plt.savefig("road_map.png")
    plt.show()


if __name__ == "__main__":
    main()
