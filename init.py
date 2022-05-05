import pygame
import sys

pygame.init()

w = 500
h = 400

ventana = pygame.display.set_mode( (w,h) )
pygame.display.set_caption("hola mundo")
rect = pygame.Rect(100, 100, 120, 30)

while True:
    ventana.fill( (51,193,255) )
    pygame.draw.rect(ventana, (141,51,255), rect )
    pygame.display.update() 
    tecla = pygame.key.get_pressed()

    if rect.x < 0:
        rect.x = 0
    
    if rect.y < 0:
        rect.y = 0
    
    if rect.y > w:
        rect.y = w 
    
    if rect.x > h:
        rect.x = h  
    
    if tecla[pygame.K_a]:
        rect.x = rect.x -1    
    
    if tecla[pygame.K_d]:
        rect.x = rect.x +1     
    
    if tecla[pygame.K_w]:
        rect.y = rect.y -1      
    
    if tecla[pygame.K_s]:
        rect.y = rect.y +1   
    
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

 