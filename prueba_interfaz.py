import pygame
from pygame.locals import *
from cancion import Cancion
from lr import ArbolDeCanciones
from reproductor import reproductor
import sys

reproductor = reproductor('C:/Users/RCGAM/Desktop/canciones/aiuda.txt')


NEGRO = (0,0,0)
BLANCO =(255,255,255)
GRIS = (169,169,169)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
MORADO = (100,70,150)
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 300

ANCHO_BOTON = SCREEN_WIDTH//6
ALTO_BOTON = SCREEN_HEIGHT//10

x_boton , y_boton = (SCREEN_WIDTH * 0.2), 3*SCREEN_HEIGHT//4

def mostrar_texto(texto,x,y,fuente):
    TextSurf, TextRect = text_objects(texto, fuente)
    TextRect.center = ((x//2),(y//2))
    pantalla.blit(TextSurf, TextRect)
    pygame.display.update()
    # time.sleep(2)

def lista():

    ventana = pygame.display.set_mode((200,200))
    pygame.display.set_caption('Lista de reproducción')

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def text_objects(text, font):
    textSurface = font.render(text, True, (200,0,0))
    return textSurface, textSurface.get_rect()

def dibujar_fondo():
    fondo = pygame.transform.scale(imagen_fondo,[SCREEN_WIDTH,SCREEN_HEIGHT])
    pantalla.blit(fondo,[20,20])

def dibujar_boton(texto,x,y,ancho,alto,ic,ac,accion = None):
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+ancho > mouse[0] > x and y+alto > mouse[1] > y:
        pygame.draw.rect(pantalla, ac,(x,y,ancho,alto))
        if click[0] == 1 and accion != None:
                accion()

            
    else:
        pygame.draw.rect(pantalla, ic,(x,y,ancho,alto))
    
    smallText = pygame.font.Font("freesansbold.ttf",10)
    textSurf, textRect = text_objects(texto, smallText)
    textRect.center = ( (x+(ancho/2)), (y+(alto/2)) )
    pantalla.blit(textSurf, textRect)

def main():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        pygame.draw.rect(pantalla,MORADO,(SCREEN_WIDTH/4,SCREEN_HEIGHT/4,SCREEN_WIDTH/2,SCREEN_HEIGHT/3))
        texto = pygame.font.Font('freesansbold.ttf',30)
        fuente2 = pygame.font.Font('freesansbold.ttf',10)
        titulo = str(reproductor.actual.data.titulo)
        autor = str(reproductor.actual.data.interprete)
        info = 'Reproduciendo : ' +autor +', ' +titulo
        textsurf,textrect = text_objects(info  , fuente2)
        textrect.center = ((SCREEN_WIDTH/4+(SCREEN_WIDTH/4),SCREEN_HEIGHT/4+(SCREEN_HEIGHT/6)))
        pantalla.blit(textsurf,textrect)
        
        dibujar_boton('Pausa',x_boton,y_boton,ANCHO_BOTON,ALTO_BOTON,MORADO,AZUL)
        dibujar_boton('MostrarLR',x_boton*2,y_boton,ANCHO_BOTON,ALTO_BOTON,MORADO,AZUL)
        dibujar_boton('Sig. Cancion',3*x_boton,y_boton,ANCHO_BOTON,ALTO_BOTON,MORADO,AZUL)
        dibujar_boton('Agregar Lista',4*x_boton,y_boton,ANCHO_BOTON,ALTO_BOTON,MORADO,AZUL)

        pygame.display.update()
        clock.tick(15)

pygame.init()
pantalla = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Administrador de Música')
pantalla.fill(GRIS)
# imagen_fondo = pygame.image.load('')
# imagen_boton = pygame.image.load("../img/button.png")
# imagen_boton_pressed = pygame.image.load("../img/buttonPressed.png")
clock = pygame.time.Clock()

if __name__ == "__main__":
    main()



