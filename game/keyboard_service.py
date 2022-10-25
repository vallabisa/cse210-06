
import pyray
from video_service import VideoService



class KeyboardService:
    """This class detects the player's input on the keyboard.

    Attr:
        cell: The size of the current cell on the grid.
    """

    def __init__(self, cell = 5):
        """Constructs a new KeyboardService.
        
        Args:
            cell_size: The size of the current cell in the grid.
        """
        self._cell = cell
        self._bullet = False

    def get_direction(self):
        """Gets the direction based on which keyboard keys the player presses.

        Returns:
            The direction.
        """
        direction_x = 0
        
        if pyray.is_key_down(pyray.KEY_LEFT):
            direction_x = -self._cell
            #print("left")
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            direction_x = self._cell
            #print("right")
        return direction_x
    
    def get_bullet(self):    
        if pyray.is_key_pressed(pyray.KEY_SPACE):
            #self._bullet = True
            #print("fire")
            return True
        return False
            
