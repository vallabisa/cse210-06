class Color:
    """Chooses the colors to be displayed on the screen for the chosen objects.

    Attr:
        _red: The RGB value for the color red.
        _green: The RGB value for the color green.
        _blue: The RGB value for the color blue.
        _opacity: The numerical value for the opacity.
    """
    
    def __init__(self, red, green, blue, opacity = 255):
        """Constructs a new Color.
        
        Args:
            red: The RGB value for the color red.
            green: The RGB value for the color green.
            blue: The RGB value for the color blue.
            opacity: The numerical value for the opacity.
        """

        self._red = red
        self._green = green
        self._blue = blue 
        self._opacity = opacity

    def rgb_value(self):
        """Gets the RGB values of the various colors.

        Returns:
            RGB: The chosen color as an RGB value.
        """

        return (self._red, self._green, self._blue, self._opacity)   