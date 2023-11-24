import pygame

#IMAGENES
imagen_de_fondo = pygame.image.load("imagenes/fondo.webp")
imagen_de_fondo = pygame.transform.scale(imagen_de_fondo, (900, 500)) 

imagen_conductor = pygame.image.load("imagenes/reportero.png")
imagen_conductor = pygame.transform.scale(imagen_conductor, (350, 350))

imagen_menu = pygame.image.load("imagenes\imagen_menu.jpg")
imagen_menu = pygame.transform.scale(imagen_menu,(600,400))

imagen_start = pygame.image.load("imagenes/boton.png")
imagen_start = pygame.transform.scale(imagen_start,(150,73))

imagen_reloj = pygame.image.load("imagenes\clock.png")
imagen_reloj = pygame.transform.scale(imagen_reloj,(40,42))

imagen_fondo_tiempo = pygame.image.load("imagenes/fondo_tiemp.png")
imagen_fondo_tiempo = pygame.transform.scale(imagen_fondo_tiempo,(170,68))

imagen_50_50 = pygame.image.load("imagenes/50-50.png")
imagen_50_50 = pygame.transform.scale(imagen_50_50,(100,70))

imagen_publico = pygame.image.load("imagenes\publico.png")
imagen_publico = pygame.transform.scale(imagen_publico,(100,70))

imagen_icono = pygame.image.load("imagenes/icono.png")

#COLORES
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (50, 200, 90)
BLANCO = (255, 255, 255)
PLATEADO = (192, 192, 192)
PURPURA = (80, 0, 128)
AZUL = ( 0, 0, 180)

#SONIDO
def sonidos(path:str):
    """
    Brief: 
        Funcion para cargar el sonido
    Parametros:
        pantalla:str
    """
    sonido = pygame.mixer.Sound(path)
    sonido.set_volume(0.1)
    sonido.play(-1)

#DIBUJAR RECTANGULO
def dibujar_rectangulo(pantalla: pygame.Surface, color: tuple, posicion_x: int, posicion_y: int, ancho: int, alto: int, borde=0):
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
    pygame.draw.rect(pantalla, color, (posicion_x, posicion_y, ancho, alto),borde)