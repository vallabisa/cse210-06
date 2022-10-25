
import constants
import random

from flying_objects import Flying_Objects
from color import Color


class Aliens(Flying_Objects):
    """
    The visual representation of the aliens in the game. 
    Manages the appearance, position and velocity of the aliens.
    """

    def __init__(self):
        super().__init__()
        self._text = "(OwO)"
        self._font_size = 30
        self.alive = True
        self._color = Color(0, 0, 255)
        self.position.x = int(random.uniform(0, constants.MAX_X-20))
        self.position.y = int(random.uniform(0, 20))

    def update(self):
        check = 0
        if self.position.y <= constants.MAX_Y:
            self.position.y += self.position.dy
            self.position.x += (random.randint(-100,100))
        else:
            self.alive = False
            check += 1
        if check == 1:
            print("You Failed! ~ Game Over!")
            
        if self.position.x < 0:
            self.position.x = constants.MAX_X
        elif self.position.x > constants.MAX_X:
            self.position.x = 0



    def hit(self):
        """
        Called once collision is made
        """
        self.alive = False
        

