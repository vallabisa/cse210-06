from point import Point

class Velocity():
    """
    Manages the direction and speed (velocity) of the flying objects in the game.
    """

    def __init__(self):

        self._velocity = Point(0,0)

    def get_velocity(self):
        """Gets the direction and speed (velocity) of the flying objects.
        
        Returns:
            The velocity of the flying objects.
        """

        return self._velocity

    def set_velocity(self, velocity):
        """Updates the velocity of the flying objects.
        
        Args:
            velocity: The new speed and direction of the flying objects.
        """

        self._velocity = velocity