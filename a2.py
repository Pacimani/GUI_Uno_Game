#!/usr/bin/env python3
"""
Assignment 2 - UNO++
CSSE1001/7030
Semester 2, 2018
"""
import random

__author__ = "Pacifique Imani & 45217171 here"

# Write your classes here


class Card(object):  # a class
    """ A class card which accpet the number and colour of a card.   """

    def __init__(self, number, colour):
        """
        Construct the ordinary card based on the number and colour given.
        Parameter:
            numbe(int): the number of the card.
            colour(str): the colour of the card.
        Pre-condition:
            colour(str) present in the UnoGame.
        For example: red,yellow,green,blue and black.
        """
        self._number = number
        self._colour = colour
        self._AMOUNT = 0  

    def get_number(self):
        """Returns the number(int) this the card """
        return self._number

    def get_colour(self):
        """Returns the colour of this card """
        return self._colour

    def set_number(self, number):
        """Set the number value of the card.
        Parameter:
            number(int): a new number for the card 
        """
        self._number = number

    def set_colour(self, colour):
        """Set the colour of the card.
        Parameter:
            colour(str): the new colour of the card
        Pre-condition:
            colour present in UnoGame. eg: red,yellow,green,blue and black
        """
        self._colour = colour

    def get_pickup_amount(self):
        """A function which returns  the amount the card the next player should pick.
        Returns:
            Iff type(Card) is played, 0.
            Iff type(Pickup2Card) is played, the next player picks 2.
            Iff type(Pickup4Card) is played, the next player picks 4
            Otherwise, None(nonetype) iff the card is not one of the above.
        """
        return self._AMOUNT

    def matches(self, card):
        """Determine whether the next card to be place on the pile matches the colour of number of this card.
        Parameter:
            card<class, (int, str)>: with a either number or colour to be checked:
        Returns:
            bool: return True iff the card meet the conditions otherwise return False"""

        if card.get_number() == self._number or card.get_colour() == self._colour:
            return True
        return False

    def play(self, player, game):
        """Perform actions base on the class of card played, and returns None iff type(Card) is played.
        Parameter:
            game: UnoGame the interface where the game is played.
            player:the player playing the game
        For example:
          Iff type(Card) is played, None is returned otherwise the return will follow another cards' function
        Returns:
            None(Nonetype)
        """
        return None

    def __str__(self):
        """Return string associated with the card(type). this includes colour and number  """

        return f"Card({self._number}, {self._colour})"

    def __repr__(self):
        """Return string associated with the card(type). this includes colour and number """
        return str(self)


class SkipCard(Card):  # a subclass of Card
    """A class which accept the number and colour of the card """

    def __init__(self, number, colour):
        """Construct the skipcard class based on the number and colour given.
        Parameter:
            numbe(int): the number of the card.
            colour(str): the colour of the card.
        Pre-condition:
            colour(str) present in the UnoGame.
        For example: red,yellow,green,blue and black.
        """
        super().__init__(number, colour)

    def play(self, player, game):
        """Perform action base on the class of card played.
        Parameter:
            game: UnoGame the interface where the game is played.
            player: The player playing the game.
        For example:
         In this case, iff type(SkipCard) is played, the game is skipped otherwise the game remains normal
        """
        game.skip()

    def __str__(self):
        """Return string associated with the card(type). this includes colour and number """

        return f"SkipCard({self._number}, {self._colour})"

    def __repr__(self):
        """Return string associated with the card(type). this includes colour and number """
        return str(self)


class ReverseCard(Card):  # a subclass of Card
    """A class which takes in number and colour  """

    def __init__(self, number, colour):
        """Construct the reverse card class based on the number and colour given.
        Parameter:
            numbe(int): the number of the card.
            colour(str): the colour of the card.
        Pre-condition:
            colour(str) present in the UnoGame.
        For example: red,yellow,green,blue and black.
        """
        super().__init__(number, colour)

    def play(self, player, game):
        """Perform action base on the class of card played.
        Parameter:
            game: UnoGame the interface where the game is played.
            player:The player playing the game
        For example:
         In this case, iff type(ReverseCard) is played, the direction of the game is reversed otherwise the game remains normal
        """
        game.reverse()

    def __str__(self):
        """Return string associated with the card(type). this includes colour and number """

        return f"ReverseCard({self._number}, {self._colour})"

    def __repr__(self):
        """Return string associated with the card(type). this includes colour and number """
        return f"ReverseCard({self._number}, {self._colour})"


class Pickup2Card(Card): 
    """ A pickup 2 card class which takes in number and colour    """

    def __init__(self, number, colour):
        """Construct the Pickup2Card class based on the number and colour given.
        Parameter:
            numbe(int): the number of the card.
            colour(str): the colour of the card.
        Pre-condition:
            colour(str) present in the UnoGame.
        For Example: red,yellow,green,blue and black.
        """
        super().__init__(number, colour)
        self._AMOUNT = 2

    def play(self, player, game):
        """Perform action base on the class of card played.
        Parameter:
            game: UnoGame the interface where the game is played.
            player: The player playing the game.
        For example:
         In this case, iff type(Pickup2Card) is played, the next player pick up two card from the pickup_pile deck.
        """
        # pick up 2 cards from the pickup pile
        picking_card = game.pickup_pile.pick(self._AMOUNT)
        # getting location so that the game follows the normal direction after picking up
        next_player_location = game.get_turns()._location
        # the next player picks 2 cards and adds them to their deck
        game.next_player().get_deck().add_cards(picking_card)
        # returning the game in the normal direction
        game.get_turns()._location = next_player_location

    def __str__(self):
        """Return string associated with the card(type). this includes colour and number """
        return f"Pickup2Card({self._number}, {self._colour})"

    def __repr__(self):
        """Return string associated with the card(type). this includes colour and number """
        return str(self)


class Pickup4Card(Card):
    """ A special  class pick up 4 card which takes in number and colour """

    def __init__(self, number, colour):
        """Construct the Pickup4Card class based on the number and colour given.
        Parameter:
            numbe(int): the number of the card.
            colour(str): the colour of the card.
        Pre-condition:
            colour(str) present in the UnoGame.
        For example: red,yellow,green,blue and black.
        """

        super().__init__(number, colour)
        self._AMOUNT = 4

    def matches(self, card):
        """Returns True to all type of card present on the pile.
        Parameter:
            card<class> a Pickup4card class which matches with any card 
        Return:
            bool: True iff it is played all the time
        """
        return True

    def play(self, player, game):
        """Perform action base on the class of card played.
        Parameter:
            game: UnoGame the interface where the game is played.
            player: The player playing the game.
        For example:
         In this case, iff type(Pickup4Card) is played, the next player pick up two card from the pickup_pile deck.
        """

        picking_card = game.pickup_pile.pick(self._AMOUNT)
        next_player_location = game.get_turns()._location
        game.next_player().get_deck().add_cards(picking_card)
        # returning the game to its normal direction
        game.get_turns()._location = next_player_location

    def __str__(self):
        """Return string associated with the card(type). this includes colour and number """

        return f"Pickup4Card({self._number}, {self._colour})"

    def __repr__(self):
        """Return string associated with the card(type). this includes colour and number """

        return str(self)


class Deck(object):
    """A collection of ordered Uno cards   """

    def __init__(self, starting_cards=None):
        """Construct a collection ordered Uno cards as per the list of cards given.
        Parameter:
            starting_card(list): a list of card type wiht number and colour.
        Pre-condition:
            the deck should be initialize wiht None
        """

        if starting_cards == None:
            self._list_card = []
        else:
            self._list_card = []
            self._list_card.extend(starting_cards)

    def get_cards(self):
        """Returns the list of cards in the deck. or an empty list iff the list has no element"""
        return self._list_card

    def get_amount(self):
        """Return the amount of cards in the deck"""
        return len(self._list_card)

    def shuffle(self):
        """Shuffle the order of cards in the deck """
        random.shuffle(self._list_card)

    def pick(self, amount=1):
        """Take the first of card off the deck and return them 
        Parameter:
            amount(int): the amount of card to be taken off the deck.
        """
        if len(self._list_card) > amount:
            amount_cards = self._list_card[-amount:]
            # deleting these amount from the deck
            del self._list_card[-amount:]
            return amount_cards

        else:
            return self._list_card

    def add_card(self, card):
        """Place a card on top of the deck.
        Parameter:
            card<class (int, str)>: place a card on top of the deck."""
        self._list_card.append(card)

    def add_cards(self, cards):
        """Place a list of card on top of deck.
        Parameter:
            cards: a list of card<class(int, str)>"""
        self._list_card.extend(cards)

    def top(self):
        """Pick a card on top of the list and return it on None iff the list is empty."""
        if len(self._list_card) > 0:
            return self._list_card[-1]
        else:
            return None


class Player(object):
    """A player represent one of the players to play the game"""

    def __init__(self, name):
        """Create a player to play the game based on  given name.
        Parameter:
            name(str): the name of the player to play the game.
        """
        self._name = name
        self._deck = Deck()

    def get_name(self):
        """Returns the name(str) of the player"""
        return self._name

    def get_deck(self):
        """Returns the deck(list) of the player, a list cards """
        return self._deck

    def is_playable(self):
        """Returns NotImplementedError(class), the method to be implemented in the subclass"""

        raise NotImplementedError("on the base Player class")

    def has_won(self):
        """Determine whether the player has won the game or not.
        Returns:
            True(bool): returns True iff the player's deck is empty. otherwise None
        """
        if len(self._deck.get_cards()) == 0:
            return True
        else:
            return False

    def pick_card(self, putdown_pile):
        """Returns NotImplementedError(class), the method to be implemented in the subclass
        Paramenter:
            putdown_pile(list): list of putting down cards
        """

        raise NotImplementedError("on the base Player class")


class HumanPlayer(Player):
    """A human player to play the game"""

    def __init__(self, name):
        """Create a player to play the game based on  given name.
        Parameter:
            name(str): the name of the player to play the game.
        """
        super().__init__(name)
        self._deck = Deck()

    def is_playable(self):
        """Returns True 'bool' since this player is Human player"""
        return True

    def pick_card(self, putdown_pile):
        """Reterns None(Nonetype) when it is human turn to play 
        Paramenter:
            putdown_pile(list): list of putting down cards
        """
        return None


class ComputerPlayer(Player):
    """A Computer player to play the game"""

    def __init__(self, name):
        """Create a player to play the game based on  given name.
        Parameter:
            name(str): the name of the player to play the game.
        """
        super().__init__(name)
        self._deck = Deck()

    def is_playable(self):
        """Returns False 'bool' since this player is Human player"""
        return False

    def pick_card(self, putdown_pile):
        """Select the card to be played from the player's current deck and returns it
        Paramenter:
            putdown_pile(list): list of putting down cards
        """
        for card in self._deck.get_cards():
            #checking whether this card matches the card on top of the pile
            if card.matches(putdown_pile.top()):
                # save this card so that it is return it after it has been removed from the deck
                return_card = card
                self._deck.get_cards().remove(card)
                return return_card


def main():
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()
