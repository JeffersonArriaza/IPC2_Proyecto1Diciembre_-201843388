from Listas import *

class Artistas():
    def __init__(self, nombre):
        self.nombre =  nombre
        self.listadeAlbums = ListaDoblementeE()

    def insertarAlbum(self, album):
        self.listadeAlbums.InsertarDatos(album)

class Albums():
    def __init__(self, nombre, imagen):
        self.nombre =  nombre
        self.imagen =  imagen
        self.listadeCanciones = ListaDoblementeE()

    def insertarCancion(self, cancion):
        self.listadeCanciones.InsertarDatos(cancion)

class Cancion():
    def __init__(self, nombre, ruta):
        self.nombre =  nombre
        self.ruta =  ruta

class Temporal():
    def __init__(self, nombreCancion,artista,album,imagen,ruta):
        self.nombreCancion = nombreCancion
        self.artista = artista
        self.album = album
        self.imagen = imagen
        self.ruta = ruta