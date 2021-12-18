class Nodo(object):
    def __init__(self, dato=None, next=None, back=None):
        self.dato = dato
        self.next = next
        self.back = back

class ListaDoblementeE(object):
    def __init__(self):
        self.cabecera = None
        self.abajo = None
        self.contador = 0

    def InsertarDatos(self, dato):
        nodot = Nodo(dato)

        if self.cabecera is None:
            self.cabecera = nodot
            self.abajo = self.cabecera
        else:
            nodot.back = self.abajo
            self.abajo.next = nodot
            self.abajo = nodot

    def RecorrerLista(self):
        actual = self.cabecera
        while actual:
            dato = actual.dato
            actual = actual.next
            yield dato