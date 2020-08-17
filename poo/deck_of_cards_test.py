# deck_of_cards_test.py

from deck import DeckOfCards

def main():
    my_deck = DeckOfCards()     # crear mazo de cartas
    #print(my_deck)
    my_deck.shuffle()           # revolver mazo de cartas
    #my_deck.deal_card()
    #print(my_deck)
    numero_de_jugadores = int(input("Numero de jugadores a repartir: "))
    s=''
    numero_cartas_sobrantes = my_deck.NUMBER_OF_CARDS % numero_de_jugadores
    numero_cartas_repartir = my_deck.NUMBER_OF_CARDS - numero_cartas_sobrantes
    for i in range(0, numero_cartas_repartir):
        s += f"{my_deck.deal_card():<19}"
        if (i + 1) % numero_de_jugadores == 0:
            s += '\n'
        
    print(s)
        
    
if __name__ == "__main__":
    main()


