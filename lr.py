from abb import ArbolBinariodeBusqueda as abb
from cancion import Cancion

class ArbolDeCanciones(object):

    def __init__(self):
        'Inicializa el arbol para guardar las canciones'
        self.contenido = abb()

    def agregarLista(self,lista):
        'Recibe un archivo con una lista de canciones, crea objetos tipo cancion con los elementos y luego los añade al arbol'

        with open(lista, 'r') as f:
            for i in f:
                C_info=i.split('\t')
                C_info[-1]=C_info[-1].strip()
                if '.mp3' or '.wav' in C_info[2]:
                    cancion=Cancion(C_info[0], C_info[1], C_info[2])
                    self.contenido.agregar(cancion)
                else:
                    print( '\nAlgunas canciones no se han podido importar. Las canciones deben estar en formato mp3 o wav')
        f.closed


    def eliminarCancion(self,interprete,titulo):
        'Recibe el interprete y titulo de la cancion a eliminar'
        self.contenido.eliminarCancion(interprete,titulo)

    def obtenerLR(self):
        '??????'
        pass

    def mostrarLR(self):
        'Hacer recorrido in - order para imprimir el arbol ##'
        j = []
        self.contenido.in_order(self.contenido.raiz)
        print(*j)


    
