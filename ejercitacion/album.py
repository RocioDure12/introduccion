"""Funcion que se llame make album donde retornen un diccionario escribienfo album musical
nombre artista, nombre album. Debe contener un parametro opcional que sea la cantidad de pistas del album y
muestre esa informacion"""


def build_album(nombre_artista, nombre_album, cant_pistas=""):
    album = {'nombre': nombre_artista, 'album': nombre_album}
    if cant_pistas:
        album['pistas'] = cant_pistas
       
    return album

build_album("Gustavo Cerati", "Ahi vamos","13")



