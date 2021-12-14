import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
IMAGE_WIDTH = 30
IMAGE_HEIGHT = 30

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Fly')
 
clock = pygame.time.Clock()

pygame.display.update()
background_position = [0, 0]
 
image = pygame.image.load("/Users/dyarovyi/Desktop/Python Core/Lv-655.PythonCore/HW8/dyarovyi/rocket.png").convert()
image = pygame.transform.scale(image, (IMAGE_WIDTH, IMAGE_HEIGHT))
image.set_colorkey(BLACK)
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False            
 
    cursor_position = pygame.mouse.get_pos()
    x = cursor_position[0]
    y = cursor_position[1]

    x = x if x < SCREEN_WIDTH - IMAGE_WIDTH else SCREEN_WIDTH - IMAGE_WIDTH
    y = y if y < SCREEN_HEIGHT - IMAGE_HEIGHT else SCREEN_HEIGHT - IMAGE_HEIGHT
 
    screen.fill(BLACK)
    screen.blit(image, [x, y])
 
    pygame.display.flip()
    clock.tick(60)