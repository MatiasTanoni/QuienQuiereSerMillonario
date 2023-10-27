import json
import pygame

#IMAGENES
imagen_de_fondo = pygame.image.load("imagenes/fondo.webp")
imagen_de_fondo = pygame.transform.scale(imagen_de_fondo, (900, 500)) 

imagen_conductor = pygame.image.load("imagenes/reportero.png")
imagen_conductor = pygame.transform.scale(imagen_conductor, (350, 350))

imagen_icono = pygame.image.load("imagenes/icono.png")

#COLORES
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (50, 200, 90)
BLANCO = (255, 255, 255)
PLATEADO = (192, 192, 192)
PURPURA = (128, 0, 128)

#DIBUJAR RECTANGULO
def dibujar_rectangulo(pantalla: pygame.Surface, color: tuple, posicion_x: int, posicion_y: int, ancho: int, alto: int):
    """
    Brief: 
        Dibuja un rectangulo en la pantalla.
    Parametros:
        pantalla:pygame.Surface = pantalla del juego.
        color:tuple = Un color.
        ubicacion_x (int): posicion en el eje x.
        ubicacion_y (int): posicion en el eje y.
        ancho (int): Ancho del rectangulo. 
        alto (int): Largo del rectangulo.
    Retorno:
    """
    pygame.draw.rect(pantalla, color, (posicion_x, posicion_y, ancho, alto))