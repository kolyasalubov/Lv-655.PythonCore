from pygame.constants import HIDDEN


class GameStats:
    """Відстежування статистики гри"""

    def __init__(self, ai_game):
        """Інінціалізація статистики"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Рекорд не анульовуєтсья
        self.high_score = 0

        # Розпочати гру у не активному стані
        self.game_active = False

        # Розпочати гру в активному стані
        # self.game_active = True


    def reset_stats(self):
        """Інінціалізація статистики, що може змініюватись впродовж гри"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
