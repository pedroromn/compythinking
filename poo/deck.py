# deck.py
""" Deck class represents a deck of Cards. """
import random
from card import Card

class DeckOfCards:
    """ Deck class represents a deck of Cards. """
    NUMBER_OF_CARDS = 52    # constant number of cards
    
    def __init__(self):
        """ Initialize the deck. """
        self.__current_card = 0
        self.__deck = []
        
        for count in range(DeckOfCards.NUMBER_OF_CARDS):
            self.__deck.append(Card(Card.FACES[count % 13], 
                            Card.SUITS[count // 13]))
            
    def shuffle(self):
        """ Shuffle deck. """
        self.__current_card = 0
        random.shuffle(self.__deck)
        
    def deal_card(self):
        """ Return the card """
        try:
            card = self.__deck[self.__current_card]
            self.__current_card += 1
            return card
        except:
            return None
        
    def __str__(self):
        """ Return a string representation of the current __deck. """
        s = ''
        for index, card in enumerate(self.__deck):
            s += f"{self.__deck[index]:<19}"
            if (index + 1) % 4 == 0:
                s += '\n'
        
        return s