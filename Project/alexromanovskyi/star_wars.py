import sys
from time import sleep

import pygame
import pygame.mouse

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class StarWars:
    """Загальний клас, що керує ресурсами та поведінкою гри"""

    def __init__(self):
        """Ініціалізувати гру, створити ресурс гри"""
        pygame.init()
        self.settings = Settings()

        # Можливість гри у режимі вікна
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))


        # Можливість гри на повний екран
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Star Wars")

        # Створити екземпляр для збереження ігрової статистики
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Створюємо кнпку Play.
        self.play_button = Button(self, "Play")
        
        """Задаєм колір фону"""
        self.bg_color = (255, 255, 255)


    def _create_fleet(self):
        """Створити флот прибульців"""
        # Створити прибульців та визначити їх кількість у ряду.
        # Відстань між прибульцами рівна ширині прибульця
        # Створити прибульця
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Визначити, яка кількість рядів прибульців поміщається на екрані.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                            (2 * alien_height) - ship_height)
        number_rows = available_space_y // (4 * alien_height)

        # # Створити перший ряд прибульців
        # for alien_number in range (number_aliens_x):
        #     self._create_alien(alien_number)

        # Створити повний флот прибульців 
        for row_number in range(number_rows):
            for alien_number in range (number_aliens_x):
                self._create_alien(alien_number, row_number)
    

    def _create_alien(self, alien_number, row_number):
            # Створити першого прибульця та поставити його до ряду
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
            self.aliens.add(alien)


    def _check_fleet_edges(self):
        """
        Реагує відповідно до того, чи досяг прибулець краю екрану
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """Спуск всього флоту та зміна його напрямку"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def run_game(self):
        """Розпочати головний цикл гри"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                
            self._update_screen()


    def _update_bullets(self):
        """Оновити позицію куль та позбавитись старих"""
        # Оновити позицію куль
        self.bullets.update()

        # Позбавляємось куль що зникли
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()        

        
    def _check_bullet_alien_collisions(self):
        """Реакція на зіткнення куль з прибульцями"""
        # Видалити всі кулі та прибульців, що зіткунулися
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
        self.sb.prep_score()
        self.sb.check_high_score()

        if not self.aliens:
            # Знищення наявних куль і творення флоту
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Збільшити рівень
            self.stats.level +=1
            self.sb.prep_level()


    def _update_aliens(self):
        """
        Перевірити, чи флот знаходиться на краю, 
        тоді оновити позиції всіх прибульців флоту
        """
        self._check_fleet_edges() 
        self.aliens.update()

        # Шукати зіткнення корабля із прибульцями.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            print("Ship hit !!!")

        #Шукати чи досяг прибулець нижнього краю
        self._check_aliens_bottom()


    def _check_aliens_bottom(self):
        """Перевірити чи досяг корабель прибульців нижнього краю"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break


    def _check_events(self):
        """Реагує на натискання клавіш та подій миші"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event) 
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        """ Розпочати нову гру, коли користувач натискає кнопку Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if self.play_button.rect.collidepoint(mouse_pos):
            # Анулювати ігрову статистику
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            
            # Приховати курсор миші.
            pygame.mouse.set_visible(False)

            # Позбавитись надлишку прибульців та куль
            self.aliens.empty()
            self.bullets.empty()

            # Створити новий флот та відцентрувати корабель.
            self._create_fleet()
            self.ship.center_ship()


    def _check_keydown_events(self, event):
        """Реагувати на нитискання клавіш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event):
        """Реагувати, коли клавіша не натиснута"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self):
        """ Створити нову кулю та додати її до групи куль"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _ship_hit(self):
        """Реагує на зіткнення прибульція з кораблем"""
        
        if self.stats.ships_left >0:
            # Зменшити життів коробля та оновити табло.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Позбавитися надлишку прибульців та куль.
            self.aliens.empty()
            self.bullets.empty()

            # Створити новий флот та відцентрувати корабель.
            self._create_fleet()
            self.ship.center_ship()

            # Пауза 
            sleep (1.0)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


    def _update_screen(self):
        """Оновити зображення на екрані та перемкнутися на новий екран"""
        # Наново промалювати екран на кажній ітерації циклу
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Намалювати інформацію про рахунок
        self.sb.show_score()

        # Намалюємо кнопку Play, якщо гра неакктивна.
        if not self.stats.game_active:
            self.play_button._draw_button()

        # Показати останній намальований екран.
        pygame.display.flip()

if __name__ == "__main__":
    """ Створити екземпляр гри та запустити гру. """

    ai = StarWars()
    ai.run_game()