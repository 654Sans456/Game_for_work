import pygame

pygame.init()

x_win = 800
y_win = 600

win = pygame.display.set_mode((x_win, y_win))
win.fill((56, 56, 56))

pygame.display.set_caption(" -=+=- Сапёр -=+=- ")
pygame.display.set_icon(pygame.image.load("for_game/Game_Icon.png"))

run : bool = 1
while (run):
    
    
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = 0
        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                run = 0
    
    pygame.display.update()

pygame.quit()
