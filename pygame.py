import pygame.display
import pygame.sprite
import pygame 
pygame.init()
screen = pygame.display.set_mode((600,300))
rinning = True 
while True:
    screen.fill((114,157,224))
    pygame.displai.update()
    for event in pygame.event.get():
        if event.tupe == pygame.QIUT:
            rinning = False
            pygame.quit()
        elif event.type == pygame.KETDOWN:
            if event.key == pygame.K_a:
                screen.fill(78,44,133)
    
    