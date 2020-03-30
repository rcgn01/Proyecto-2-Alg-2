import pygame
from pygame.locals import *
from cancion import Cancion
from lr import ArbolDeCanciones
from reproductor import reproductor
import sys


#Definicion de los colores usando RGB.
NEGRO = (0,0,0)
BLANCO =(255,255,255)
GRIS = (169,169,169)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
MORADO = (100,70,150)

#Ancho y alto de botones y ventana
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 300
ANCHO_BOTON = SCREEN_WIDTH//6
ALTO_BOTON = SCREEN_HEIGHT//10

class Boton(object):
    'Clase que facilita la creacion de botones'

    def __init__(self, position, size, imagen):
        'Recibe la posicion, el tamaño y la imagen del boton que se desea crear'
        self.imagen = pygame.image.load(imagen)
        self.imagen = pygame.transform.scale(self.imagen,size)
        self.position = position
        self.size = size

        self._rect = self.imagen.get_rect()
        self._rect.topleft = self.position


    def dibujar(self, pantalla,event,accion=None):
        'Dibuja el boton. Si se hace click sobre el boton y se proporciona una accion a realizar, se realiza la accion'
        self._rect = self.imagen.get_rect()
        self._rect.topleft = self.position
        
        # Verifica si se hace click sobre el boton al dibujarlo
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Si se presiona el click izquierdo
                if self._rect.collidepoint(event.pos): #Si el cursor esta sobre le boton
                    pygame.draw.rect(pantalla, (190,190,190),(self.position,self.size))
                    pantalla.blit(self.imagen, self._rect)
                    if accion is not None:
                        #Se realiza la accion que se prporciono. Para cada accion posible se define una funcion mas abajo
                        #Acciones posibles: reproducir, pausar, detener, saltar cancion, mostrar lista ... 
                        if accion == 'pausar':
                            if rp.estaTocandoCancion():
                                rp.pause()
                            else:
                                rp.reproducir()
                        elif accion == 'saltar':
                            rp.sigCancion()
                        elif accion == 'detener':
                            rp.parar()
                        elif accion == 'agregar':
                            #Solicitar ruta del archivo
                            #reproductor.cargarCancion()
                            pass
                        elif accion == 'mostrarlista':
                            #Obtener la lista del reproductor y luego de alguna manera hacer que salga en la pantalla. Aqui tambien se hara la funcion eliminar
                            pass

        else:
            #En este caso no se ha hecho click sobre el boton
            pygame.draw.rect(pantalla, GRIS,(self.position,self.size))
            pantalla.blit(self.imagen, self._rect)

def ruta():
    'Pantalla inicial donde se pide al usuario suministrar la ruta al archivo txt con la informacion de las canciones a reproducir'

    screen = pygame.display.set_mode((700, 360))
    path = ""
    font = pygame.font.Font(None, 30)
    font1 = pygame.font.Font(None, 16)
    textsurf,textrect = objeto_texto('Introduzca la ruta al archivo txt con la informacion de las canciones a reproducir : '  , font1)
    textrect.center = ((3*SCREEN_WIDTH//4)-20,SCREEN_HEIGHT/4+(SCREEN_HEIGHT/6))

    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.key == K_BACKSPACE:
                    path = path[:-1]
                elif evt.key == K_RETURN: #Si se presiona enter
                    return path
                else:
                    path += evt.unicode
            elif evt.type == QUIT:
                sys.exit()
        screen.fill(GRIS)
        block = font.render(path, True, NEGRO)
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(textsurf,textrect)
        screen.blit(block, rect)
        pygame.display.flip()

def objeto_texto(texto, font):
    'Recibe un string con el texto que se quiere crear y la fuente a usar. Retorna una superficie con dicho texto'
    texto_surf = font.render(texto, True,NEGRO)
    return texto_surf, texto_surf.get_rect()

def dibujar_fondo(pantalla,imagen_fondo):
    'Funcion que escala el fondo al tamaño de la ventana y lo muestra'
    #Actualmente no la estamos usando pero la dejo por si le ponemos un fondo
    fondo = pygame.transform.scale(imagen_fondo,[SCREEN_WIDTH,SCREEN_HEIGHT])
    pantalla.blit(fondo,[20,20])

def main():
    'Bucle principal del reproductor'
    pygame.init() #Inicializacion pygame
    clock = pygame.time.Clock()
    texto = pygame.font.Font('freesansbold.ttf',10)


    path = ruta() #Se muestra la pantalla principal donde se pide la ruta al archivo txt
    rp = reproductor(str(path)) #Se crea el reproductor llamando al TAD reproductor

    pantalla = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #Creacion de la ventana del reproductor
    pygame.display.set_caption('Administrador de Música') #titulo de la ventana
    pantalla.fill(GRIS) #Se colorea el fondo de gris

    #Creacion de los botones usando la clase boton
    play_pausa = Boton((15,230),(ANCHO_BOTON,ALTO_BOTON+10),'C:/Users/RCGAM/OneDrive/Documentos/Ene Mar 20/Lab Alg2/Proyecto II/imagenes/pausa.png')
    cargar = Boton((300,230),(ANCHO_BOTON,ALTO_BOTON+10),'C:/Users/RCGAM/OneDrive/Documentos/Ene Mar 20/Lab Alg2/Proyecto II/imagenes/add1.png')
    detener = Boton((110,230),(ANCHO_BOTON,ALTO_BOTON+10),'C:/Users/RCGAM/OneDrive/Documentos/Ene Mar 20/Lab Alg2/Proyecto II/imagenes/detener.png')
    sig = Boton((205,230),(ANCHO_BOTON,ALTO_BOTON+10),'C:/Users/RCGAM/OneDrive/Documentos/Ene Mar 20/Lab Alg2/Proyecto II/imagenes/siguiente1.png')
    mostrarlr = Boton((400,230),(ANCHO_BOTON,ALTO_BOTON+10),'C:/Users/RCGAM/OneDrive/Documentos/Ene Mar 20/Lab Alg2/Proyecto II/imagenes/lista.png')

    #Creacion del cuadro donde se muestra la cancion que se esta reproduciendo
    cuadro = pygame.image.load('C:/Users/RCGAM/OneDrive/Documentos/Ene Mar 20/Lab Alg2/Proyecto II/imagenes/cuadro1.png')
    cuadro = pygame.transform.scale(cuadro,(300,130))
    cuadro_rect = cuadro.get_rect()
    cuadro_rect.center = (SCREEN_WIDTH/4+(SCREEN_WIDTH/4),(SCREEN_HEIGHT/4)+45)
    pantalla.blit(cuadro,cuadro_rect)


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
            #Se dibujan los botones y se verifica si se hace click sobre ellos
            play_pausa.dibujar(pantalla,event,'pausar')
            sig.dibujar(pantalla,event,'saltar')
            mostrarlr.dibujar(pantalla,event,'mostrarlista')
            detener.dibujar(pantalla,event,'detener')
            cargar.dibujar(pantalla,event,'agregar')

        #Se crea el texto que muestra la cancion que se esta reproduciendo y lo muestra
        pygame.draw.rect(pantalla,GRIS,(SCREEN_WIDTH/4,(SCREEN_HEIGHT/4)+10,SCREEN_WIDTH/2,(SCREEN_HEIGHT/4)-20))
        titulo = str(rp.actual.data.titulo)
        autor = str(rp.actual.data.interprete)
        if rp.estaTocandoCancion():
            info = 'Reproduciendo : ' +autor +', ' +titulo
        else:
            info = 'Reproductor pausado : ' +autor +', '+titulo
        textsurf,textrect = objeto_texto(info  , texto)
        textrect.center = ((SCREEN_WIDTH/4+(SCREEN_WIDTH/4),SCREEN_HEIGHT/4+(SCREEN_HEIGHT/6)))
        pantalla.blit(textsurf,textrect)

        #Actualizacion de pantalla
        pygame.display.update()
        clock.tick(15)

if __name__ == "__main__":
    main()



