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
import random

class Die():
    def __init__(self, sides):
        self.sides = sides
    
    def roll(self):
        return random.randint(1, self.sides)


class DiceBox():
    def __init__(self):
        self.dice = []

    def add(self, number_of_dice, sides):
        for i in range (number_of_dice):
            new_die = Die(sides)
            self.dice.append(new_die)

    def roll_all(self):
        results = []
        for die in self.dice:
            results.append(die.roll())
        return f"Total: {sum(results)}, Rolls:{results}"

    def list_dice(self):
        return [f"d{die.sides}" for die in self.dice]

    def empty_box(self):
        self.dice = []