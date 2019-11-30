from math import sqrt
import random


# CHECKLIST

# TODO: use try/except clauses for various error types! Don't let the tests fail unexpectedly.

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
# def compute_total_distance(road_map)
# def swap_cities(road_map, index1, index2)
# def shift_cities(road_map):
# def find_best_cycle(road_map) - no test
# def print_map(road_map) - no test
# def main() - no test

def read_cities(file_name):
    # TODO: check done
    """
    Read in the data from the given `file_name`
    Return the data as a list of quadruples (4-element tuples)
    :param file_name: String
    :return road_map: List of Quadruples
    """

    road_map = []
    try:
        with open(file_name) as infile:
            for line in infile:
                location = line.replace('\n', '').split('\t')
                state, city, lon, lat = location
                quadruple = (state, city, float(lon), float(lat))
                road_map.append(quadruple)
        return road_map

    except FileNotFoundError:
        print('File not found, check the filename and try again')
        if '.' not in file_name:
            print('Remember to include the file type suffix e.g. filename.txt')
    except ValueError:
        print('Invalid data on line {} of {}'.format(str(len(road_map)+1), file_name))
        if not file_name.endswith('.txt'):
            print('Try using a text file')


def print_cities(road_map):
    # TODO: check done
    """
    Unpack city data from road_map
    Format longitude and latitude to 2 decimal places
    Print a list of cities and their coordinates
    :param road_map: List of Quadruples
    """

    try:
        if not road_map:
            print('No city data to print')
            return
        if not isinstance(road_map, list):
            raise TypeError

        for location in road_map:
            state, city, lon, lat = location
            lon = round_coordinates(lon, city, state, 'longitude')
            lat = round_coordinates(lat, city, state, 'latitude')
            if lon and lat:
                print('{}, {}: {}, {}'.format(city, state, lon, lat))
        print('='*40)

    except (TypeError, ValueError):
        print('Error printing cities, please check data format')


def round_coordinates(coord, city, state, coord_type):
    # TODO: check done!
    """
    Takes a longitude or latitude
    Convert string to float if necessary
    Return the float rounded to 2 decimal places
    :param coord: Float or String
    :param city: String
    :param state: String
    :param coord_type: String
    :return: Float (rounded to 2 decimal places)
    """

    try:
        if isinstance(coord, (str, int)):
            coord = float(coord)
        return round(coord, 2)

    except (TypeError, ValueError):
        print('Error rounding {} for {}, {}. Check data type'.format(coord_type, city, state))


def compute_total_distance(road_map):
    # TODO: catch exceptions
    """
    Iterate over road_map data, sum the distance between each
    consecutive city (including first and last cities, to form a cycle)
    Keep a running sum of the distances and return the total
    :param road_map: List of Quadruples
    :return total_distance: Float
    """

    try:
        if not isinstance(road_map, list):
            raise TypeError

        total_distance = 0
        for i, city1 in enumerate(road_map):
            city2 = road_map[(i + 1) % len(road_map)]
            if not len(city1) == len(city2) == 4:
                raise ValueError
            location1 = city1[-2:]
            location2 = city2[-2:]
            total_distance += euclidean_distance(location1, location2)
        return total_distance

    except (TypeError, ValueError):
        print('Cannot compute total distances, check cities data')


def euclidean_distance(location1, location2):
    # TODO: check done
    """
    Calculate the Euclidean distance between 2 cities
    Accept long/lat coordinates of (x1,y1) and (x2,y2)
    Return formula sqrt((x1-x2)**2 + (y1-y2)**2)
    :param location1: Tuple containing 2 Float elements
    :param location2: Tuple containing 2 Float elements
    :return: Float
    """

    try:
        lon1, lat1 = location1
        lon2, lat2 = location2
        return sqrt((lon1 - lon2)**2 + (lat1 - lat2)**2)

    except (TypeError, ValueError):
        print('Error calculating euclidean_distance, check location data')


def swap_cities(road_map, index1, index2):
    # TODO: catch exceptions
    """
    Swap the elements at index1 and index2 in the road_map list
    Calculate total distance between cities in amended road_map
    :param road_map: List of Quadruples
    :param index1: Integer
    :param index2: Integer
    :return new_tuple: Tuple containing a List of Quadruples and a Float
    """

    try:
        new_map = road_map[:]
        if index1 != index2:
            new_map[index1], new_map[index2] = new_map[index2], new_map[index1]
        distance = compute_total_distance(new_map)
        if distance:
            return tuple((new_map, distance))

    except TypeError:
        print('Error when swapping cities, check data')


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
    # TODO: check done
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
        count = 10000
        while count > 0:
            if count % 2 == 0:
                current_road_map = shift_cities(current_road_map)
            else:
                index1 = get_random_index(len(current_road_map)-1)
                index2 = get_random_index(len(current_road_map)-1)
                cycle = swap_cities(current_road_map, index1, index2)
                if not best_cycle or cycle[1] < best_cycle[1]:
                    current_road_map = cycle[0]
                    best_cycle = cycle
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
    :param best_cycle: Tuple containing List of Tuples and a Float
    """

    try:
        if not best_cycle:
            raise TypeError
        road_map = best_cycle[0]
        for i, city in enumerate(road_map):
            city2 = road_map[(i + 1) % len(road_map)]
            if not len(city) == len(city2) == 4:
                raise ValueError
            cost = euclidean_distance(city[-2:], city2[-2:])
            print('{} to {}: {}'.format(city[0], city2[0], cost))
        total_distance = best_cycle[1]
        print('*** TOTAL COST OF CYCLE: {}'.format(total_distance))

    except (IndexError, TypeError, ValueError):
        print('Invalid data, cannot print map')


def visualise(road_map):
    # TODO: logic (Tkinter?)
    # TODO: catch exceptions
    """ either graphically print the given road_map or will open a GUI window with the drawing
    of the road_map. Also, extend the functionality of your main function so that it provides
    visualisation of the best route  when found. You do not need to test the visualise function.
    """
    print('grid')


def main(file_name=None):
    # TODO: visualisation updates
    """
    Open specified file by name
    Print city data
    Calculate "best" cycle and print it
    TODO print graphic visualisation of the best cycle
    :param file_name: String (optional)
    """

    if not file_name:
        file_name = input('Enter the name of the file to read from: ')

    try:
        road_map = read_cities(file_name)
        if road_map:
            print_cities(road_map)
            best_cycle = find_best_cycle(road_map)
            print_map(best_cycle)
            best_road_map = best_cycle[0]
            # TODO: implement visualise(best_road_map)

    except TypeError:
        pass


if __name__ == "__main__":  # keep this in
    main()
