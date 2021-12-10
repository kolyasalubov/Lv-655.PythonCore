import pygame

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# This sets the name of the window
pygame.display.set_caption('Fly')
 
clock = pygame.time.Clock()

#обновляємо екран 
pygame.display.update()
 
# Set positions of graphics
background_position = [0, 0]
 
# Load and set up graphics.
#background_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load("e:\!Python\SoftServ\Lv-655.PythonCore\HW8\\NRavlyk\Game\small4.png").convert()
player_image_height_half = player_image.get_height()/2
player_image_width_half = player_image.get_width()/2

#Якщо в зображення не має прозорого слою, то щоб його встановити,
#необхідно використати метод set_colorkey() класу Surface:
player_image.set_colorkey(BLACK)
 
done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True            
 
    
# Get the current mouse position. This returns the position
    # as a list of two numbers.
#повертає поточну позицію мишки на екрані
    player_position = pygame.mouse.get_pos()
    x,y = 0,0
    if player_position[0]<player_image_width_half:
        x = player_image_width_half
    elif player_position[0]+player_image_width_half>pygame.display.get_window_size()[0]:
        x = pygame.display.get_window_size()[0]-player_image_width_half
    else:
        x = player_position[0]

    if player_position[1]<player_image_height_half:
        y = player_image_height_half
    elif player_position[1]+player_image_height_half>pygame.display.get_window_size()[1]:
        y = pygame.display.get_window_size()[1]-player_image_height_half
    else:
        y = player_position[1]        
    
 
    # Copy image to screen:
#копіює картинку на екран
    screen.fill(BLACK)
    screen.blit(player_image, [x-player_image_width_half, y-player_image_height_half])
 
#обновляємо екран
    pygame.display.flip()
 
    clock.tick(60)


pygame.quit()