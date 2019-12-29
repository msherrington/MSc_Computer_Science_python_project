import matplotlib.pyplot as plt
import os.path
import random

from math import sqrt

# CHECKLIST

# TODO: Raise Errors, don't catch them!!
# TODO: test for raised errors


# You must implement all the required functions and the implementation must handle all the permitted inputs correctly.
# You must provide good code coverage to catch any errors before we do.
# We expect to see at least 5 tests for each function that needs to be tested (see above).

# Style...
# Use proper indentation and spacing, (check PEP8)
# Don't repeat code if you can put it in a function and just call the function.
# Try to avoid redundancy (such as the beginner's if better == True).

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
        raise TypeError('Filename must be a string, not a {}'.format(type(file_name)))
    if not os.path.exists(file_name):
        message = 'File "{}" not found.'.format(file_name)
        if '.' not in file_name:
            message += ' Remember to add the file suffix e.g. "filename.txt"'
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
            quadruple = (state, city, float(lat), float(lon))
            road_map.append(quadruple)
    return road_map


def validate_road_map(road_map):
    if not isinstance(road_map, list):
        raise TypeError('The road_map must be a list')
    if len(road_map) == 0:
        raise IndexError('The road_map list cannot be empty')
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


def can_be_floated(value):
    """
    Check if a datatype can be floated without errors
    :param value: any datatype
    :return: Boolean
    """

    if not isinstance(value, (str, int, float)):
        return False
    try:
        float(value)
        return True
    except ValueError:
        return False


def round_coordinates(coord):
    """
    Takes a latitude or longitude
    Return a float rounded to 2 decimal places
    :param coord: Number or String
    :return: Float (rounded to 2 decimal places)
    """

    if not isinstance(coord, (str, int, float)):
        raise TypeError('Coordinate must be string or number')
    if not can_be_floated(coord):
        raise ValueError('Cannot float coordinate')
    return round(float(coord), 2)


def compute_total_distance(road_map):
    """
    Iterate over road_map data, sum the distance between each
    consecutive city (including first and last cities, to form a cycle)
    Keep a running sum of the distances and return the total
    :param road_map: List of Quadruples
    :return total_distance: Float
    """

    road_map = validate_road_map(road_map)

    total_distance = 0
    for i, city in enumerate(road_map):
        next_city = road_map[(i + 1) % len(road_map)]
        if not all(isinstance(c, tuple) for c in [city, next_city]):
            raise TypeError('Each road_map element must be a tuple')
        if not len(city) == len(next_city) == 4:
            raise ValueError('Each tuple in the road_map must contain 4 elements')
        if not all(isinstance(c, float) for c in [city[2], city[3], next_city[2], next_city[3]]):
            raise TypeError('Coordinates must be of type float')
        location1 = city[-2:]
        location2 = next_city[-2:]
        total_distance += euclidean_distance(location1, location2)
    return total_distance


def euclidean_distance(location1, location2):
    """
    Calculate the Euclidean distance between 2 cities
    Accept lat/lon coordinates of (x1,y1) and (x2,y2)
    Return formula sqrt((x1-x2)**2 + (y1-y2)**2)
    :param location1: Tuple containing 2 Float elements
    :param location2: Tuple containing 2 Float elements
    :return: Float
    """

    locations = [location1, location2]
    if not all(isinstance(x, (tuple, list)) for x in locations):
        raise TypeError('Coordinates must be packed in tuples or lists')
    if not all(len(x) == 2 for x in locations):
        raise ValueError('Exactly two elements required in location tuple')
    lat1, lon1 = location1
    lat2, lon2 = location2
    if not all(isinstance(x, (float, int)) for x in [lat1, lon1, lat2, lon2]):
        raise TypeError('Coordinates must be a number')
    return sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)


def swap_cities(road_map, index1, index2):
    # TODO: check done
    """
    Swap the elements at index1 and index2 in the road_map list
    Calculate total distance between cities in amended road_map
    :param road_map: List of Quadruples
    :param index1: Integer
    :param index2: Integer
    :return new_tuple: Tuple containing a List of Quadruples and a Float
    """

    try:
        indices = [index1, index2]
        if not all(isinstance(i, int) for i in indices) or not isinstance(road_map, list):
            raise TypeError

        new_map = road_map[:]
        if not all(new_map[i] and i >= 0 for i in indices):
            raise IndexError

        if index1 != index2:
            new_map[index1], new_map[index2] = new_map[index2], new_map[index1]
        distance = compute_total_distance(new_map)
        if distance:
            return tuple((new_map, distance))

    except TypeError:
        print('Data error. Check road_map and indices data types')
    except IndexError:
        print('Index cannot be negative, or higher than length of road_map list')


def shift_cities(road_map):
    # TODO: check done
    """
    Return a mutated version of the road_map list
    with the last index moved to index zero
    and all other elements moved to the next index along
    :param road_map: List of Quadruples
    :return List of Quadruples
    """

    try:
        return [road_map[-1]] + road_map[:-1]
    except IndexError:
        print('Cannot shift cities in empty road_map')
    except TypeError:
        print('Invalid datatype, cannot shift cities')


def find_best_cycle(road_map):
    """
    Perform 10,000 iterations of either shifting or swapping indices in road_map
    Swapping occurs using randomly generated indices
    Calculate the total distance after each shift
    Each iteration uses the shortest road_map found so far
    :param road_map: List of Quadruples
    :return best_cycle: Tuple containing a List of Quadruples and a Float
    """

    try:
        if not road_map:
            raise ValueError
        current_road_map = road_map
        best_cycle = None
        maximum = len(road_map) - 1
        count = 10000
        while count > 0:
            temp_road_map = shift_cities(current_road_map) if count % 2 != 0 else current_road_map
            index1 = get_random_index(maximum)
            index2 = get_random_index(maximum)
            cycle = swap_cities(temp_road_map, index1, index2)
            if not best_cycle or cycle[1] < best_cycle[1]:
                best_cycle = cycle
                current_road_map = cycle[0]
            count -= 1
        return best_cycle

    except(TypeError, ValueError):
        print('Error finding best cycle')


def get_random_index(maximum):
    """
    Return random integers in the range 0 to maximum
    :param maximum: integer
    :return integer
    """

    try:
        return random.randint(0, maximum)

    except (TypeError, ValueError):
        print('Invalid number: must be positive integer')


def print_map(best_cycle):
    # TODO: check ths one carefully
    # TODO: catch exceptions
    """
    Print the connection and cost between each city
    Print the total cost for the entire cycle
    :param best_cycle: Tuple containing List of Quadruples and a Float
    """

    try:
        if not best_cycle:
            raise TypeError
        road_map = best_cycle[0]
        for i, city in enumerate(road_map):
            next_city = road_map[(i + 1) % len(road_map)]
            if not len(city) == len(next_city) == 4:
                raise ValueError
            cost = euclidean_distance(city[-2:], next_city[-2:])
            print('{} to {}: {}'.format(city[0], next_city[0], cost))
        total_distance = best_cycle[1]
        print('*** TOTAL COST OF CYCLE: {}'.format(total_distance))

    except (IndexError, TypeError, ValueError):
        print('Invalid data, cannot print map')


def visualise(road_map):
    # TODO: raise exceptions
    """
    Graphically display the given road_map cycle
    as a popup display within the IDE and
    saved as a .png file within the project directory
    :param road_map: List of Quadruples
    """

    plt.title('Travelling Salesman\'s Road Map')

    plt.xlabel('Longitude')
    x = [round_coordinates(lon, city, state) for state, city, lat, lon in road_map]
    x.append(x[0])

    plt.ylabel('Latitude')
    y = [round_coordinates(lat, city, state) for state, city, lat, lon in road_map]
    y.append(y[0])

    plt.plot(x, y, 'rD')  # vertices
    plt.plot(x, y, '-b')  # edges
    for i in range(len(x)-1):
        plt.annotate(str(i+1), (x[i], y[i]))  # vertex labels

    plt.savefig("road_map.png")
    plt.show()


def main():
    # TODO: raise errors (?) - maybe not
    """
    Open specified file by name
    Format and print city data
    Calculate "best" cycle and print it
    Display the best cycle as a plotted graph
    """

    file_name = input('Enter the name of the file to read from: ')

    road_map = read_cities(file_name)
    print_cities(road_map)

    best_cycle = find_best_cycle(road_map)
    print_map(best_cycle)

    best_road_map = best_cycle[0]
    visualise(best_road_map)


if __name__ == "__main__":  # keep this in
    main()
