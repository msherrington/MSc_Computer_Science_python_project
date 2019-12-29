import random

class Services:
    """
    Service for reusable utility methods
    """

    @staticmethod
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

    @staticmethod
    def random_index(maximum):
        """
        Return random integers in the range 0 to maximum
        :param maximum: integer
        :return integer
        """

        if not isinstance(maximum, int):
            raise TypeError('Maximum must be an integer')
        if maximum < 0:
            raise ValueError('Maximum must be a positive integer')
        return random.randint(0, maximum)

    @staticmethod
    def round_coordinates(coord):
        """
        Takes a latitude or longitude
        Return a float rounded to 2 decimal places
        :param coord: Number or String
        :return: Float (rounded to 2 decimal places)
        """

        if not isinstance(coord, (str, int, float)):
            raise TypeError('Coordinate must be string or number')
        if not Services().can_be_floated(coord):
            raise ValueError('Cannot float coordinate')
        return round(float(coord), 2)

    @staticmethod
    def validate_road_map(road_map):
        if not isinstance(road_map, list):
            raise TypeError('The road_map must be a list')
        if len(road_map) == 0:
            raise IndexError('The road_map list cannot be empty')
        return road_map
