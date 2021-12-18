import pygame

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# This sets the name of the window
pygame.display.set_caption('Pica')

#обновляємо екран 
pygame.display.update()

player_image = pygame.image.load("pica_game").convert()#вказуємо шлях до нашого обєкта(зобарення)
player_image_height_half = player_image.get_height()
player_image_width_half = player_image.get_width()

#Якщо в зображення не має прозорого слою, то щоб його встановити,
#необхідно використати метод set_colorkey() класу Surface:
player_image.set_colorkey(BLACK)

done = False

pygame.mouse.set_visible(False)#прибираємо зображення курсора

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
    screen.fill(BLACK)  #затираєм слід       
                                       
# Get the current mouse position. This returns the position
    
#повертає поточну позицію мишки на екрані та обмежуємо область руху нашого обєкта
    player_position = pygame.mouse.get_pos() 
    x = player_position[0]
    y = player_position[1]
    if player_position[0]<player_image_width_half:
        x = player_image_width_half*0.1
    elif player_position[0]+player_image_width_half>pygame.display.get_window_size()[0]:
        x = pygame.display.get_window_size()[0]-player_image_width_half*1.1
    else:
        x = player_position[0]

    if player_position[1]<player_image_height_half:
        y = player_image_height_half*0.1
    elif player_position[1]+player_image_height_half>pygame.display.get_window_size()[1]:
        y = pygame.display.get_window_size()[1]-player_image_height_half*1.1
    else:
        y = player_position[1]        
           
#копіює картинку на екран
    screen.blit(player_image, [x, y])
  
#обновляємо екран
    pygame.display.flip()
 
pygame.quit()