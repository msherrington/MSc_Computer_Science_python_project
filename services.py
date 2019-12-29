class Services:
    """
    Service for reusable utility methods
    """

    @staticmethod
    def validate_road_map(road_map):
        if not isinstance(road_map, list):
            raise TypeError('The road_map must be a list')
        if len(road_map) == 0:
            raise IndexError('The road_map list cannot be empty')
        return road_map
