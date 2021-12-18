import xml.etree.ElementTree as ET

import pygame as pygame

from Clases import Artistas, Albums, Cancion, Temporal
from Listas import *
from os import system
from tkinter import *
from tkinter import filedialog
#import pygame
from PIL import _imagingtk, Image

listaDeArtistas = ListaDoblementeE()
listaTemporal = ListaDoblementeE()

mi_archivo = ET.parse("ArchivosEntrada.xml")
padre = mi_archivo.getroot()

for hijo in padre:
    nombreCancion = hijo.attrib['nombre']
    contad = 0
    for subhijo in hijo:
        if contad == 0:
            artista = subhijo.text
        if contad == 1:
            album = subhijo.text
        if contad == 2:
            imagen = subhijo.text
        if contad == 3:
            ruta = subhijo.text
        contad = contad + 1

    temp = Temporal(nombreCancion, artista, album, imagen, ruta)
    listaTemporal.InsertarDatos(temp)

for objeto in listaTemporal.RecorrerLista():
    if listaDeArtistas.contador == 0:
        NuevoArtista = Artistas(objeto.artista)
        NuevoAlbum = Albums(objeto.album, objeto.imagen)
        NuevaCancion = Cancion(objeto.nombreCancion, objeto.ruta)
        NuevoAlbum.insertarCancion(NuevaCancion)
        NuevoArtista.insertarAlbum(NuevoAlbum)
        listaDeArtistas.InsertarDatos(NuevoArtista)

    else:
        for artista in listaDeArtistas.RecorrerLista():
            if artista.nombre == objeto.artista:
                print("El Artista esta Repetido")
                for album in artista.listadeAlbums.recorrer():
                    if album.nombre == objeto.album:
                        print("El Album esta repetido")
                        NuevaCancion = Cancion(objeto.nombredeCancion, objeto.ruta)
                        album.insertarCancion(NuevaCancion)
                        break

                    else:
                        NuevoAlbum = Albums(objeto.album, objeto.imagen)
                        NuevaCancion = Cancion(objeto.nombredeCancion, objeto.ruta)
                        NuevoAlbum.insertarCancion(NuevaCancion)
                        artista.insertarAlbum(NuevoAlbum)
                        break
            else:
                NuevoArtista = Artistas(objeto.artista)
                NuevoAlbum = Albums(objeto.album, objeto.imagen)
                NuevaCancion = Cancion(objeto.nombredeCancion, objeto.ruta)
                NuevoAlbum.insertarCancion(NuevaCancion)
                NuevoArtista.insertarAlbum(NuevoAlbum)
                listaDeArtistas.InsertarDatos(NuevoArtista)
                break
        break


for artista in listaDeArtistas.RecorrerLista():

    print("Artista: ", artista.nombre)
    for album in artista.listadeAlbums.RecorrerLista():

        print("Album: ", album.nombre)
        print("Imagen de Album: ", album.imagen)
        for cancion in album.listadeCanciones.RecorrerLista():
            print("Cancion: ", cancion.nombre)
            print("Ruta: ", cancion.ruta)

#Graphviz
archivo = open("Reporte.dot", "w")
archivo.write('digraph grid {layout=dot labelloc = "t"edge [   arrowtail="open" ] rankdir="LR"')

for artista in listaDeArtistas.RecorrerLista():
        archivo.write(artista.nombre +"\n")
for artista in listaDeArtistas.RecorrerLista():
         archivo.write(artista.nombre + "->"+"\n")
archivo.write('"Null :3"\n')

for artista in listaDeArtistas.RecorrerLista():
   for album in artista.listadeAlbums.RecorrerLista():
       archivo.write(artista.nombre + "->" + album.nombre+"\n")

for artista in listaDeArtistas.RecorrerLista():
    for album in artista.listadeAlbums.RecorrerLista():
       for cancion in album.listadeCanciones.RecorrerLista():
           archivo.write(album.nombre + "->" + cancion.nombre +"\n")


archivo.write("}")
archivo.close()

system("dot.exe -Tpng Reporte.dot -o Reporte.png")
system("Reporte.png")

#import xml.etree.ElementTree as ET
ListasReproduccion = ET.Element("ListaReproduccion")
Lista =ET.SubElement(ListasReproduccion,"Lista")
Lista.set("update", "nombre")


#Interfaz Grafica

ventana =Tk()
ventana.title("AppMusic")
ventana.geometry("400x400")
ventana.iconbitmap("Musica\GUI\icono-musica.ico") #"Musica\GUI\icono-musica.ico"
ventana.resizable(0,0)
pygame.mixer.init()

global posicion, n, pausa
posicion = 0
n = 0
pausa = False

Pantalla = Listbox(ventana, bg="beige", fg="blue", width=65, selectbackground="white", selectforeground="black")
Pantalla.pack(pady=10, anchor=CENTER)
Pantalla.config(bg="white", font=("Verdana", 16))

botones = Frame(ventana, bg="white", width=400, height=50)
botones.pack(pady=1, anchor=CENTER)

def abrir_musica():

    canciones = filedialog.askopenfilenames(initialdir="/", title="Escoge una cancion", filetypes=(("mp3", "*.mp3",),("all files", "*.*")))
    for cancion in canciones:
        cancion=cancion.replace(r"C:\Users\jefri\Desktop\Cursos Vacacionales\Laboratorio\proyectos\Musica\musica", "")
        cancion=cancion.replace(".mp3", "")
        Pantalla.insert(END, "cancion")

def reproducir():
    cancion=Pantalla.get(ACTIVE)
    pygame.mixer.music.load("parametro de lista doble")
    pygame.mixer.music.play()

def detener():
    pygame.mixer.music.stop()
    Pantalla.select_clear(ACTIVE)

def Pausar(pausar):
    global pausa
    pausa = pausar
    if pausa:
        pygame.mixer.music.unpause()
        pausa = False
    else:
        pygame.mixer.music.pause()
        pausa= True
        Pantalla.select_clear(ACTIVE)

def Anterior():

    global posicion, n

    if posicion>0:
        posicion=posicion-1
    else:
        posicion= 0

def Siguiente():
    global posicion, n

    if posicion==n-1:
        posicion=0
    else:
        posicion= posicion+1

def Borrar():
    Pantalla.delete(0, END)
    pygame.mixer.music.stop()

imagenAtras = Image.open("Musica\GUI\Botonatras.png")

imagenReproducir = Image.open("Musica\GUI\Botonplay.png")

imagenPausar = Image.open("Musica\GUI\Botonpausa.png")

imagenDetener = Image.open("Musica\GUI\Botondetener.png")

imagenSiguiente = Image.open("Musica\GUI\Botonsiguiente.png")
#imagenSiguiente = imagenSiguiente.subsample(2, 2)

atras = Button(botones, text="Atras", command= Anterior)
atras.grid(row=0, column=0)

reproducir= Button(botones, text="Reproducir", command= reproducir)
reproducir.grid(row=0, column=1)

pausar = Button(botones, text="Pausar", command= detener)
pausar.grid(row=0, column=2)

detener= Button(botones, text="Detener", command= Pausar)
detener.grid(row=0, column=3)

siguiente = Button(botones, text="Siguiente", command= Siguiente)
siguiente.grid(row=0, column=4)
#image=imagenSiguiente

MenuBarra = Menu(ventana)
ventana.config(menu=MenuBarra)

remover = Menu(MenuBarra)
MenuBarra.add_cascade(label="Borrar canciones", command=remover)
remover.add_command(label="Borrar todas las canciones", command=Borrar)



ventana.mainloop()