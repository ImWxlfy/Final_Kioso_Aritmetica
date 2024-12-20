import pygame

def reproducir_sonido(nombre_sonido: str, sonidos: dict, estado_config: dict, SONIDO_CANAL: pygame.mixer.Channel) -> None:
    """
    Reproduce un efecto de sonido específico.
    
    Args:
        nombre_sonido (str): Nombre del sonido a reproducir.
        sonidos (dict): Diccionario de sonidos pre-cargados.
        estado_config (dict): Configuración actual del juego.
        SONIDO_CANAL (pygame.mixer.Channel): Canal de sonido para reproducir el efecto.
    """
    try:
        sonido = sonidos[nombre_sonido]
        sonido.set_volume(estado_config["sounds_volume"])
        SONIDO_CANAL.play(sonido)
    except KeyError:
        print(f"Sonido '{nombre_sonido}' no encontrado.")

def reproducir_musica(ruta: str, loop: int, music_name: str, current_music: list) -> None:
    """
    Reproduce una pista de música si no está ya en reproducción.
    
    Args:
        ruta (str): Ruta de la música.
        loop (int): Número de veces que se repetirá la música (-1 para infinito).
        music_name (str): Nombre identificador de la música.
        current_music (list): Lista con el nombre actual y el volumen de la música.
    """
    if current_music[0] != music_name:
        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.set_volume(current_music[1])
            pygame.mixer.music.load(ruta)
            pygame.mixer.music.play(loop)
            current_music[0] = music_name
        except pygame.error as e:
            print(f"Error al reproducir música {ruta}: {e}")

def detener_musica(current_music: list) -> None:
    """
    Detiene la música en reproducción.
    
    Args:
        current_music (list): Lista con el nombre actual y el volumen de la música.
    """
    pygame.mixer.music.stop()
    current_music[0] = None

