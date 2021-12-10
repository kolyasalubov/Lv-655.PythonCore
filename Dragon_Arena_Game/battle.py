import pygame
import random
from pygame import mixer

pygame.init()

#set framerate
clock = pygame.time.Clock()
fps = 60

#game_window
bottom_panel = 200
screen_width = 1280
screen_height = 1024 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dragon Arena")

#define game variables
current_fighter = 0
total_fighters = 5
action_cooldown = 0
action_wait_time = 90
attack = False
potion = False
clicked = False


#define fonts
font = pygame.font.SysFont('Times New Roman', 36)

#define font colors
red = (255, 0, 0)
green = (0, 255, 0)


#load images and music
# background image
background_img = pygame.image.load('Dragon_Arena_Game/img/Background/background.jpg').convert_alpha()
# background sound
mixer.music.load('Dragon_Arena_Game/sound/background.wav')
mixer.music.play(-1)
# panel image
panel_img = pygame.image.load('Dragon_Arena_Game/img/Icons/panel.jpg').convert_alpha()
sword_img = pygame.image.load('Dragon_Arena_Game/img/Icons/sword.png').convert_alpha()


#function for drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


#function for drawing background
def draw_bg():
    screen.blit(background_img, (0, 0))

#function for drawing panel
def draw_panel():
    #draw panel rectangle
    screen.blit(panel_img, (0, screen_height - bottom_panel))
    #show dragon stats
    # draw_text(f'{golden_dragon.name} HP: {golden_dragon.hp}', font, red, 100, screen_height - bottom_panel + 20)
    for count, i in enumerate(dragon_list):
        #show name and health
        draw_text(f'{i.name} HP: {i.hp}', font, green, 100, (screen_height - bottom_panel + 20) + count * 60)
    for count, i in enumerate(monster_list):
        #show name and health
        draw_text(f'{i.name} HP: {i.hp}', font, red, 750, (screen_height - bottom_panel + 20) + count * 60)


# Class for all creatures
class Fighter():
    def __init__(self, x, y, name, max_hp, strength, potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_potions = potions
        self.potions = potions
        self.alive = True

        self.animation_list = []
        self.frame_index = 0

        self.action = 0 #0: idle, 1:ability_1

        self.update_time = pygame.time.get_ticks()

        #load idle images
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f"Dragon_Arena_Game/img/{self.name}/Idle/{i}.png")
            img = pygame.transform.scale(img, (250, 250))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        #load attack ability_1 images
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f"Dragon_Arena_Game/img/{self.name}/Ability_1/{i}.png")
            img = pygame.transform.scale(img, (250, 250))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def update(self):
        animation_cooldown = 100
        #handle animation
        #update image
        self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #if the animation has run out, then reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.idle()

    def draw(self):
        screen.blit(self.image, self.rect)


    def idle(self):
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()


    def attack(self, target):
        #deal damage to enemy
        rand = random.randint(-5, 5)
        damage = self.strength + rand
        target.hp -= damage
        #check if target has died
        if target.hp < 1:
            target.hp = 0
            target.alive = False
        #set variables to attack animation
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, hp):
        #update with new health
        self.hp = hp
        #calculate health ratio
        ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, red, (self.x, self.y, 200, 15))
        pygame.draw.rect(screen, green, (self.x, self.y, 200 * ratio, 15))


golden_dragon = Fighter(200, 260, 'Golden Dragon', 30, 10, 3)
forest_dragon = Fighter(300, 460, 'Forest Dragon', 30, 10, 3)
silver_dragon = Fighter(200, 660, 'Silver Dragon', 30, 10, 3)

dragon_list = []
dragon_list.append(golden_dragon)
dragon_list.append(forest_dragon)
dragon_list.append(silver_dragon)

monster_snake_1 = Fighter(1010, 260, 'Monster Snake', 30, 6, 1)
monster_snake_2 = Fighter(910, 460, 'Monster Snake', 30, 6, 1)
monster_snake_3 = Fighter(1010, 660, 'Monster Snake', 30, 6, 1)

monster_list = []
monster_list.append(monster_snake_1)
monster_list.append(monster_snake_2)
monster_list.append(monster_snake_3)


golden_dragon_health_bar = HealthBar(100, screen_height - bottom_panel + 60, golden_dragon.hp, golden_dragon.max_hp)
forest_dragon_health_bar = HealthBar(100, screen_height - bottom_panel + 120, forest_dragon.hp, forest_dragon.max_hp)
silver_dragon_health_bar = HealthBar(100, screen_height - bottom_panel + 180, silver_dragon.hp, silver_dragon.max_hp)
monster_snake_1_health_bar = HealthBar(750, screen_height - bottom_panel + 60, monster_snake_1.hp, monster_snake_1.max_hp)
monster_snake_2_health_bar = HealthBar(750, screen_height - bottom_panel + 120, monster_snake_2.hp, monster_snake_2.max_hp)
monster_snake_3_health_bar = HealthBar(750, screen_height - bottom_panel + 180, monster_snake_3.hp, monster_snake_3.max_hp)



run = True
while run:

    clock.tick(fps)

    #draw background
    draw_bg()

    #draw panel
    draw_panel()
    golden_dragon_health_bar.draw(golden_dragon.hp)
    forest_dragon_health_bar.draw(forest_dragon.hp)
    silver_dragon_health_bar.draw(silver_dragon.hp)
    monster_snake_1_health_bar.draw(monster_snake_1.hp)
    monster_snake_2_health_bar.draw(monster_snake_2.hp)
    monster_snake_3_health_bar.draw(monster_snake_3.hp)

    #draw fighters
    for dragon in dragon_list:
        dragon.update()
        dragon.draw()

    # golden_dragon.update()
    # golden_dragon.draw()
    # forest_dragon.update()
    # forest_dragon.draw()
    # silver_dragon.update()
    # silver_dragon.draw()
    for monster in monster_list:
        monster.update()
        monster.draw()



    #control player actions
    #reset action variables
    attack = False
    potion = False
    target = None
    #make sure mouse is visible
    pygame.mouse.set_visible(True)
    pos = pygame.mouse.get_pos()
    for count, monster in enumerate(monster_list):
        if monster.rect.collidepoint(pos):
            #hide mouse
            pygame.mouse.set_visible(False)
            #show sword in place of mouse cursor
            screen.blit(sword_img, pos)
            if clicked == True:
                attack = True
                target = monster_list[count]




    #player action
    for count, dragon in enumerate(dragon_list):
        if current_fighter == 0 + count:
            if dragon.alive == True:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    #attack
                    if attack == True and target != None:
                        dragon.attack(target)
                        current_fighter += 1
                        action_cooldown = 0
            else:
                current_fighter += 1


    #enemy action
    for count, monster in enumerate(monster_list):
        if current_fighter == 3 + count:
            if monster.alive == True:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    #attack
                    monster.attack(random.choice(dragon_list))
                    current_fighter += 1
                    action_cooldown = 0
            else:
                current_fighter += 1

#if all fighters have had a turn then reset
    if current_fighter > total_fighters:
        current_fighter = 1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        else:
            clicked = False

    pygame.display.update()

pygame.quit()