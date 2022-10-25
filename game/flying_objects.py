import pyray
from point import Point
from color import Color

class Flying_Objects():
    """
    Starting point of the object
    Velocity of the object moving
    """
    def __init__(self):
        self.position = Point()
        self.alive = True

    def draw(self):
        """
        Draw the flying object
        """
        pass

   
    def update(self):
        pass

    def hit(self):
        """
        Called when collision is made with a bullet.
        """
        pass