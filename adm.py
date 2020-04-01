import os
import sys
import pygame
import tkinter as tk

from pygame.locals      import *
from cancion            import Cancion
from lr                 import ArbolDeCanciones
from reproductor        import Reproductor
from abb                import ArbolBinariodeBusqueda
from pygame             import mixer
from tkinter            import filedialog


#Roberto Gamboa 16-10394
#Kevin Briceño 15-11661


#Archivo donde se crea y se maneja toda la interfaz grafica usada por el administrador de musica

#Definicion de los colores usando RGB.
NEGRO = (0,0,0)
COLOR_FONDO = (67,179,174)

#Ancho y alto de botones y ventana
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 300
ANCHO_BOTON = SCREEN_WIDTH//6
ALTO_BOTON = SCREEN_HEIGHT//10

x = os.path.abspath('Prueba_interfaz.py')
y = os.path.dirname(x)
img_dir = y + '/imagenes/'


#Inicializacion de pygame
pygame.init()

#Creacion de las fuestes para los textos que se muestran en pantalla
texto = pygame.font.Font('pacifico.ttf',10)
texto_lista = pygame.font.Font('pacifico.ttf',13)
titulo_lista = pygame.font.Font('pacifico.ttf',15)
texto_titulo = pygame.font.Font('ostrich-regular.ttf',15)

# Entrada:
#	texto : string con el mensaje que se quiere mostrar en pantalla
#	font : fuente que usara el texto
def objeto_texto(texto, font):
    'Recibe un string con el texto que se quiere crear y la fuente a usar. Retorna una superficie con dicho texto'

    assert(font!= None and texto != None) #Precondicion

    texto_surf = font.render(texto, True,NEGRO)
    return texto_surf, texto_surf.get_rect()


# Entrada:
#	pantalla : ventana actual del administrador de musica
#   imagen_findo : ruta a la imagen que se usara como fondo
def dibujar_fondo(pantalla,imagen_fondo,SCREEN_WIDTH,SCREEN_HEIGHT):
    'Funcion que escala el la imagen del fondo al tamaño de la ventana y lo muestra'
    assert(True)
    fondo = pygame.image.load(imagen_fondo)
    fondo = pygame.transform.scale(fondo,[SCREEN_WIDTH,SCREEN_HEIGHT])
    pantalla.blit(fondo,[0,0])

def ruta():

    clock = pygame.time.Clock()

    'Pantalla inicial donde se pide al usuario suministrar la ruta al archivo txt con la informacion de las canciones a reproducir'
    screen = pygame.display.set_mode((700, 200))
    pygame.display.set_caption('Administrador de Música - Carga de archivo') #titulo de la ventana
    icono = pygame.image.load(img_dir+'icono.png')
    pygame.display.set_icon(icono) #Icono de ventana
    screen.fill(COLOR_FONDO) #Se colorea el fondo
    dibujar_fondo(screen,img_dir+'fondo1.png',700,200)
    textsurf,textrect = objeto_texto('Presione cualquier tecla para seleccionar el archivo txt con la informacion de las canciones a reproducir '  , texto_lista)
    textrect.center = ((3*SCREEN_WIDTH//4)-20,SCREEN_HEIGHT/4)
    screen.blit(textsurf,textrect)
    pygame.display.flip()

    while True:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                sys.exit()
            
            if evt.type == KEYDOWN:
                return obtener_archivo()
    
    pygame.display.update()
    clock.tick(60)

def obtener_archivo():
    'Abre un ventana de dialogo donde se le solicita al usuario que seleccione el archivo .txt con la informacion de las canciones'
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

#Se muestra la pantalla principal donde se pide la ruta al archivo txt.
try:
    path = ruta()
    reproductor = Reproductor(str(path)) #Se crea el reproductor llamando al TAD reproductor
    reproductor.cargarCancion() #Se añade a la libreria de musica las canciones de la LR
except:
    print('El archivo no contiene la informacion sobre canciones correcta. Por favor intente de nuevo')


class Boton(object):
        'Clase que facilita la creacion de botones'

        # Entrada:
        #	self : boton actual
        #	position: posicion en la pantalla donde se mostrara en boton, debe ser una tupla en forma (x,y)
        #   size : tamaño del boton
        #   imagen : ruta al icono del boton

        def __init__(self, position, size, imagen):
            'Recibe la posicion, el tamaño y la imagen del boton que se desea crear'

            assert(position != None and size != None and imagen != None) #Precondicion

            self.imagen = pygame.image.load(imagen)
            self.imagen = pygame.transform.scale(self.imagen,size)
            self.position = position
            self.size = size
            self.click = False
            self.eliminar = False
            self.salir = False

            # self._rect = pygame.Rect(position,size)
            self._rect = self.imagen.get_rect()
            self._rect.topleft = self.position

        # Entrada:
        #	self : boton actual
        #	event: evento actual
        def manejar_evento(self,event):
            'Funcion que verifica usando los eventos de pygame si se ha hecho click en el boton'
            
            #Se almacena en una variable booleana si se ha hecho click sobre el boton y en la funcion dibujar se realiza la accion de el boton

            assert(True)#Precondicion

            mouse = pygame.mouse.get_pos()
            if self.position[0]+self.size[0] > mouse[0] > self.position[0] and self.position[1]+self.size[1] > mouse[1] > self.position[1] and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.click = True
                self.eliminar = True
                self.salir = True
        
        # Entrada:
        #	self : boton actual
        #	pantalla: ventana del reproductor
        #   accion : accion que se desea realizar al presionar el boton
        def dibujar(self, pantalla,accion=None):
            'Dibuja el boton. Si se hace click sobre el boton y se proporciona una accion a realizar, se realiza la accion'
            
            assert(pantalla!=None) #Precondicion

            if self.click: # is some button clicked
                self.click = False
                #pygame.draw.rect(pantalla, (190,190,190),(self.position,self.size))
                pantalla.blit(self.imagen, self._rect)
                if accion is not None:
                    #Se realiza la accion que se prporciono. Para cada accion posible se define una funcion mas abajo
                    #Acciones posibles: reproducir, pausar, detener, saltar cancion, mostrar lista ... 
                    if accion == 'pausar':
                        if pygame.mixer.music.get_busy()== False:
                            reproductor.reproducir()
                        elif pygame.mixer.music.get_busy()== True:
                            reproductor.pause()
                    elif accion == 'saltar':
                        reproductor.sigCancion()
                    elif accion == 'detener':
                        reproductor.parar()
                    elif accion == 'agregar':
                        try:
                            archive = obtener_archivo()
                            reproductor.lista.agregarLista(archive)
                            print(reproductor.lista.mostrarLR())
                            reproductor.queue = reproductor.lista.obtenerLR()
                            reproductor.cargarCancion()
                        except:
                            pass
                    elif accion == 'mostrarlista':
                            mostrar_lista(pantalla,reproductor,reproductor.lista.obtenerLR())
                    elif accion == 'eliminar':
                        pass
            else:
                self._rect = self.imagen.get_rect()
                self._rect.topleft = self.position
                #pygame.draw.rect(pantalla, GRIS,(self.position,self.size))
                pantalla.blit(self.imagen, self._rect)

class Lista(object):
    'Clase que recibe la lista de reproduccion y creo botones y texto para cada elemento'

    # Entrada:
    #	self : lista actual
    #	lista: lista con la informacion de las canciones
    #   pantalla : ventana del reproductor
    def __init__(self,lista,pantalla):
        'Inicializa el objeto tipo lista '
        self.lista = lista
        self.pantalla = pantalla
        self.textos = self.agregar_textos()
        self.botones = self.agregar_botones()

    # Entrada:
    #	self : lista actual
    def agregar_textos(self):
        'Crea los textos con los titulos e interpretes de cada cancion en la lista y los guarda en un arreglo para luego mostrarlos en pantalla'
        assert(True) #Precondicion
        self.textos = []
        i = 45
        for j in self.lista:
            #pygame.draw.rect(self.pantalla,BLANCO,(SCREEN_WIDTH/4,(SCREEN_HEIGHT/4)+10,SCREEN_WIDTH/2, (SCREEN_HEIGHT/4)+20 ))
            titulo = str(j.data.titulo)
            autor = str(j.data.interprete)
            info = autor +', ' +titulo +'.'
            textsurf,textrect = objeto_texto(info  , texto_lista)
            textrect.topleft = (520,i)
            self.textos.append((textsurf,textrect)) #se añaden las superficies a un arreglo.
            i += 40
        return self.textos
    
    # Entrada:
    #	self : lista actual
    def agregar_botones(self):
        'Crea los botones para eliminar cada cancion de la lista'
        assert(True)
        self.botones = []
        i = 45
        for j in range(len(self.textos)):
            x = Boton((750,i),(25,25),img_dir+'eliminar.png')
            self.botones.append(x)
            i += 40
        return self.botones

    # Entrada:
    #	self : lista actual
    def dibujar_lista(self,pantalla):
        'Junta los botones y textos creados para mostrarlos en pantalla'
        assert(True)
        textsurf,textrect = objeto_texto('Lista de Reproducción (Interprete, Titulo)'  , titulo_lista)
        textrect.topleft = (520,5)
        pantalla.blit(textsurf,textrect)
        for j in range(len(self.lista)):
            pantalla.blit(self.textos[j][0],self.textos[j][1])
            self.botones[j].dibujar(pantalla,'eliminar')


# Entrada:
#	pantalla : ventana actual del administrador de musica
#   reproductor : reproductor actual
#   lista : lista con los elementos de la LR
def mostrar_lista(pantalla,reproductor,lista):
    'Recibe la lista generada por queue y la muestra en pantalla ayudandose de la clase Lista'

    #Es practicamente otra funcion main pero amplia la ventana y muestra la lista de reproduccion a un lado 

    clock = pygame.time.Clock()
    icono = pygame.image.load(img_dir+'icono.png')
    pantalla = pygame.display.set_mode((SCREEN_WIDTH+300,SCREEN_HEIGHT)) #Creacion de la ventana del reproductor
    pygame.display.set_caption('Administrador de Música') #titulo de la ventana
    pygame.display.set_icon(icono) #Icono de ventana
    pantalla.fill(COLOR_FONDO) #Se colorea el fondo de gris
    dibujar_fondo(pantalla,img_dir+'fondo1.png',SCREEN_WIDTH+300,SCREEN_HEIGHT)

    ayuda = Lista(reproductor.queue,pantalla)
    ayuda.dibujar_lista(pantalla)

    #Creacion de los botones
    play_pausa = Boton((15,230),(ANCHO_BOTON,ALTO_BOTON+10),img_dir+'play.png')
    cargar = Boton((300,230),(ANCHO_BOTON,ALTO_BOTON+10),img_dir+'agregar1.png')
    detener = Boton((110,230),(ANCHO_BOTON,ALTO_BOTON+10),img_dir+'parar.png')
    sig = Boton((205,230),(ANCHO_BOTON,ALTO_BOTON+10),img_dir+'sig.png')
    mostrarlr = Boton((400,230),(ANCHO_BOTON,ALTO_BOTON+10),img_dir+'lista1.png')

    #Creacion del cuadro donde se muestra la cancion que se esta reproduciendo
    cuadro = pygame.image.load(img_dir+'cuadro1.png')
    cuadro = pygame.transform.scale(cuadro,(300,130))
    cuadro_rect = cuadro.get_rect()
    cuadro_rect.center = (SCREEN_WIDTH/4+(SCREEN_WIDTH/4),(SCREEN_HEIGHT/4)+45)
    pantalla.blit(cuadro,cuadro_rect)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            #Verifica si alguno de los botones para eliminar canciones se ha clickeado
            for j in ayuda.botones:
                j.manejar_evento(event)
            
            #Verifica si se ha clickeado sobre alguno de los botones
            play_pausa.manejar_evento(event)
            sig.manejar_evento(event)
            mostrarlr.manejar_evento(event)
            detener.manejar_evento(event)
            cargar.manejar_evento(event)

            #Si se hace click al boton para mostrar la lista cuando la lista ya esta desplegada, la oculta
            if mostrarlr.salir:
                return main(500,300)
        
        #Se crea el texto que muestra la cancion que se esta reproduciendo y se pone en pantalla
        if reproductor.actual is not None:
            titulo = str(reproductor.actual.data.titulo)
            autor = str(reproductor.actual.data.interprete)
            if reproductor.estaTocandoCancion():
                info = 'Reproduciendo : ' +autor +', ' +titulo
            else:
                info = 'Reproductor pausado : ' +autor +', '+titulo
        else:
            info = 'No hay ninguna cancion cargada en el reproductor'
        textsurf,textrect = objeto_texto(info  , texto_titulo)
        textrect.center = (((SCREEN_WIDTH/2) -len(info)/3,SCREEN_HEIGHT/4+(SCREEN_HEIGHT/6)))
        pantalla.blit(textsurf,textrect)

    
        #Se dibujan los botones y se verifica si se hace click sobre ellos
        play_pausa.dibujar(pantalla,'pausar')
        sig.dibujar(pantalla,'saltar')
        mostrarlr.dibujar(pantalla,'mostrarlista')
        detener.dibujar(pantalla,'detener')
        cargar.dibujar(pantalla,'agregar')
        for j in range(len(ayuda.botones)):
            ayuda.botones[j].dibujar(pantalla,'eliminar')
            if ayuda.botones[j].eliminar:
                ayuda.botones[j].eliminar = False
                reproductor.lista.eliminarCancion(ayuda.lista[j].data.interprete,ayuda.lista[j].data.titulo)
                reproductor.queue.remove(reproductor.queue[j])
                try:
                    reproductor.actual = reproductor.queue[0]
                except:
                    reproductor.actual = None
                dibujar_fondo(pantalla,img_dir+'fondo1.png',SCREEN_WIDTH+300,SCREEN_HEIGHT)
                pantalla.blit(cuadro,cuadro_rect)
                ayuda = Lista(reproductor.queue,pantalla)
                ayuda.dibujar_lista(pantalla)
                break

        #Actualizacion de pantalla
        pygame.display.update()
        clock.tick(60)


def main(SCREEN_WIDTH,SCREEN_HEIGHT):
    
    'Bucle principal del reproductor'
    
    clock = pygame.time.Clock()
    
    icono = pygame.image.load(img_dir+'icono.png')
    pantalla = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #Creacion de la ventana del reproductor
    pygame.display.set_caption('Administrador de Música') #titulo de la ventana
    pygame.display.set_icon(icono) #Icono de ventana
    pantalla.fill(COLOR_FONDO) #Se colorea el fondo de gris
    dibujar_fondo(pantalla,img_dir+'fondo1.png',SCREEN_WIDTH,SCREEN_HEIGHT)
    

    #Creacion de los botones usando la clase boton
    play_pausa = Boton((15,230),(ANCHO_BOTON,ALTO_BOTON+10),img_dir+'play.png')
    cargar = Boton((300,230),(ANCHO_BOTON,ALTO_BOTON+10),img_dir+'agregar1.png')
    detener = Boton((110,230),(ANCHO_BOTON,ALTO_BOTON+10),img_dir+'parar.png')
    sig = Boton((205,230),(ANCHO_BOTON,ALTO_BOTON+10),img_dir+'sig.png')
    mostrarlr = Boton((400,230),(ANCHO_BOTON,ALTO_BOTON+10),img_dir+'lista1.png')

    #Creacion del cuadro donde se muestra la cancion que se esta reproduciendo
    cuadro = pygame.image.load(img_dir+'cuadro1.png')
    cuadro = pygame.transform.scale(cuadro,(300,130))
    cuadro_rect = cuadro.get_rect()
    cuadro_rect.center = (SCREEN_WIDTH/4+(SCREEN_WIDTH/4),(SCREEN_HEIGHT/4)+45)
    pantalla.blit(cuadro,cuadro_rect)
    status = True
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif status:
                play_pausa.manejar_evento(event)
                sig.manejar_evento(event)
                mostrarlr.manejar_evento(event)
                detener.manejar_evento(event)
                cargar.manejar_evento(event)

                #Se crea el texto que muestra la cancion que se esta reproduciendo y se pone en pantalla
                if reproductor.actual is not None:
                    titulo = str(reproductor.actual.data.titulo)
                    autor = str(reproductor.actual.data.interprete)
                    if reproductor.estaTocandoCancion():
                        info =  autor +', ' +titulo
                        head = 'Reproduciendo : '
                    else:
                        head = 'Reproductor pausado : '
                        info = autor +', '+titulo
                else:
                    info = 'No hay ninguna cancion cargada en el reproductor'
                textsurf,textrect = objeto_texto(info  , texto_titulo)
                textrect.center = (((SCREEN_WIDTH/2) -len(info)/3,SCREEN_HEIGHT/4+(SCREEN_HEIGHT/6)))
                pantalla.blit(textsurf,textrect)
                
                textsurf,textrect = objeto_texto(head  , texto_titulo)
                textrect.center = (((SCREEN_WIDTH/2),SCREEN_HEIGHT/4+(SCREEN_HEIGHT/6) -20))
                pantalla.blit(textsurf,textrect)

        #Se dibujan los botones y se verifica si se hace click sobre ellos
        play_pausa.dibujar(pantalla,'pausar')
        sig.dibujar(pantalla,'saltar')
        mostrarlr.dibujar(pantalla,'mostrarlista')
        detener.dibujar(pantalla,'detener')
        cargar.dibujar(pantalla,'agregar')
        #Actualizacion de pantalla
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main(SCREEN_WIDTH,SCREEN_HEIGHT)