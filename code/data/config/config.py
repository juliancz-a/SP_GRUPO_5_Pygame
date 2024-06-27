import json
import re

def update_data (path:str, data):
    with open(path, "w", encoding="utf8") as archive:
        
        data = json.dump(data,archive,indent=4)

def read_data(path:str) -> list[dict]:
    with open(path, "r", encoding="utf8") as archive:
        data = json.load(archive)
    
    return data

def read_score (path, lista_jugadores):
    with open(path, "r", encoding="utf8") as archive:
        for empleado in archive:
            registro = re.split(",|\n", empleado)                
            if registro[0] != "nombre":
                diccionario_jugador = crear_diccionario_jugador(registro[0], registro[1],  registro[2])
                lista_jugadores.append(diccionario_jugador)
                
    return lista_jugadores

def update_score (path:str, lista_jugadores:list[dict]):
    """Actualiza un archivo CSV con una lista. Toma como header las keys de cada valor. Luego se escribe el contenido de cada empleado, es decir, cada diccionario.
    Args: path (ruta del archivo CSV con el contenido anterior), lista_jugadores(lista con el contenido actualizado)"""
    try:
        with open(path, "w", encoding="utf8") as archive:
        
            header = f"nombre,puntos,partidas\n"
            archive.write(header)
            for jugador in lista_jugadores:
                data_jugador = f"{jugador["nombre"]},{jugador["puntos"]},{jugador["partidas"]}\n"
                archive.write(data_jugador)
        

    except FileNotFoundError as e:
        print("Error crítico: no se ha encontrado el archivo solicitado para actualizar la lista. La lista permanecerá con su estado anterior.")


def crear_diccionario_jugador (nombre:str, puntos:int, partidas:int) -> dict:
    """Se crea un diccionario a partir de los parametros establecidos.
    Args: Datos que debe tener cada jugador. Cada uno debe estar previamente validado.
    Retorno: Diccionario con los datos."""
    diccionario_jugador = {
        "nombre" : nombre,
        "puntos" : int(puntos),
        "partidas" : int(partidas),
    }
    return diccionario_jugador
