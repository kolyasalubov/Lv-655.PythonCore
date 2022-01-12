import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Клас для керування кораблем."""

    def __init__(self, ai_game):
        
        """Інаціалізувати корабль та встановыть його вихідне положення."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Завантажити зображення коробля та отриманти його rect
        self.image = pygame.image.load(r"C:\Users\Easy\Desktop\PythonCore\Home_work\Lv-655.PythonCore\Project\alexromanovskyi\images\x.jpg").convert()

        self.rect = self.image.get_rect()

        #Створити кожен новий корабль внизу екрана, по центру.
        self.rect.midbottom = self.screen_rect.midbottom
        #Зберегти десяткове значення для позиції коробля по горозитолі.
        self.x = float(self.rect.x)
        #Індикатор руху
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Оновити поточну позицію коробля на основі індикатору руху."""
        #Оновиити значення ship.x, а не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            self.rect.x -= 1
        #Оновиит обьєкт rect з rect.x
        self.rect.x = self.x


    def blitme(self):
        """Намалювати коробаль у його поточному розташуванні."""
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """ Відцентрувати корабель на екрані"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)