import pygame
import sys

from modulos.contorno import dibujar_texto_con_contorno

def mostrar_menu(config: dict, recursos: dict, funciones: dict):
    """
    Muestra el menú principal del juego con opciones para iniciar, ver puntuaciones, ajustar volumen y salir.

    Args:
        config (dict): Configuración general del juego.
            - estado_config (dict): Configuración actual del juego.
            - BLACK (tuple): Color negro.
            - WIDTH (int): Ancho de la pantalla.
            - HEIGHT (int): Alto de la pantalla.
        recursos (dict): Recursos visuales.
            - font (pygame.font.Font): Fuente principal.
            - small_font (pygame.font.Font): Fuente secundaria.
            - screen (pygame.Surface): Superficie de la pantalla.
            - OPCIONES_IMAGE (pygame.Surface): Imagen para botones.
        funciones (dict): Funciones relacionadas con el menú.
            - cambiar_fondo_func (function): Función para cambiar el fondo.
            - reproducir_sonido_func (function): Función para reproducir sonidos.
            - iniciar_juego_func (function): Función para iniciar el juego.
            - mostrar_tabla_puntuaciones_func (function): Función para mostrar la tabla de puntuaciones.
            - mostrar_menu_volumen_func (function): Función para mostrar el menú de volumen.
            - reproducir_musica_func (function): Función para reproducir música.
            - guardar_config_func (function): Función para guardar la configuración.
    """
    funciones['reproducir_musica_func'](
        r"Terrile-Kioso-Aritmetica\modulos\assets\musica_menu.mp3",
        loop=-1, music_name="menu",
        current_music_list=[None, config['estado_config']["music_volume"]]
    )

    while True:
        funciones['cambiar_fondo_func'](r"Terrile-Kioso-Aritmetica\modulos\assets\fondo_menu.png")
        
        dibujar_texto_con_contorno(
            "Arithmetic Adventure",
            recursos['font'],
            (255, 255, 0),
            config['BLACK'],
            (config['WIDTH'] - recursos['font'].size("Arithmetic Adventure")[0]) // 2,
            config['HEIGHT'] // 6,
            recursos['screen']
        )

        botones = {
            "Iniciar Juego": (config['WIDTH'] // 2, config['HEIGHT'] // 2 - 150),
            "Tabla de Puntuaciones": (config['WIDTH'] // 2, config['HEIGHT'] // 2 - 50),
            "Volumen": (config['WIDTH'] // 2, config['HEIGHT'] // 2 + 50),
            "Salir": (config['WIDTH'] // 2, config['HEIGHT'] // 2 + 150)
        }
        rects = {}
        for texto, posicion in botones.items():
            rect = recursos['OPCIONES_IMAGE'].get_rect(center=posicion)
            recursos['screen'].blit(recursos['OPCIONES_IMAGE'], rect.topleft)
            dibujar_texto_con_contorno(
                texto,
                recursos['small_font'],
                (255, 255, 255),
                config['BLACK'],
                rect.centerx - recursos['small_font'].size(texto)[0] // 2,
                rect.centery - recursos['small_font'].get_height() // 2,
                recursos['screen']
            )
            rects[texto] = rect

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                funciones['guardar_config_func'](None, config['estado_config'])
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = event.pos
                    if rects["Iniciar Juego"].collidepoint(mouse_pos):
                        funciones['reproducir_sonido_func']("tocar_opcion", recursos['sonidos'], config['estado_config'], None)
                        funciones['iniciar_juego_func']()
                    elif rects["Tabla de Puntuaciones"].collidepoint(mouse_pos):
                        funciones['reproducir_sonido_func']("tocar_opcion", recursos['sonidos'], config['estado_config'], None)
                        funciones['mostrar_tabla_puntuaciones_func']()
                    elif rects["Volumen"].collidepoint(mouse_pos):
                        funciones['reproducir_sonido_func']("tocar_opcion", recursos['sonidos'], config['estado_config'], None)
                        funciones['mostrar_menu_volumen_func']()
                    elif rects["Salir"].collidepoint(mouse_pos):
                        funciones['reproducir_sonido_func']("tocar_opcion", recursos['sonidos'], config['estado_config'], None)
                        funciones['guardar_config_func'](config['estado_config'], config['estado_config'])
                        pygame.quit()
                        sys.exit()