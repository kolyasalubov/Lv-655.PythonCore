import pygame

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# This sets the name of the window
pygame.display.set_caption('Fly')

clock = pygame.time.Clock()

# обновляємо екран
pygame.display.update()
pygame.mouse.set_visible(False)

# Set positions of graphics
background_position = [0, 0]

# Load and set up graphics.
#background_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load(
    '4825026.png').convert()

# Якщо в зображення не має прозорого слою, то щоб його встановити,
# необхідно використати метод set_colorkey() класу Surface:
player_image.set_colorkey(BLACK)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


# Get the current mouse position. This returns the position
    # as a list of two numbers.
# повертає поточну позицію мишки на екрані
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]

    if x >= 150:
        x = x-150
    if y >= 150:
        y = y-150

    # Copy image to screen:
# копіює картинку на екран
    screen.fill(BLACK)
    screen.blit(player_image, [x, y])

# обновляємо екран
    pygame.display.flip()

    clock.tick(60)


pygame.quit()
