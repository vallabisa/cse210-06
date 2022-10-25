from ship import Ship
from aliens import Aliens
from bullets import Bullets

class Cast():  
    
    def __init__(self):

        self._alien = Aliens()
        self._aliens = []
        self._ship = Ship()
        self._ships = []
        self._bullets = []
        self._bullet = Bullets(0, 0)
    
    def create_alien(self, pop):
        """
        Create aliens
        """
        while pop > 0:
            self._aliens.append(self._alien)
            pop -= 1   

    def create_ship(self):
        """
        Create a ship
        """
        self._ships.append(self._ship)

    def create_bullet(self, x, y):
        """
        Create a bullet
        """
        self._bullet = Bullets(x, y)
        self._bullets.append(self._bullet)

    def get_all_actors(self):
        self._actors = []
        for alien in self._aliens:
            self._actors.append(alien)

        for bullet in self._bullets:
            self._actors.append(bullet)

        for ship in self._ships:
            self._actors.append(ship)

        return self._actors

    def remove_object(self):
        for bullet in self._bullets:
            if not bullet.alive:
                self._bullets.remove(bullet)

        for alien in self._aliens:
            if not alien.alive:
                self._aliens.remove(alien)