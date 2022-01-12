import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Клас, що представляє одного прибульця з флоту """
    def __init__(self, ai_game):
        """Ініціалізувати прибульця та задати його початкове розташування"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Завантажуємо картинку прибульця та задаєм rect атрибути
        self.image = pygame.image.load(r"C:\Users\Easy\Desktop\PythonCore\Home_work\Lv-655.PythonCore\Project\alexromanovskyi\images/t.jpg").convert()
        self.rect = self.image.get_rect()

        #Старт кожного нового прибульця в верхньому лівому кутку екрану
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    

        #Помістити прибульців в конкретній горизонтальній позиції
        self.x = float(self.rect.x)


    def check_edges(self):
        """ Повертає істину, якщо прибулець знаходиться на краю екрану"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True


    def update(self):
        """Змістити прибульців праворуч та ліворуч"""
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x