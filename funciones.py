import csv
import json
import sys
from audiovisual import *
from tkinter.simpledialog import askstring as prompt
import pygame
import re

premios = [100,200,300,500,1000,2000,4000,8000,16000,32000,64000,125000,250000,500000,1000000]
comodines = {"50-50":"se puede usar",
             "publico":"se puede usar"}

def ventana(tamaño,titulo,icono):
    """
    Brief: 
        Crea una ventana
    Parametros:
        tamaño = el tamaño de la ventana
        titulo = el titulo de la ventana
        icono = el icono de la ventana
    Retorno:
        ventana
    """
    ventana = pygame.display.set_mode(tamaño)
    pygame.display.set_caption(titulo)
    pygame.display.set_icon(icono)   

    return ventana

def crear_menu():
    """
    Brief: 
        Crea un menú.
    Retorno:
        True, si se clickea dentro del rango del boton start
    """
    MENU = ventana((600,400),"Menú",imagen_icono)                          

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                if start_rectangulo.collidepoint(x,y):
                    return True

        
        MENU.blit(imagen_menu, [0, 0])

        start_rectangulo = MENU.blit(imagen_start,[8,320]) 

        pygame.display.update()

def actualizar_pantalla(pantalla,color,pregunta,premios,i,tiempo):
    """
    Brief: 
        actualiza la pantalla con las preguntas, respuestas, los premios, sus respectivos rectangulos y el reloj
    Parametros:
        pantalla = la pantalla donde se quiera usar esta funcion
        color = un color
        pregunta = la pregunta que se va a presentar en pantalla
        premios = los premios
        i = el indice que lo utilice para las preguntas y los premios.
        tiempo = el reloj 
    """
    dibujar_rectangulo(pantalla, color,50,410,220,30)
    dibujar_rectangulo(pantalla, color,50,460,220,30)
    dibujar_rectangulo(pantalla, color,300,410,220,30)
    dibujar_rectangulo(pantalla, color,300,460,220,30)
    presentar_opciones_preguntas(pantalla,preguntas[i]["opciones"],pregunta)
    dibujar_rectangulo(pantalla,AZUL,15,14,80,310,0)
    dibujar_rectangulo(pantalla,PURPURA,15,14,80,310,3) 
    presentar_premios(pantalla,premios[i],20,300)
    aplicar_mensaje(pantalla,tiempo,814,28,BLANCO,57)

#ARCHIVO CSV
def guardar_partida(premio: int):
    """
    Brief: 
        Guarda el nombre y el premio del jugador.
        Se utilizan 4 excepciones(una por si el archivo ya existe, la segunda si no se encontro el archivo, 
        la tercera si no se pudo abrir el archivo y la ultima es una Exception general que tira el mensaje 'Error!')
    Parametros:
        premio:int = El premio que gano el jugador. 
    Retorno:
    """
    try:
        jugador = cargar_nombre_premio(premio)

        with open("partidas.csv", "a", encoding="UTF8") as archivo:
            mensaje = f"{jugador['nombre']}, ${jugador['dinero_acumulado']}\n"
            archivo.write(mensaje)

    except FileExistsError:
        print("El archivo donde se guardan los datos ya existe")
    except FileNotFoundError:
        print("No se encontro el archivo csv, donde estan los datos de las partidas")
    except OSError:
        print("No se pudo abrir el archivo csv, donde estan los datos de las partidas")
    except Exception:
        print("Error!")

#ARCHIVO JSON
def cargar_preguntas():
    """
    Brief: 
        Carga las preguntas del archivo json.
    Parametros:
    Retorno:
        preguntas
    """ 
    preguntas = []

    with open("preguntas.json", "r", encoding="UTF8") as archivo:
        preguntas = json.load(archivo)

    return preguntas

preguntas = cargar_preguntas()


def aplicar_mensaje(pantalla: pygame.Surface, mensaje: str, posicion_x: int, posicion_y: int, color: tuple, tamaño: int, fuente: str = ""):
    """
    Brief: 
        Aplica un mensaje creado a la pantalla.
    Parametros:
        pantalla:pygame.surface = La pantalla del juego.
        mensaje:str = El mensaje.
        posicion_x:int = posicion en el eje x.
        posicion_y:int = posicion en el eje y.
        color:tuple = Un color especifico.
        tamaño:int = El tamaño del mensaje.
        fuente:str = La fuente del mensaje.
    Retorno:
    """
    mi_fuente = pygame.font.SysFont(fuente, tamaño)
    mensaje = mi_fuente.render(mensaje, 0, color)

    pantalla.blit(mensaje, (posicion_x, posicion_y))


def filtrar_pregunta(preguntas: list, premio: int):
    """
    Brief: 
        Filtra las preguntas por premio.
    Parametros:
        preguntas:list = Lista con las preguntas.
        premio:int = premio de la pregunta a filtrar.
    Retorno:
        Una pregunta con el premio .
    """
    preguntas_por_premio = []
    
    for pregunta in preguntas:
        if pregunta["premio"] == premio:
            preguntas_por_premio.append(pregunta)
    
    return preguntas_por_premio[0]

def respuesta_seleccionada(pregunta:dict):
    """
    Brief: 
        Evalua que repuesta fue seleccionada.
    Parametros:
        pregunta:dict = cada pregunta
    Retorno:
        True.
        False.
    """
    if pregunta["respuesta_correcta"] == pregunta["opciones"][0]:
        coordenadas = [50, 270, 410, 437]
    elif pregunta["respuesta_correcta"] == pregunta["opciones"][1]:
        coordenadas = [50, 270, 460, 487]
    elif pregunta["respuesta_correcta"] == pregunta["opciones"][2]:
        coordenadas = [300, 520, 408, 437]
    else:
        coordenadas = [300, 520, 458, 489]

    coordenadas_50_50 = [152,245,13,76]
    coordenadas_publico = [260,356,11,77]
    mouse_x,mouse_y = pygame.mouse.get_pos()        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if coordenadas_50_50[0] < mouse_x < coordenadas_50_50[1] and coordenadas_50_50[2] < mouse_y < coordenadas_50_50[3]:
                comodines["50-50"] = "utilizado"
            elif coordenadas_publico[0] < mouse_x < coordenadas_publico[1] and coordenadas_publico[2] < mouse_y < coordenadas_publico[3]:
                comodines["publico"] = "utilizado"
            elif mouse_x > coordenadas[0] and mouse_x < coordenadas[1] and mouse_y > coordenadas[2] and mouse_y < coordenadas[3]:
                return True
            else:
                return False


def presentar_comodin_publico(pantalla:pygame.Surface, pregunta):
    """
    Brief: 
        Presenta el comodin del "publico" si es que el comodin fue "utilizado".
    Parametros:
        pantalla:pygame.Surface = la pantalla donde se quiera printear
        pregunta = las preguntas
    """
    if comodines["publico"] == "utilizado":
        if pregunta["opciones"][0] == pregunta["respuesta_correcta"]:
            aplicar_mensaje(pantalla,"60%", 120,415,ROJO,17,"Arial Black")
            aplicar_mensaje(pantalla,"10%", 120,465,ROJO,17,"Arial Black")
            aplicar_mensaje(pantalla,"25%", 370,415,ROJO,17,"Arial Black")
            aplicar_mensaje(pantalla,"5%", 370,465,ROJO,17,"Arial Black")
        if pregunta["opciones"][1] == pregunta["respuesta_correcta"]:
            aplicar_mensaje(pantalla,"60%", 120,465,ROJO,17,"Arial Black")
            aplicar_mensaje(pantalla,"25%", 120,415,ROJO,17,"Arial Black")
            aplicar_mensaje(pantalla,"10%", 370,415,ROJO,17,"Arial Black")
            aplicar_mensaje(pantalla,"5%", 370,465,ROJO,17,"Arial Black")
        if pregunta["opciones"][2] == pregunta["respuesta_correcta"]:
            aplicar_mensaje(pantalla,"60%", 370,415,ROJO,17,"Arial Black")
            aplicar_mensaje(pantalla,"25%", 120,415,ROJO,17,"Arial Black")
            aplicar_mensaje(pantalla,"10%", 120,465,ROJO,17,"Arial Black")
            aplicar_mensaje(pantalla,"5%", 370,465,ROJO,17,"Arial Black")
        if pregunta["opciones"][3] == pregunta["respuesta_correcta"]:
            aplicar_mensaje(pantalla,"60%", 370,465,ROJO,17,"Arial Black")
            aplicar_mensaje(pantalla,"25%", 120,415,ROJO,17,"Arial Black")
            aplicar_mensaje(pantalla,"10%", 370,415,ROJO,17,"Arial Black")
            aplicar_mensaje(pantalla,"5%", 120,465,ROJO,17,"Arial Black")

def presentar_opciones_preguntas(pantalla: pygame.Surface, opciones: list, pregunta:dict):
    """
    Brief: 
        presenta las opciones en la pantalla y también la pregunta dependiendo tambien si se fue "utilizado" el comodin 50-50
    Parametros:
        pantalla:pygame.Surface = pantalla donde se van a mostrar las opciones y la pregunta.
        opciones:list = Opciones que se van a mostrar en la pantalla.
        pregunta:dict = la pregunta que se va a mostrar en la pantalla
    """
    aplicar_mensaje(pantalla, pregunta["enunciado"], 50, 370, VERDE, 18, "Arial Black")

    if comodines["50-50"] == "utilizado":
        if pregunta["opciones"][0] == pregunta["respuesta_correcta"]:
            aplicar_mensaje(pantalla, opciones[0], 55, 415,  BLANCO, 12, "Arial Black")
            aplicar_mensaje(pantalla, opciones[1], 55, 465,  BLANCO, 12, "Arial Black")
        if pregunta["opciones"][1] == pregunta["respuesta_correcta"]:
            aplicar_mensaje(pantalla, opciones[2], 305, 415,  BLANCO, 12, "Arial Black")
            aplicar_mensaje(pantalla, opciones[1], 55, 465,  BLANCO, 12, "Arial Black")
        if pregunta["opciones"][2] == pregunta["respuesta_correcta"]:
            aplicar_mensaje(pantalla, opciones[2], 305, 415, BLANCO, 12, "Arial Black")
            aplicar_mensaje(pantalla, opciones[3], 305, 465, BLANCO, 12, "Arial Black")
        if pregunta["opciones"][3] == pregunta["respuesta_correcta"]:
            aplicar_mensaje(pantalla, opciones[0], 55, 415, BLANCO, 12, "Arial Black")
            aplicar_mensaje(pantalla, opciones[3], 305, 465, BLANCO, 12, "Arial Black")
    else:
        aplicar_mensaje(pantalla, opciones[0], 55, 415,  BLANCO, 12, "Arial Black")
        aplicar_mensaje(pantalla, opciones[1], 55, 465,  BLANCO, 12, "Arial Black")
        aplicar_mensaje(pantalla, opciones[2], 305, 415, BLANCO, 12, "Arial Black")
        aplicar_mensaje(pantalla, opciones[3], 305, 465, BLANCO, 12, "Arial Black")

def presentar_premios(pantalla: pygame.Surface, valor_premio: int, posicion_x: int, posicion_y: int):
    """
    Brief: 
        presenta los premios en la pantalla.
    Parametros:
        pantalla:pygame.Surface = pantalla del juego.
        valor_premio:int = premio que se va a mostrar.
        posicion_x:int = posicion en el eje x.
        posicion_y:int = posicion en el eje y.
    Retorno:
    """
    for premio in premios:
        premio = str(premio)
        if valor_premio == int(premio):
            color_texto =  ROJO
        else:
            color_texto = BLANCO

        aplicar_mensaje(pantalla, f"${premio}", posicion_x, posicion_y, color_texto, 12, "Arial Black")
        posicion_y -= 20

        

def cargar_nombre_premio(premio: int):
    """
    Brief: 
        Carga el nombre del jugador
    Parametros:
        premio:int = El puntaje que logro alcanzar el jugador.
    Retorno:
        jugador
    """

    nombre_ingresado = prompt("Fin", f"¡Has terminado el juego, usted gano ${premio}! \nIngrese su nombre para guardalo en la tabla de puntuaciones: ")
    jugador = {}
    if nombre_ingresado != None and len(nombre_ingresado) != 0:
        if type(nombre_ingresado) == str or re.search("/",nombre_ingresado) != None():
            nombre_ingresado = re.sub("/", " ", nombre_ingresado)
            nombre_ingresado = nombre_ingresado.strip()
            jugador["nombre"] = nombre_ingresado                         
    else:
        jugador["nombre"] = "incognito"
    jugador["dinero_acumulado"] = premio
    return jugador

jugador = {
    "nombre":" ",
    "dinero_acumulado":0,
}