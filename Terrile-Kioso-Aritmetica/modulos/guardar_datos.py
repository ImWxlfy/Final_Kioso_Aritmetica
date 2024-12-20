import json
from datetime import datetime

def guardar_config(config: dict, estado_config: dict) -> None:
    """
    Guarda la configuración del juego en un archivo JSON.
    
    Args:
        config (dict): La configuración actual a guardar.
    """
    try:
        with open(r"Terrile-Kioso-Aritmetica\config.json", "w", encoding="utf8") as file:
            json.dump(config, file, indent=4)
    except Exception as e:
        print(f"Error al guardar la configuración: {e}")


def guardar_puntaje(nombre: str, puntuacion: int) -> None:
    """
    Guarda el puntaje del jugador en un archivo JSON con la fecha actual.
    
    Args:
        nombre (str): Nombre del jugador.
        puntuacion (int): Puntuación obtenida.
    """
    registro = {
        "nombre": nombre,
        "puntaje": puntuacion,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    try:
        with open(r"Terrile-Kioso-Aritmetica\historial_puntajes.json", "r", encoding="utf8") as file:
            historial = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        historial = []

    historial.append(registro)

    with open(r"Terrile-Kioso-Aritmetica\historial_puntajes.json", "w", encoding="utf8") as file:
        json.dump(historial, file, indent=4, ensure_ascii=False)