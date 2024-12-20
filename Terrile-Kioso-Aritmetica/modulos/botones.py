import pygame

def dibujar_comodines(comodines: list, comodines_disponibles: dict, screen: pygame.Surface, WIDTH: int, HEIGHT: int):
    """
    Dibuja los comodines en la pantalla, ajustando su posición de manera responsiva.
    
    Args:
        comodines (list): Lista de comodines con sus propiedades.
        comodines_disponibles (dict): Comodines disponibles.
        screen (pygame.Surface): Superficie de la pantalla.
        WIDTH (int): Ancho de la pantalla.
        HEIGHT (int): Alto de la pantalla.
    """
    margen_lateral = WIDTH * 0.15
    margen_superior = HEIGHT * 0.15

    contador = 0
    for comodin in comodines:
        pos_x = margen_lateral
        pos_y = margen_superior + contador * (comodin["imagen_disponible"].get_height() + 20)

        comodin["rect"].topleft = (pos_x, pos_y)

        if comodin["usado"] or comodines_disponibles[comodin["nombre"]] <= 0:
            screen.blit(comodin["imagen_usado"], comodin["rect"].topleft)
        else:
            screen.blit(comodin["imagen_disponible"], comodin["rect"].topleft)
        
        contador += 1

def dibujar_opciones(opciones: list, small_font: pygame.font.Font, WIDTH: int, BLACK: tuple, GRAY: tuple, screen: pygame.Surface) -> list:
    """
    Dibuja las opciones de respuesta en la pantalla.
    
    Args:
        opciones (list): Lista de opciones de respuesta.
        small_font (pygame.font.Font): Fuente secundaria.
        WIDTH (int): Ancho de la pantalla.
        BLACK (tuple): Color negro.
        GRAY (tuple): Color gris.
        screen (pygame.Surface): Superficie de la pantalla.
        
    Returns:
        list: Lista de rectángulos de las opciones dibujadas y sus respuestas.
    """
    margen_superior = 120
    espacio_entre_opciones = 80
    opcion_width, opcion_height = 200, 50  # Tamaño del rectángulo

    opcion_rects = []
    contador = 0
    for opcion in opciones:
        rect = pygame.Rect(
            WIDTH // 2 - opcion_width // 2,
            margen_superior + 200 + contador * espacio_entre_opciones,
            opcion_width,
            opcion_height
        )
        opcion_rects.append((rect, opcion))

        pygame.draw.rect(screen, GRAY, rect)

        texto_opcion = small_font.render(str(opcion), True, BLACK)
        screen.blit(
            texto_opcion,
            (rect.centerx - texto_opcion.get_width() // 2, rect.centery - texto_opcion.get_height() // 2)
        )

        contador += 1

    return opcion_rects
