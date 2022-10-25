import constants
class Point:
    """A distance from a point of origin.

    Attr:
        _x: The horizontal distance from the point of origin.
        _y: The vertical distance from the point of origin.
    """
    
    def __init__(self):
        """Constructs a new Point.
        
        Args:
            x: The x (horizontal) value.
            y: The y (vertical) value.
        """

        self.x = 0
        self.y = 0
        self.dx = constants.DX
        self.dy = constants.DY

