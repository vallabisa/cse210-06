
import constants
import random


from color import Color
from flying_objects import Flying_Objects

class Ship(Flying_Objects):
    
    def __init__(self):
        super().__init__()
        self._text = "<^>"
        self._font_size = 20
        self._color = Color(255, 255, 0)
        self.position.x = int(random.uniform(0, constants.MAX_X))
        self.position.y = int(random.uniform(450, constants.MAX_Y-10))
        self.alive = True
        self.lives = 3

    def move(self, movement):
        if self.position.x < 0:
            self.position.x = constants.MAX_X
        elif self.position.x > constants.MAX_X:
            self.position.x = 0
        else:
            self.position.x += movement
        #print(self.position.x)

    def hit(self):
        """
        Called once collision is made with alien
        """
        self.lives -= 1
        if self.lives <= 0:
            self.alive = False
            