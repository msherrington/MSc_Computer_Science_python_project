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
    def validate_road_map(road_map):
        if not isinstance(road_map, list):
            raise TypeError('The road_map must be a list')
        if len(road_map) == 0:
            raise IndexError('The road_map list cannot be empty')
        return road_map
