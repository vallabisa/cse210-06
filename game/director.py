from pyray import *
from keyboard_service import KeyboardService
from cast import Cast
from video_service import VideoService

class Director:
    """
    Controls the game play and executes acctions as needed till game 
    is closed   
    """
    def __init__(self):
        self._video_service = VideoService()
        self._keyboard_service = KeyboardService()
        self._pop = 10
        self._cast = Cast()
        self.score = 0

    def start_game(self):
        """
        Run the game loop till game closed
        """
        self._video_service.open_window()
        self.populate()
        while not window_should_close():
            self.update()
            self._video_service.first_buffer()
            self.draw_objects()
            self._video_service.second_buffer()
    
    def populate(self):
        self._cast.create_ship()
        self._cast.create_alien(self._pop)
        
  
    def draw_objects(self):
        actors = self._cast.get_all_actors()
        #print(actors)
        self._video_service.display_flying_objects(actors)

    def update(self):
        self._cast._ship.move(self._keyboard_service.get_direction())
        check = self._keyboard_service.get_bullet()
        if check:
            self._cast.create_bullet(self._cast._ship.position.x, self._cast._ship.position.y)
        self._cast._alien.update()
        for bullets in self._cast._bullets:
            bullets.update()
        self.collision()
        self.removal()

    def collision(self):
        """
        check for collisions
        """
        too_close = 0
        #run through all objects and check for collision
        for alien in self._cast._aliens:
            for bullet in self._cast._bullets:
                if bullet.alive and alien.alive:
                    #print(alien.position.y)
                    #print(bullet.position.y)
                    #print(bullet.position.y - alien.position.y)
                    #collision of bullet and alien
                    
                    if ((#first section
                        (bullet.position.x - alien.position.x) >= too_close and # > 0 < 40
                        (bullet.position.x - alien.position.x) <= (too_close + 40)
                        ) and #and second section
                        ((bullet.position.y - alien.position.y) >= too_close and
                        (bullet.position.y - alien.position.y) <= (too_close + 30)
                        )):
                    
                    #if (((bullet.position.x - alien.position.x) < 0 > 40) and 
                        #(bullet.position.y - alien.position.y < 0 > 30)):
                        #update objects and score
                        #print("hit here")
                        bullet.hit()
                        alien.hit()
                        self.score += 5
                        print(f"Score: {self.score}")
                        print("You win! ~ Game Over!")
        
        for alien in self._cast._aliens:    
            for ship in self._cast._ships:
                if ship.alive and alien.alive:
                    #print(ship.position.y)
                    #print(alien.position.y)
                    #print((ship.position.y - alien.position.y))
                    #collision of ship and alien
                    if ((#first section
                        (ship.position.x - alien.position.x) >= too_close and
                        (ship.position.x - alien.position.x) <= (too_close + 30)
                        ) and #and second section
                        ((ship.position.y - alien.position.y) >= too_close and
                        (ship.position.y - alien.position.y) <= (too_close + 30)
                        )):
                        #update objects and score
                        #print("hit alien")
                        alien.hit()
                        ship.hit()
                        self.score -= 5
                        print(f"Score: {self.score}")
                        print("You Died! ~ Game Over!")
                        ship.hit()

    def removal(self):
        self._cast.remove_object()


