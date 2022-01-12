class Settings:
    """Клас для зберігання всіх налаштувань гри"""

    def __init__(self):
        """Ініціалізувати постійні налаштування гри"""

        # Параметри екрану
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # Налаштування коробля
        self.ship_speed = 0.75
        self.ship_limit = 3

        # Налаштування кулі
        self.bullet_speed = 1.0
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (255, 102, 102)
        self.bullets_allowed = 3

        # Налаштування прибульців
        self.alien_speed = 0.1
        self.fleet_drop_speed = 15

        # fleet_directin це напрям руху: 1 праворуч, -1 ліворуч
        self.fleet_direction = 1

        # Як швидко гра має прискорюватися
        self.speedup_scale = 1.2
        self.initialize_dynamic_settings()

        # Як швидко збільшується вартість прибульців
        self.score_scale = 1.5

    
    def initialize_dynamic_settings(self):
        """ Ініціалізація змінних налаштувань."""
        self.ship_speed = 0.5
        self.bullet_speed = 1.5
        self.alien_speed = 0.2
        self.alien_points = 50

        # fleet_directin це напрям руху: 1 праворуч, -1 ліворуч
        self.fleet_direction = 1


    def increase_speed(self):
        """ Збільшення налаштувань швидкості та вартості прибульців"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)