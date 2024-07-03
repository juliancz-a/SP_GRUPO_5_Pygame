from game_tools.class_card import *

def set_cards(coords:tuple , initial_pos_x, cards_counter:int, letras:list = None) -> list:
    """Inicialización de las cartas: seteo de sus posiciones, asignación de letra.
    Args:
        coords (tuple): Coordenadas para mostrar las cartas en pantallas.
        cards_counter (int): Cantidad de cartas
        letras (list, optional): Lista de letras. Cada carta tendrá una letra asignada.

    Returns:
        list: Lista con las cartas definidas."""
    
    card_list = []

    if letras != None:
        letras = letras.split(",")

    center_x = coords[0] // 2 
    initial_pos_x = initial_pos_x #-315
    card_pos = 0

    for i in range(cards_counter):
        card = Card( (100,128), (initial_pos_x + center_x, coords[1]), CARTAS, CARTAS_SOUND, card_pos)

        if letras != None:
            card.letter = letras[i]
            
        card_list.append(card)

        initial_pos_x += 105
        card_pos +=1

    return card_list

def draw_cards(surface:pygame.Surface, card_list:list[Card], transparency:int = 255) -> None:
    """Dibujar en pantalla una lista de cartas preeinicializadas.

    Args:
        surface (pygame.Surface): Superficie en la cual dibujar las cartas
        card_list (list[Card]): Listado de cartas a ser bliteadas.
        transparency (int, optional): Transparencia de la carta (imagen)."""

    for i in range (len(card_list)):
        card_list[i].draw_card(surface, "white", FUENTE_2, 86, transparency)

def handle_cards_interaction(event:pygame.event.Event, card_list:list[Card], selected_letters:list, posiciones_libres:list, posiciones_anexadas:list):
    """Manejar la interacción del usuario con las cartas: Agregarlas o sacarlas de la selección.

    Args:
        event (pygame.event.Event): Evento capturado del loop de eventos. Se llama a func "interaction" para saber si el usuario presionó una carta.
        card_list (list[Card]): Lista de cartas utilizadas.
        selected_letters (list): Lista de letras seleccionadas, serán las letras asignadas a cada carta en particular.
        posiciones_libres (list): Posiciones libres (cartas no seleccionadas).
        posiciones_anexadas (list): Posiciones anexadas (cartas seleccionadas)"""
    
    occurrences_list = []
    for card in card_list:
        occurrences_list.append(card.letter)

    for card in card_list:
        action = card.card_box.interaction(event)

        if action:
            occurrences = occurrences_list.count(card.letter)

            if selected_letters.count(card.letter) < occurrences and not card.append:
                card.card_pos = append_card(card_list, card, selected_letters, posiciones_anexadas, posiciones_libres)
                
            elif card.append:
                return_card(card_list, card, selected_letters, posiciones_anexadas, posiciones_libres)


def append_card(card_list:list[Box], card:Card, selected_letters:list, posiciones_anexadas:list, posiciones_libres:list) -> int:
    """Anexar una carta a la primera posición libre que encuentre. Lista de letras seleccionadas adoptará a la letra de la carta según su posición. 
    Args:
        card_list (list[Box]): Lista de cartas utilizadas.
        card (Card): Carta actual con la cual se interactuó
        selected_letters (list): Lista de letras seleccionadas, serán las letras asignadas a cada carta en particular.
        posiciones_anexadas (list): Posiciones anexadas (pos de cartas seleccionadas) 
        posiciones_libres (list): Posiciones libres (pos de cartas no seleccionadas).

    Returns:
        int: Nueva posición de la carta, que se encuentra anexada a la selección."""
    
    new_card_pos = posiciones_libres[0]
    posiciones_libres.pop(0)

    selected_letters[new_card_pos] = card.letter
    
    card.append = True
    
    card.card_box.rectangulo.x, card.card_box.rectangulo.y = card_list[new_card_pos].card_box.original_rectangulo.x, 250
    
    posiciones_anexadas.append(card.card_pos)

    return new_card_pos

def return_card (card_list:list[Box], card, selected_letters:list, posiciones_anexadas, posiciones_libres:list):
    """Reestablecer una carta a una posición libre, regresandola a su estado original de preselección. Lista de letras seleccionadas volverá a no tener una carta seleccionda,
    segun la posición en donde ésta se encontraba.

    Args:
        card_list (list[Box]): Lista de cartas utilizadas.
        card (_type_): Carta actual con la cual se interactuó
        selected_letters (list): Lista de letras seleccionadas, serán las letras asignadas a cada carta en particular.
        posiciones_anexadas (_type_):  Posiciones anexadas (cartas seleccionadas)
        posiciones_libres (list):  Posiciones libres (cartas no seleccionadas)."""
    
    selected_letters[card.card_pos] = ""
    posiciones_libres.append(card.card_pos)
    ordenar_elementos(posiciones_libres, 1)
   
    card.card_pos = posiciones_anexadas[len(posiciones_anexadas) - 1]

    posiciones_anexadas.remove(card.card_pos)
    
    card.append = False

    card.card_box.rectangulo.x, card.card_box.rectangulo.y = card_list[card.card_pos].card_box.original_rectangulo.x, 100

def reset_pos (card_list:list[Box], selected_letters:list, posiciones_anexadas:list, posiciones_libres:list):
    """Reinciar a las cartas seleccionadas a las posiciones originales

    Args:
        card_list (list[Box]): Lista de cartas utilizadas.
        selected_letters (list): Lista de letras seleccionadas, serán las letras asignadas a cada carta en particular.
        posiciones_anexadas (list): Posiciones anexadas (cartas seleccionadas)
        posiciones_libres (list): Posiciones libres (cartas no seleccionadas)."""
    
    for card in card_list:
        if card.append:
            return_card(card_list, card, selected_letters, posiciones_anexadas, posiciones_libres)

def shuffle_cards (card_list:list):
    """Mezclar las letras asignadas a cada carta NO SELECCIONADA de una lista.
    Args:
        card_list (list): Lista de cartas utilizadas."""
    
    shuffle_card = []
    for card in card_list:
        
        if card.append is False:
            shuffle_card.append(card.letter)

    for card in card_list:
        if card.append is False:
           
            card.letter = shuffle_card.pop(random.randint(0, len(shuffle_card) - 1))
        

