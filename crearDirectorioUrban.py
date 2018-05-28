import os
from datetime import datetime
import shutil

def copiarArchivo(ruta_archivo, res):
    aux = res
    print ("la ruta del archivo es :" + ruta_archivo)
    print ("la clasificacion: "+ res)
    #origen = ruta_archivo
    #destino = ruta_archivo + os.mkdir("NuevaData")

    #if (aux == 'a'):
    if os.path.exists("/home/chinaski/Documentos/Python/NuevaData/"+aux):
        print ("existe carpeta")

    else:
        print ("no existe - la creamos")
        auxruta = "/home/chinaski/Documentos/Python/NuevaData/"+aux
        print (auxruta)
        os.mkdir(auxruta)



def clasificador(x):
    return {
        0: 'air_conditioner',
        1: 'car_horn',
        2: 'children_playing',
        3: 'dog_bark',
        4: 'drilling',
        5: 'engine_idling',
        6: 'gun_shot',
        7: 'jackhammer',
        8: 'siren',
        9:'street_music',

    }[x]


def identificarElemento(elemento):
    #print ("hola")
    print ("identificando elemento")
    print(elemento)


    #print (len(elemento))

    letra = elemento[len(elemento) - 6]


    print(letra)
    #letra = elemento[len(elemento)-6]+elemento[len(elemento)-5]

    #46669 - 4 - 0 - 33.wav
    if (elemento[len(elemento) - 6] == "-" and elemento[len(elemento) - 8] == "-" ): #46669 - 4 - 0 - 3.wav
        print ("prueba")
        print (clasificador(int(elemento[len(elemento) - 9])))
        resultadoclasi = clasificador(int(elemento[len(elemento) - 9]))
        print (resultadoclasi)
        return resultadoclasi
    if (elemento[len(elemento) - 6] == "-" and elemento[len(elemento) - 9] == "-" ): #46669 - 4 - 10 - 3.wav
        print ("prueba")
        print (clasificador(int(elemento[len(elemento) - 10])))
        resultadoclasi = clasificador(int(elemento[len(elemento) - 10]))
        print (resultadoclasi)
        return resultadoclasi
    if (elemento[len(elemento) - 7] == "-" and elemento[len(elemento) - 9] == "-" ):#46669 - 4 - 0 - 33.wav
        resultadoclasi = clasificador(int(elemento[len(elemento) - 10]))
        print (resultadoclasi)
        return resultadoclasi
    if (elemento[len(elemento) - 8] == "-" and elemento[len(elemento) - 10] == "-" ):#46669 - 4 - 0 - 330.wav
        resultadoclasi = clasificador(int(elemento[len(elemento) - 11]))
        print (resultadoclasi)
        return resultadoclasi
    if (elemento[len(elemento) - 8] == "-" and elemento[len(elemento) - 11] == "-" ):#46669 - 4 - 04 - 330.wav
        resultadoclasi = clasificador(int(elemento[len(elemento) - 12]))
        print (resultadoclasi)
        return resultadoclasi


def listarArchivos():
    #ruta_app = os.getcwd()
    #ruta_app = "/home/chinaski/Documentos/Python/Data"
    ruta_app="/media/sf_Carpeta_compartida/UrbanSound8K/audio"
    total = 0
    num_archivos = 0
    formato = '%d-%m-%y %H:%M:%S'
    linea = '-' * 60

    for ruta, directorios, archivos in os.walk(ruta_app, topdown=True):
        print('\nruta       :', ruta)
        #print (len(ruta))
        letra = ruta[len(ruta)-1]+ruta[len(ruta)-2]
        print(letra)
        for elemento in archivos:
            num_archivos += 1
            archivo = ruta + os.sep + elemento
            estado = os.stat(archivo)
            tamano = estado.st_size
            ult_acceso = datetime.fromtimestamp(estado.st_atime)
            modificado = datetime.fromtimestamp(estado.st_mtime)
            ult_acceso = ult_acceso.strftime(formato)
            modificado = modificado.strftime(formato)
            total += tamano
            print(linea)
            print('archivo      :', elemento)
            print  ( elemento)
            print (num_archivos)
            res = str (identificarElemento(elemento))
            print (res)
            copiarArchivo((ruta_app + "/" + elemento), res)
            origen = ruta_app + "/" + elemento
            print (origen)
            destino ="/home/chinaski/Documentos/Python/NuevaData/" + res + "/" + elemento
            print (destino)
            shutil.copyfile(origen, destino)


            #print('ultimo acceso:', ult_acceso)
            #print('tamano (Kb)  :', round(tamano/1024, 1))

    #print(linea)
    #print('Num. archivos:', num_archivos)
    #print('Total (kb)   :', round(total/1024, 1))

listarArchivos()

#print (Archivos)

