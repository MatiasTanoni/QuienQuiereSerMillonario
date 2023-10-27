from funciones import *
from audiovisual import *
import pygame, sys
import tkinter
from tkinter.simpledialog import askstring as alert
import time

pygame.init()

clock = pygame.time.Clock() 
PANTALLA = pygame.display.set_mode((900, 500))                                 
pygame.display.set_caption("¿Quien quiere ser millonario?")                                        
pygame.display.set_icon(imagen_icono) 

i = 0
tiempo_inicial = pygame.time.get_ticks()


pregunta = filtrar_pregunta(preguntas, premios[i])

while True:
    PANTALLA.blit(imagen_de_fondo, [0, 0])
    PANTALLA.blit(imagen_conductor, [535, 150])
    dibujar_rectangulo(PANTALLA, NEGRO,50,410,220,30)
    dibujar_rectangulo(PANTALLA, NEGRO,50,460,220,30)
    dibujar_rectangulo(PANTALLA, NEGRO,300,410,220,30)
    dibujar_rectangulo(PANTALLA, NEGRO,300,460,220,30)
    presentar_opciones_preguntas(PANTALLA,preguntas[i]["opciones"],pregunta)
    presentar_premios(PANTALLA,premios[i],20,300)
    respuesta = respuesta_seleccionada(pregunta) 

    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial  
    tiempo = f"{(tiempo_transcurrido*0.001):.02f}"
    dibujar_rectangulo(PANTALLA,PURPURA,775,17,107,60)
    aplicar_mensaje(PANTALLA,tiempo,790,30,BLANCO,50)

    if float(tiempo) >= 10.00 and float(tiempo) <= 15.00:
        mensaje = "Tiene unicamente 30 segundos para jugar en cada pregunta!"
        dibujar_rectangulo(PANTALLA,BLANCO,140,90,620,40)
        aplicar_mensaje(PANTALLA,mensaje,150,100,ROJO,18,"Arial Black") 

    if respuesta == True and float(tiempo) <= 30.02:
        tiempo_inicial = pygame.time.get_ticks()
        i = i + 1
        if i >= len(premios):
            guardar_partida(premios[i-1])
            break
        elif premios[i] == 2000 or premios[i] == 64000:
            opcion = prompt("Continuar","Desea continuar o retirarse con lo obtenido. Ingrese la palabra 'SALIR' si quiere salir")
            opcion = opcion.upper()
            if opcion == "SALIR":
                guardar_partida(premios[i-1])
                break
        pregunta = filtrar_pregunta(preguntas, premios[i])   
    elif respuesta == False or float(tiempo) >= 30.02:       
            guardar_partida(0) 
            break
    
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
