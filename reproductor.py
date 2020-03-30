from lr import ArbolDeCanciones
from pygame import mixer


class reproductor(object):

    def __init__(self,canciones):
        'Recibe un txt con las canciones y crea la lista con ellas'
        self.lista = ArbolDeCanciones()
        self.lista.agregarLista(canciones)
        self.queue = self.lista.obtenerLR()
        self.actual = self.queue[0]
        # mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        # mixer.load(self.actual.ubicacion)
    
    def crearReproductor(self, cancion):
        pygame.mixer.music.load(cancion.ubicacion)
    
    def cargarCancion(self,cancion):
        self.lista.contenido.agregar(cancion)
        self.actual = cancion
        pygame.mixer.music.load(self.actual)
    
    def reproducir(self):
        mixer.music.play()

    def parar(self):
        pygame.mixer.music.stop()

    def pause(self):
        if self.estaTocandoCancion():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def estaTocandoCancion(self):
        try:
            if pygame.mixer.music.play() == True:
                return True 
            elif pygame.mixer.music.play() == False:
                return False
        except :
            return False
    
    
    def sigCancion(self):
        pygame.mixer.music.skip()
            

# pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
# rep = reproductor('C:/Users/RCGAM/Desktop/proyecto de mrd/canciones/aiuda.txt')
# rep.reproducir()