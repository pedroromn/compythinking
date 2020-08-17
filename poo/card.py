# card.py
# Deittel pag 429 - Class Card
""" Card class that represents a playing card and its image file name. """

class Card:
    """ Card class that represents a playing card and its image file name. """
    
    FACES = ['Ace', '2', '3' , '4' , '5', '6', '7', '8', 
             '9', '10', 'Jack', 'Queen', 'King']
    
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    
    def __init__(self, face, suit):
        """ Initialize a Card with a face and suit """
        self.__face = face
        self.__suit = suit
        
    @property
    def face(self):
        """ Return the Card's self.__face value.  """
        return self.__face
    
    @property
    def suit(self):
        """ Return the Card's self.__suit value. """
        return self.__suit
    
    @property
    def image_name(self):
        """ Return the Card's image file name. """
        return str(self).replace(' ', '_') + '.png'
    
    def __repr__(self):
        """ Return string representation for repr(). """
        return f"Card(face='{self.face}', suit='{self.suit}')"
    
    def __str__(self):
        """ Return string representation for str(). """
        return f"{self.face} of {self.suit}"
    
    def __format__(self, format):
        """ Return formatted string representation for str(). """
        return f"{str(self):{format}}"