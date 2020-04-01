from cancion import Cancion

#Roberto Gamboa 16-10394
#Kevin Briceño 15-11661


class Nodo(object):
    'Clase donde se almacenan las canciones para luego ser añadidas al arbol binario de busqueda'

    # Entrada:
    #	cancion: cancion a almacenar. Debe ser un objeto tipo cancion

    def __init__(self,cancion):
        'Crea un nodo con objetos tipo Cancion'
        self.left = None
        self.right = None
        self.parent = None
        self.data = cancion

class ArbolBinariodeBusqueda(object):

    'Arbol Binario de Busqueda para almacenar y hacer operaciones sobre las canciones'

    def __init__(self):
        self.raiz = None
        self.elems = 0

    # Entrada:
    #	self : ABB actual
    #	cancion : cancion a agregar al ABB
    def agregar(self,cancion):
        'Agrega el nuevo objeto tipo cancion al arbol comparando las claves por orden lexicografico'

        assert(cancion!=None) #Precondicion

        y = None
        x = self.raiz

        while x is not None:
            y = x
            if cancion.interprete != x.data.interprete:
                if cancion.interprete < x.data.interprete:
                    x = x.left
                else:
                    x = x.right
            elif cancion.interprete == x.data.interprete:
                if cancion.titulo < x.data.titulo:
                    x = x.left
                else:
                    x = x.right
        
        cancion = Nodo(cancion)
        cancion.parent = y

        if y is None:
            self.raiz = cancion
        elif cancion.data.interprete != y.data.interprete:
                if cancion.data.interprete < y.data.interprete:
                   y.left = cancion
                else:
                    y.right = cancion
        elif cancion.data.interprete == y.data.interprete:
            if cancion.data.titulo < y.data.titulo:
                y.left = cancion
            else:
                y.right = cancion
        
        self.elems += 1

    def _inOrderTrav(self, subTree,arreglo=[]):
        assert(True) #Precondicion
        if subTree is not None :
            self._inOrderTrav(subTree.left,arreglo)
            print("[{0}:{1}] ".format(subTree.data.interprete, subTree.data.titulo))
            arreglo.append(subTree)
            self._inOrderTrav(subTree.right,arreglo)
        return arreglo
   

    # Entrada:
    #	self : ABB actual
    #	interprete: interprete de la cancion a eliminar
    #   titulo : titulo de la cancion a eliminar
    def eliminarCancion(self,interprete,titulo):
        'Recibe el interprete y titulo de la cancion a eliminar'

        assert(interprete!=None and titulo != None) #Precondicion

        z = self.buscarCancion(interprete,titulo)

        if z is None:
            print('La cancion no se encuentra en la lista')
            return

        if z.left is None or z.right is None:
            y = z
        else:
            y = self.sucesor(z)
        
        if y.left is not None:
            x = y.left
        else:
            x = y.right
        
        if x is not None:
            x.parent = y.parent
        
        if y.parent is None:
            self.raiz = x
        else:
            if y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x
        
        if y != z:
            z.data = y.data
            y = None
        
        self.elems -= 1
    
    # Entrada:
    #	self : ABB actual
    #	interprete: interprete de la cancion a buscar
    #   titulo : titulo de la cancion a buscar 
    def buscarCancion(self,interprete,titulo):
        'Busca una cancion por interprete y titulo y devuelve un apuntador a la cancion. Se usa en la funcion eliminarCancion'

        assert(interprete != None and titulo != None) #Precondicion

        x = self.raiz

        while x is not None and interprete != x.data.interprete and titulo != x.data.titulo:    
            if interprete != x.data.interprete:
                if interprete < x.data.interprete:
                    x = x.left
                else:
                    x = x.right
            elif interprete == x.data.interprete:
                if titulo < x.data.titulo:
                    x = x.left
                else:
                    x = x.right

        if x.left is not None:
            if x.left.data.titulo == titulo:
                x = x.left
        if x.right is not None:
            if x.right.data.titulo == titulo:
                x = x.right

        assert(x == None or (x.data.titulo == titulo and x.data.interprete == interprete)) #Postcondicion

        return x
    
    # Entrada:
    #	self : ABB actual
    #	subTree: nodo que se esta visitando actualmente
    #   arreglo : arreglo donde se almacenan los elementos del ABB
    def guardar_inorder(self,subTree,arreglo = []):
        'Realiza el recorrido in orden del arbol pero en vez de imprimir los nodos los guarda en un arreglo'
        assert(True) #Precondicion
        if subTree is not None:
            self.guardar_inorder(subTree.left,arreglo)
            if all(arreglo[j].data.ubicacion != subTree.data.ubicacion for j in range(len(arreglo)) ):
                arreglo.append(subTree)
            else:
                pass
            self.guardar_inorder(subTree.right,arreglo)
        return arreglo
    
    # Entrada:
    #	self : ABB actual
    #	x : nodo al que se le desea encontrar el sucesor
    def sucesor(self,x):
        'Devuelve el sucesor de x'

        assert(x!= None) #Precondicion

        #Cuando el nodo tiene un subarbol derecho
        if x.right is not None:
            x = x.right
            while x.left is not None:
                x = x.left
            return x
        
        #Cuando el nodo no tiene subarbol derecho
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y

    # Entrada:
    #	self : ABB actual
    def minimo(self):
        'Retorna el elemento con la menor clave en el  ABB'
        assert(True) #Precondicion
        x = self.raiz
        while x.left is not None:
            x = x.left
        return x
    
    # Entrada:
    #	self : ABB actual
    def maximo(self):
        'Retorna el elemento con la mayor clave en el ABB'
        assert(True) #Precondicion
        x = self.raiz
        while x.right is not None:
            x = x.right
        return x