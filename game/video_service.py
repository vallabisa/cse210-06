import pyray
import constants

class VideoService:
    """The responsibility of this class is to display the game on the screen. 
    """

    def __init__(self, debug = False):
        """Constructs a new VideoService.
        
        Args:
            debug: Checks to see whether the program needs to be run in debug mode.
        """
        self._debug = debug

    def is_window_open(self):
        """Checks whether the window is open.

        Returns:
            A value of "True" if the window is open or "False" if the window is closed.
        """

        return not pyray.close_window()

    def open_window(self):
        """Opens the window.
        """

        pyray.init_window(constants.MAX_X, constants.MAX_Y, constants.CAPTION)
        pyray.set_target_fps(constants.FRAME_RATE)

    def first_buffer(self):
        """Prepares the screen for the next output of the game by clearing the screen and
        drawing the next output.
        """

        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)

        if self._debug == True:
            self._draw_grid()

    def second_buffer(self):
        """Prepares the screen after the end of the game's output.
        """ 

        pyray.end_drawing()

    def draw(self, actor):
        #print(actor)
        text = actor._text
        #print(text)
        x = actor.position.x
        #print(x)
        y = actor.position.y
        #print(y)
        font_size = actor._font_size
        #print(font_size)
        color = actor._color.rgb_value()
        #print(color)
        pyray.draw_text(text, x, y, font_size, color)


    def display_flying_objects(self, objects):
        """Displays the Flying Object on the screen.

        Args:
            flying_object: The Flying Object.
        """ 

        for object in objects:
            #print() 
            #print(objects)
            self.draw(object)
                   

    def _draw_grid(self):
        """
        Draws a grid on the screen and is used as a way to gather coordinates to determine the
        position of objects on the screen.
        """
        pass
        for x in range(0, constants.MAX_X, constants.CELL_SIZE):
            pyray.draw_line(x, 0, x, constants.MAX_Y, pyray.GREY)

        for y in range(0, constants.MAX_Y, constants.CELL_SIZE):
            pyray.draw_line(0, y, constants.MAX_X, y, pyray.GREY)

    def close_window(self):
        """Closes the window."""

        pyray.close_window()