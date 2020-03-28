from abb import ArbolBinariodeBusqueda as abb
from cancion import Cancion

class ArbolDeCanciones(object):

    def __init__(self):
        'Inicializa el arbol para guardar las canciones'
        self.contenido = abb()

    def agregarLista(self,lista):
        'Recibe un archivo con una lista de canciones, crea objetos tipo cancion con los elementos y luego los añade al arbol'

        with open(ruta, 'r') as f:
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
        self.contenido._inOrderTrav(self.contenido.raiz)


    
help = ArbolDeCanciones()
# aiuda = Cancion('elriko','rikura','lazukulenzia')
# help.contenido.agregar(aiuda)
# hola = Cancion('elriko','gg','lazukulenzia')
# help.contenido.agregar(hola)
# help.mostrarLR()
# efe = Cancion('elriko','c1','lazukulenzia')
# help.contenido.agregar(efe)
# print(' ')
# why = Cancion('riquelme','c2','lazukulenzia')
# help.contenido.agregar(why)
# x = help.contenido.buscarCancion('elriko','rikura')
# print(x.data.ubicacion)
# help.mostrarLR()
# print('')
# help.eliminarCancion('elriko','gg')
ruta = 'C:/Users/RCGAM/Desktop/canciones/aiuda.txt'
help.agregarLista(ruta)
help.mostrarLR()