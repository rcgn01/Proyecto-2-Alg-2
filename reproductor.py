from lr import ArbolDeCanciones
from pygame import mixer

class reproductor(object):

    def __init__(self,canciones):
        'Recibe un txt con las canciones y crea la lista con ellas'
        self.lista = ArbolDeCanciones()
        self.lista.agregarLista(canciones)
        self.actual = self.lista.contenido.raiz
    
    def cargarCancion(self,cancion):
        self.lista.contenido.agregar(cancion)
        self.actual = cancion
    
    def reproducir(self):
        pass

    def parar(self):
        pass

    def pause(self):
        if self.estaTocandoCancion:
            pass
        else:
            pass

    def estaTocandoCancion(self):
        pass
