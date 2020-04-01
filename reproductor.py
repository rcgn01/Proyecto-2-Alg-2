import pygame
from lr                 import ArbolDeCanciones
from pygame             import mixer


#Roberto Gamboa 16-10394
#Kevin Briceño 15-11661


#Clase que se encarga de manejar el ABB con las canciones para reproducirlas

class Reproductor(object):
    'Utiliza los elementos del ABB de la lista de reproduccion y los reproduce '

    def __init__(self,canciones):
        'Recibe un txt con las canciones y crea la lista con ellas'
        
        #Procesa la informacion de las canciones recibidas en el txt y las añade a la lista
        #reproduccion. Luego las añade a la libreria de musica

        assert(canciones!= None) #Precondicion

        self.lista = ArbolDeCanciones()
        self.lista.agregarLista(canciones)
        self.queue = []
        self.queue = self.lista.obtenerLR()
        self.actual = self.queue[0]
        self.numero = 1
        self.get_pos = 0
        self.pausa = False
        pygame.mixer.init()
        for i in self.queue:
            pygame.mixer.music.queue(i.data.ubicacion)
        
            
    def cargarCancion(self):
        'Añade una nueva cancion al reproductor'
        assert(True) #Precondicion
        self.actual = self.queue[0]
        pygame.mixer.music.load(self.actual.data.ubicacion)
    
    def reproducir(self):
        'Reproduce la cancion ya cargada'
        assert(True) #Precondicion
        pygame.mixer.music.play(0)

    def parar(self):
        'Detiene la reproduccion de la cancion'
        assert(True) #Precondicion
        pygame.mixer.music.stop()
        self.get_pos = 0

    def pause(self):
        'Pausa o reanuda la reproduccion de la cancion segun sea necesario'
        assert(True) #Precondicion
        pausar = self.pausa
        if pausar==False:
            pygame.mixer.music.pause()
            self.get_pos= self.get_pos + pygame.mixer.music.get_pos()
            self.pausa=True
        elif pausar==True:
            t = self.get_pos/1000
            pygame.mixer.music.play(start=t)
            self.pausa=False

    def estaTocandoCancion(self):
        'Indica si el reproductor esta tocando una cancion o no'
        assert(True) #Precondicion
        if pygame.mixer.music.get_busy() == True:
            return True 
        elif pygame.mixer.music.get_busy() == False:
            return False
    
    def sigCancion(self):
        'Salta a la siguiente cancion de la lista'
        assert(True) #Precondicion
        i = self.numero
        try:
            self.actual = self.queue[i]
            pygame.mixer.music.load(self.actual.data.ubicacion)
            i = i+1
            self.numero = i
        except:
            self.actual = None
        
            