from abb         import ArbolBinariodeBusqueda as abb
from cancion     import Cancion

#Roberto Gamboa 16-10394
#Kevin Briceño 15-11661

#Clase arbol de cancion que se apoya de un ABB para almacenar canciones en sus nodos

class ArbolDeCanciones(object):

    def __init__(self):
        'Inicializa el arbol para guardar las canciones'
        self.contenido = abb()


    # Entrada:
    #	self : LR actual
    #	lista : archivo txt donde se encuentra la informacion de las canciones a guardar en la LR
    def agregarLista(self,lista):
        'Recibe un archivo con una lista de canciones, crea objetos tipo cancion con los elementos y luego los añade al arbol'

        #Abre el archivo txt y procesa la informacion dentro de éste
        with open(lista, 'r') as f:
            for i in f:
                C_info=i.split('\t')
                C_info[-1]=C_info[-1].strip()
                info = []
                i = 0
                j = 0
                while i != len(C_info[0]):
                    if C_info[0][i] == ';' or i == len(C_info[0]) - 1:
                        if i == len(C_info[0]) - 1:
                            info.append(C_info[0][j:i+1])
                            break
                        info.append(C_info[0][j:i])
                        j = i + 1
                    i += 1
                if '.mp3' or '.wav' in info[2]:
                    cancion=Cancion(info[0], info[1], info[2])
                    self.contenido.agregar(cancion)
                else:
                    print( '\nAlguna de las canciones no tiene la extension requerida. Las canciones deben estar en formato mp3 o wav')
            f.closed

    # Entrada:
    #	self : LR actual
    #	interprete: interprete de la cancion a eliminar
    #   titulo : titulo de la cancion a eliminar
    def eliminarCancion(self,interprete,titulo):
        'Recibe el interprete y titulo de la cancion a eliminar'
        assert(True) #Precondicion
        self.contenido.eliminarCancion(interprete,titulo)

    # Entrada:
    #	self : LR actual
    def obtenerLR(self):
        'Obtiene los elementos de la LR y los guarda en un arreglo'
        assert(True) #Precondicion
        x = self.contenido.guardar_inorder(self.contenido.raiz)
        return x

    # Entrada:
    #	self : LR actual
    def mostrarLR(self):
        'Realiza el recorrida in - order del arbol de canciones y muestra sus elementos'
        assert(True) #Precondicion
        self.contenido._inOrderTrav(self.contenido.raiz)
