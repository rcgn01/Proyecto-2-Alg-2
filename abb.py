from cancion import Cancion

class Nodo(object):
    def __init__(self,cancion):
        'Crea un nodo con objetos tipo Cancion'
        self.left = None
        self.right = None
        self.parent = None
        self.data = cancion

class ArbolBinariodeBusqueda(object):

    def __init__(self):
        self.raiz = None
        self.elems = 0

    def agregar(self,cancion):
        'Agrega el nuevo objeto tipo cancion al arbol comparando las claves por orden lexicografico'
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

    def _inOrderTrav(self, subTree):
        if subTree is not None :
            self._inOrderTrav(subTree.left)
            print("[{0}:{1}] ".format(subTree.data.interprete, subTree.data.titulo))
            self._inOrderTrav(subTree.right)
   
    def eliminarCancion(self,interprete,titulo):
        'Recibe el interprete y titulo de la cancion a eliminar'

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
        
        if y != z:
            z.data = y.data
        
        self.elems -= 1
    
    def buscarCancion(self,interprete,titulo):
        'Busca una cancion por interprete y titulo y devuelve un apuntador a la cancion. Se usa en la funcion eliminarCancion'
        x = self.raiz
        while x is not None and interprete != x.data.interprete and titulo != x.data.titulo:    
            if interprete != x.data.interprete:
                if interprete < x.data.interprete:
                    x = x.left
                else:
                    x = x.right
            else:
                if titulo < x.data.titulo:
                    x = x.left
                else:
                    x = x.right
        return x
    
    def guardar_inorder(self,subTree,arreglo = []):
        #Realiza el recorrido in orden del arbol pero en vez de imprimir los nodos los guarda en un arreglo
        if subTree is not None:
            self.guardar_inorder(subTree.left,arreglo)
            arreglo.append(subTree)
            self.guardar_inorder(subTree.right,arreglo)
        return arreglo
    
    def sucesor(self,x):
        'Devuelve el sucesor de x'

        if x.right is not None:
            x = x.right
            while x.left is not None:
                x = x.left
            return x
        
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y
    