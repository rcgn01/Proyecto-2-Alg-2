import os
import os.path

#Roberto Gamboa 16-10394
#Kevin Briceño 15-11661


class Cancion(object):
    'Clase que almacena toda la informacion de las canciones a reproducir'

    # Entrada:
    #	titulo: titulo de la cancion 
    #	interprete: interprete de la cancion
    #	ubicacion: Ruta al archivo de musica de formato mp3 o wav.
    def __init__(self,interprete,titulo,ubicacion):
        'Recibe como entrada el titulo, interprete y ubicacion de la cancion. Si ninguno de estos datos es None y la ubicacion es valida, se crea el objeto de tipo cancion.'

        assert(titulo != None and interprete != None and self.es_ubicacion_valida(ubicacion)) #Precondicion

        self.titulo = str(titulo)
        self.interprete = str(interprete)
        self.ubicacion = str(ubicacion)

        assert(self.titulo == titulo and self.ubicacion == ubicacion and self.interprete == interprete) #Postcondicion
    
    # Entrada:
    #	self : cancion que se esta usando
    #	ubicacion: Ruta al archivo de musica de formato mp3 o wav.
    def es_ubicacion_valida(self, ubicacion):
        'Verifica si la ubicacion dada existe en la computadora usando la libreria os.path de Python. Luego verifica que la'

        assert(ubicacion != None) #Precondicion

        if os.path.exists(ubicacion):
            archivo, ext= os.path.splitext(ubicacion)
            if ext == str(".mp3") or ext == str(".wav"):
                return True
            else:
                return False
        else:
            return False

    # Entrada:
    #	self : cancion que se esta usando
    def obtener_titulo(self):
        'Retorna el titulo de la cancion.'
        assert(True) #Precondicion
        x = self.titulo
        assert(x==self.titulo) #Poscondicion
        return x
    
    # Entrada:
    #	self : cancion que se esta usando
    def obtener_interprete(self):
        'Retorna el interprete de la cancion.'
        assert(True) #Precondicion
        x = self.interprete
        assert(x==self.interprete) #Poscondicion
        return x
    
    # Entrada:
    #	self : cancion que se esta usando
    def obtener_ubicacion(self):
        'Retorna la ubicacion de la cancion.'
        assert(True) #Precondicion
        x = self.ubicacion
        assert(x==self.ubicacion) #Poscondicion
        return x
    
    # Entrada:
    #	self : cancion que se esta usando
    def aString(self):
        'Retorna un string con el titulo e interprete de la cancion en formato "titulo, interprete". '
        assert(True) #Precondicion
        f = [self.titulo,self.interprete]
        x = ', '.join(f)
        assert( x == self.titulo + ', '+self.interprete)
        return x


