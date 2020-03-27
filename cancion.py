
import os.path
from pathlib import Path



class Cancion(object):

    def __init__(self,titulo,interprete,ubicacion):
        'Recibe como entrada el titulo, interprete y ubicacion de la cancion. Si ninguno de estos datos es None y la ubicacion es valida, se crea el objeto de tipo cancion.'

        assert(titulo != None and interprete != None and self.es_ubicacion_valida(ubicacion)) #Precondicion

        self.titulo = str(titulo)
        self.interprete = str(interprete)
        self.ubicacion = str(ubicacion)
    
    def es_ubicacion_valida(self,u):
        'Verifica si la ubicacion dada existe en la computadora usando la libreria os.path de Python.'

        # try:
        #     assert(u != None) #Precondicion
        # except:
        #     return False
        # pass
        
        # return os.path.exists(u) 

        if '.mp3' or '.wav' in u:
            my_file = Path(u)
            return my_file.is_file()
        else:
            print('Formato de archivo no valido')
        
            
        

    def obtener_titulo(self):
        'Retorna el titulo de la cancion.'
        assert(True) #Precondicion
        x = self.titulo
        assert(x==self.titulo) #Poscondicion
        return x
    
    def obtener_interprete(self):
        'Retorna el interprete de la cancion.'
        assert(True) #Precondicion
        x = self.interprete
        assert(x==self.interprete) #Poscondicion
        return x
    
    def obtener_ubicacion(self):
        'Retorna la ubicacion de la cancion.'
        assert(True) #Precondicion
        x = self.ubicacion
        assert(x==self.ubicacion) #Poscondicion
        return x
    
    def aString(self):
        'Retorna un string con el titulo e interprete de la cancion en formato "titulo, interprete". '
        f = [self.titulo,self.interprete]
        x = ', '.join(f)
        return x

