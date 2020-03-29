from lr import ArbolDeCanciones
import pygame
from pygame import mixer

class reproductor(object):

    def __init__(self,canciones):
        'Recibe un txt con las canciones y crea la lista con ellas'
        self.lista = ArbolDeCanciones()
        self.lista.agregarLista(canciones)
        self.queue = self.lista.obtenerLR()
        self.actual = self.queue[0]
        pygame.mixer.init()
        # for i in self.queue:
            # pygame.mixer.music.queue(i.data.ubicacion)
    
    def crearReproductor(self, cancion):
        pygame.mixer.music.load(cancion.ubicacion)
    
    def cargarCancion(self,cancion):
        self.lista.contenido.agregar(cancion)
        self.actual = cancion
        pygame.mixer.music.load(self.actual)
    
    def reproducir(self,ubicacion):
        pygame.mixer.music.play()

    def parar(self):
        pygame.mixer.music.stop()

    def pause(self):
        if self.estaTocandoCancion():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def estaTocandoCancion(self):
        if pygame.mixer.music.play() == True:
            return True 
        elif pygame.mixer.music.play() == False:
            return False
    
    def sigCancion(self):
        pygame.mixer.music.skip()
            
