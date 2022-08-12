# Importing the library
import pygame
  
# Initializing Pygame
pygame.init()
  
# Initializing surface
src = pygame.display.set_mode((400,400))
 
#Colors in use 
color = (255,0,0)
colorC= (107,40,138) #color Circulo
colorT= (40,50,138)  #color Triangulo

circle_x_y = (200, 200) #Pos X and Y, must be centered
circleR = 182 #circle Radius, we can modify as we want

backcolor= (255,255,255) #background color
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    src.fill(backcolor) #turning background white       
    pygame.draw.rect(src, color, pygame.Rect(0, 0, 400, 400),2)  #hasta aquí tenemos el cuadrado, no es lo suficientemente grande
    pygame.draw.circle(src, colorC, circle_x_y, circleR, 2)
    pygame.draw.polygon(src, colorT,[(200,20), (50,300), (350,300)], 2) #draw a triangle [(x1,y1),(x2,y2),(x3,y3)]
    pygame.display.flip() #displays
pygame.quit()



