# A project that allows the use to roll various combinations of dice
# Using a pseudo-random number generator
# Returning the result graphically and by text

    # As a user
    # So that I can decide outcomes
    # I want to be able to roll dice

    # As a user
    # So that I can use different probabilities for my rolls
    # I want to choose from a selection of different sided dice

    # As a user
    # So that I can follow the rules of my favourite tabletop game
    # I want to be able to roll a combination of dice

    # As a user
    # So that I can see roll outcomes clearly
    # I want a graphical representation of the outcomes of my rolls

"""

 ┌────────────────────────┐
 │                        │
 │  DiceBox():            │
 │   -init                │ contains list of
 │     -self.dice  ───────┼────────────────────┐
 │   -add(num, sides)     │                    │
 │   -roll_all            │                    │
 │   -list_dice           │                    │
 │   -empty_box           │        ┌───────────▼──────────┐
 │                        │        │                      │
 └────────────────────────┘        │ Die():               │
                                   │  -init(self, sides)  │
                                   │    self.sides        │
                                   │  -roll               │
                                   │                      │
                                   │                      │
                                   └──────────────────────┘

"""


class Die():
    def __init__(self, sides):
        pass
    
    def roll(self):
        pass


class DiceBox():
    def __init__(self)
        pass

    def add(self, number_of_dice, sides):
        pass

    def roll_all():
        pass

    def list_dice():
        pass

    def empty_box():
        pass