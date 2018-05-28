import os
from datetime import datetime
import shutil

def escribirTxt(tipo, nom_archivo):

    f = open('/media/sf_Carpeta_compartida/lista', 'a')
    f.write(tipo+"/"+nom_archivo+" \n")




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
        0: 'dog',
        1: 'rooster',
        2: 'pig',
        3: 'cow',
        4: 'frog',
        5: 'cat',
        6: 'hen',
        7: 'insects',
        8: 'sheep',
        9:'crow',
        10:'rain',
        11:'sea_waves',
        12:'crackling_fire',
        13:'crickets',
        14:'chirping_birds',
        15:'water_drops',
        16:'wind',
        17:'pouring_water',
        18:'toilet_flush',
        19:'thunderstorm',
        20:'crying_baby',
        21:'sneezing',
        22:'clapping',
        23:'breathing',
        24:'coughing',
        25:'footsteps',
        26:'laughing',
        27:'brushing_teeth',
        28:'snoring',
        29:'drinking_sipping',
        30:'door_wood_knock',
        31:'mouse_click',
        32:'keyboard_typing',
        33:'door_wood_creaks',
        34:'can_opening',
        35:'washing_machine',
        36:'vacuum_cleaner',
        37:'clock_alarm',
        38:'clock_tick',
        39:'glass_breaking',
        40:'helicopter',
        41:'chainsaw',
        42:'siren',
        43:'car_horn',
        44:'engine',
        45:'train',
        46:'church_bells',
        47:'airplane',
        48:'fireworks',
        49:'hand_saw',

    }[x]


def identificarElemento(elemento):
    #print ("hola")
    print ("identificando elemento")
    print(elemento)

    #print (len(elemento))
    letra = elemento[len(elemento)-6]+elemento[len(elemento)-5]

    #print (letra[0])
    if (letra[0] == "-"):
        print (clasificador(int(elemento[len(elemento)-5])))
        resultadoclasi = clasificador(int(elemento[len(elemento)-5]))
        #return resultadoclasi
        escribirTxt(resultadoclasi, elemento)
    else:
        resultadoclasi = clasificador(int(elemento[len(elemento)-6]+elemento[len(elemento)-5]))
        #return resultadoclasi
        escribirTxt(resultadoclasi, elemento)


def listarArchivos():
    #ruta_app = os.getcwd()
    #ruta_app = "/home/chinaski/Documentos/Python/Data"
    ruta_app="/media/sf_Carpeta_compartida/NuevaData1"
    total = 0
    num_archivos = 0
    formato = '%d-%m-%y %H:%M:%S'
    linea = '-' * 60

    for ruta, directorios, archivos in os.walk(ruta_app, topdown=True):
        print('\nruta       :', ruta)
        #print (len(ruta))
        #letra = ruta[len(ruta)-1]+ruta[len(ruta)-2]
        #print(letra)
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
            res = str (identificarElemento(elemento))
            print (res)
            #copiarArchivo((ruta_app + "/" + elemento), res)
            #origen = ruta_app + "/" + elemento
            #print (origen)
            #destino ="/home/chinaski/Documentos/Python/NuevaData/" + res + "/" + elemento
            #print (destino)
            #shutil.copyfile(origen, destino)
            #print('ultimo acceso:', ult_acceso)
            #print('tamano (Kb)  :', round(tamano/1024, 1))

    #print(linea)
    #print('Num. archivos:', num_archivos)
    #print('Total (kb)   :', round(total/1024, 1))

listarArchivos()

#print (Archivos)