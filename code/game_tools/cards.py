from game_tools.class_card import *

def set_cards(coords, cards_counter, letras = None) -> list:
    card_list = []
    x = coords[0]
    y = coords[1]

    center = x // 2 
    if letras != None:
        letras = letras.split(",")

    initial_pos_x = -315
    card_pos = 0

    for i in range(cards_counter):
        
        card = Card( (100,128), (initial_pos_x + center,y), CARTAS, CARTAS_SOUND, card_pos)
        if letras != None:
            card.letter = letras[i]
        card_list.append(card)

        initial_pos_x += 105
        card_pos +=1

    return card_list

def draw_cards(surface:pygame.Surface, card_list:list[Card], transparency = 255):

    for i in range (len(card_list)):
        card_list[i].draw_card(surface, "white", FUENTE_2, 86, transparency)


def set_cards_interaction(event, card_list:list[Card], selected_letters:list, posiciones_libres, pos_ocupadas):
    occurrences_list = []
    for card in card_list:
        occurrences_list.append(card.letter)
    for card in card_list:
        action = card.card_box.interaction(event)
        if action:
            occurrences = occurrences_list.count(card.letter)

            if selected_letters.count(card.letter) < occurrences and not card.append:

                pos = posiciones_libres[0]
                posiciones_libres.pop(0)
            
                selected_letters[pos] = card.letter
                
                card.append = True
               
                card.card_box.rectangulo.x, card.card_box.rectangulo.y = card_list[pos].card_box.original_rectangulo.x, 250
                
                pos_ocupadas.append(card.card_pos)
                card.card_pos = pos
                
            elif card.append:
                return_card(card_list, card, selected_letters, pos_ocupadas, posiciones_libres)


def reset_pos (card_list:list[Box], selected_letters:list, pos_ocupadas, posiciones_libres:list):
    for card in card_list:
        if card.append:
            return_card(card_list, card, selected_letters, pos_ocupadas, posiciones_libres)


def return_card (card_list:list[Box], card, selected_letters:list, pos_ocupadas, posiciones_libres:list):

    selected_letters[card.card_pos] = ""
    posiciones_libres.append(card.card_pos)
    ordenar_elementos(posiciones_libres, 1)

    card.card_pos = pos_ocupadas[len(pos_ocupadas) - 1]
    pos_ocupadas.remove(card.card_pos)
    
    card.append = False

    card.card_box.rectangulo.x, card.card_box.rectangulo.y = card_list[card.card_pos].card_box.original_rectangulo.x, 100


def join_cards (selected_letters:list, words_founded:list, combinaciones):
    retorno = False

    palabra = "".join(selected_letters).lower()

    set_dict = set(combinaciones)
    
    palabra_set = {palabra}

    intersec = set_dict.intersection(palabra_set)

    coincidences = words_founded.count(palabra)

    if len(intersec) > 0 and coincidences == 0:
        retorno = palabra
    else:
        retorno = False

    return retorno


def shuffle (card_list):
    shuffle_card = []
    for card in card_list:
        
        if card.append is False:
            shuffle_card.append(card.letter)
    for card in card_list:
        if card.append is False:
           
            card.letter = shuffle_card.pop(random.randint(0, len(shuffle_card) - 1))
        

