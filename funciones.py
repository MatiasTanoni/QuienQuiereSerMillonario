import csv
import sys
from audiovisual import *
from tkinter.simpledialog import askstring as prompt
import pygame
import random
import re

premios = [100,200,300,500,1000,2000,4000,8000,16000,32000,64000,125000,250000,500000,1000000]


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
        Aplica el mensaje creado a la pantalla.
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
        premio:int = Dificultad de la pregunta a filtrar.
    Retorno:
        Una pregunta con el premio .
    """
    preguntas_por_premio = []
    
    for pregunta in preguntas:
        if pregunta["premio"] == premio:
            preguntas_por_premio.append(pregunta)
    
    return preguntas_por_premio[0]
    
    
def presentar_opciones_preguntas(pantalla: pygame.Surface, opciones: list, pregunta:dict):
    """
    Brief: 
        presenta las opciones en la pantalla y también la pregunta.
    Parametros:
        pantalla:pygame.Surface = pantalla donde se van a mostrar las opciones y la pregunta.
        opciones:list = Opciones que se van a mostrar en la pantalla.
        pregunta:dict = la pregunta que se va a mostrar en la pantalla
    Retorno:
    """
    aplicar_mensaje(pantalla, pregunta["enunciado"], 50, 370, VERDE, 18, "Arial Black")

    aplicar_mensaje(pantalla, opciones[0], 55, 415,  BLANCO, 12, "Arial Black")
    aplicar_mensaje(pantalla, opciones[1], 55, 465,  BLANCO, 12, "Arial Black")
    aplicar_mensaje(pantalla, opciones[2], 305, 415, BLANCO, 12, "Arial Black")
    aplicar_mensaje(pantalla, opciones[3], 305, 465, BLANCO, 12, "Arial Black")


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

    posicion_mouse = pygame.mouse.get_pos()        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if posicion_mouse[0] > coordenadas[0] and posicion_mouse[0] < coordenadas[1] and posicion_mouse[1] > coordenadas[2] and posicion_mouse[1] < coordenadas[3]:
                return True
            else:
                return False


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
        jugador["nombre"] = nombre_ingresado
    else:
        jugador["nombre"] = "incognito"
    jugador["dinero_acumulado"] = premio
    return jugador


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

jugador = {
    "nombre":" ",
    "dinero_acumulado":0,
}