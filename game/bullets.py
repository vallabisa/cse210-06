import constants
from flying_objects import Flying_Objects
from color import Color
from point import Point

class Bullets(Flying_Objects):
    """
    The visual representation of the bullets in the game. 
    Manages the appearance, position and velocity of the bullets.
    """

    def __init__(self, ship_x, ship_y):
        super().__init__()
        self._text = ".^."
        self._font_size = 15
        self._color = Color(255, 0, 0)
        self.position.x = ship_x
        self.position.y = ship_y
        self.alive = True
        self.move = Point()


    def update(self):
        if self.position.y >= 0:
            self.position.y -= (self.move.dy + 50) 
        else:
            self.alive = False

    def hit(self):
        """
        Called once collision is made
        """
        self.alive = False
        #print("hit")


