from funciones import *
from audiovisual import *
import pygame, sys
import time

pygame.init()
start = crear_menu()

clock = pygame.time.Clock() 
PANTALLA = pygame.display.set_mode((900, 500))                                 
pygame.display.set_caption("¿Quien quiere ser millonario?")                                        
pygame.display.set_icon(imagen_icono) 

sonidos("sonidos\\03 A Forest.wav")

indice_premios = 0
tiempo_inicial = pygame.time.get_ticks() + 30 * 1000

pregunta = filtrar_pregunta(preguntas, premios[indice_premios])

while start :
    PANTALLA.blit(imagen_de_fondo, [0, 0])
    PANTALLA.blit(imagen_conductor, [535, 150])
    respuesta = respuesta_seleccionada(pregunta) 

    tiempo_actual = pygame.time.get_ticks()
    tiempo_restante = max(tiempo_inicial - tiempo_actual,0)
    tiempo = f"{(tiempo_restante*0.001):.0f}"
    PANTALLA.blit(imagen_fondo_tiempo,[720,12])
    PANTALLA.blit(imagen_reloj,[752,26])

    if comodines["50-50"] == "se puede usar":
        PANTALLA.blit(imagen_50_50,[150,10])
    if comodines["publico"] =="se puede usar":
        PANTALLA.blit(imagen_publico,[260,10])
         

    actualizar_pantalla(PANTALLA, NEGRO,pregunta,premios,indice_premios,tiempo)
    presentar_comodin_publico(PANTALLA,pregunta)

    if float(tiempo) >= 10.00 and float(tiempo) <= 15.00:
        mensaje = "Tiene unicamente 30 segundos para jugar en cada pregunta!"
        dibujar_rectangulo(PANTALLA,BLANCO,135,90,620,40)
        dibujar_rectangulo(PANTALLA,PURPURA,135,90,620,40,4)
        aplicar_mensaje(PANTALLA,mensaje,142,100,ROJO,18,"Arial Black") 

    if respuesta == True:
        if comodines["50-50"] == "utilizado":
            comodines["50-50"] = "desactivado"
        if comodines["publico"] == "utilizado":
            comodines["publico"] = "desactivado"
        tiempo_inicial = pygame.time.get_ticks() + 30 * 1000
        indice_premios = indice_premios + 1
        if indice_premios >= len(premios):
            guardar_partida(premios[indice_premios-1])
            break
        elif premios[indice_premios] == 2000 or premios[indice_premios] == 64000:
            opcion = prompt("Continuar","Desea continuar o retirarse con lo obtenido. Ingrese la palabra 'SALIR' si quiere salir")
            opcion = opcion.upper()
            if opcion == "SALIR":
                guardar_partida(premios[indice_premios-1])
                break
        pregunta = filtrar_pregunta(preguntas, premios[indice_premios])   
    elif respuesta == False or float(tiempo_restante) <= 0.0:       
            guardar_partida(0) 
            break
    
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
