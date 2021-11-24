###########################################

#
# 1. In this exercise we will make a "Patient" class
#
# The Patient class should store the state of
# a patient in our hospital system.
#
#
# 1.1)
# Create a class called "Patient".
# The constructor should have two parameters
# (in addition to self, of course):
#
# 1. name (str)
# 2. symptoms (list of str)
#
# the parameters should be stored as attributes
# called "name" and "symptoms" respectively

#
# 1.2)
# Create a method called "add_test"
# which takes two paramters:
# 1. the name of the test (str)
# 2. the results of the test (bool)
#
# This information should be stored somehow.

#
# 1.3)
# Create a method called has_covid()
# which takes no parameters.
#
# "has_covid" returns a float, between 0.0
# and 1.0, which represents the probability
# of the patient to have Covid-19
#
# The probability should work as follows:
#
# 1. If the user has had the test "covid"
#    then it should return .99 if the test
#    is True and 0.01 if the test is False
# 2. Otherwise, probability starts at 0.05
#    and ncreases by 0.1 for each of the
#    following symptoms:
#    ['fever', 'cough', 'anosmia']

class Patient:
    
    def __init__(self, name, symptoms):
        self.name = name
        self.symptoms = symptoms
        
    def add_test(self, name_test, result_test):
        try:
            self.tests[name_test] = result_test
        except AttributeError:
            self.tests = {}
            self.tests[name_test] = result_test
            
    def has_covid(self):
        if "covid" in list(self.tests.keys()):
            if self.tests["covid"] == True:
                return 0.99
            else:
                return 0.01
        else :
            covid_symptoms = ['fever', 'cough', 'anosmia']
            nn = len(set(self.symptoms).intersection(covid_symptoms))
            return 0.05 + 0.1*nn

# example = Patient("mark", ["fever", "cough"])    
# example.add_test("blood_count", [123,456,789])
# example.add_test("pressure", [534,23,76])
# example.tests
# example.has_covid()

######################

# 2. In this exercise you will make an English Deck class made of Card classes
# 
# the Card class should represent each of the cards
#
# the Deck class should represent the collection of cards and actions on them

# 2.1) Create a Card class called "Card".
# The constructor (__init__ ) should have two parameters the "suit" and the "value" and the suit of the card.
# The class should store both as attributes.

class Card:
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

# example = Card("Diamonds", 10)
# example.suit
# example.value

# 2.2) Create a Deck class called "Deck".
# The constructor will create an English Deck (suits: Hearts, Diamonds, 
# Clubs, Spades and values: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K). 
# It will create a list of cards that contain each of the existing cards in an English Deck.
# Create a method called "shuffle" that shuffles the cards randomly. 
# Create a method called "draw" that will draw a single card and print the suit 
# and value. When a card is drawn, the card should be removed from the deck.

import random

class Deck:
    
    def __init__(self):
        list_deck = []
        for y in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for x in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']:
                list_deck.append(Card(y,x))
        self.deck = list_deck
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def draw(self):
        self.shuffle()
        draw_card = self.deck[0]
        self.deck = self.deck[1:]
        print(draw_card.value,draw_card.suit)
        
# mydeck = Deck()
# len(mydeck.deck)
# first_card = mydeck.deck[0]
# print(first_card.value,first_card.suit)

# mydeck.shuffle()
# len(mydeck.deck)
# first_card = mydeck.deck[0]
# print(first_card.value,first_card.suit)

# mydeck.draw()
# len(mydeck.deck)
# first_card = mydeck.deck[0]
# print(first_card.value,first_card.suit)

###################

# 3. In this exercise you will create an interface that will serve as template 
# for different figures to compute their perimeter and surface. 

# 3.1Create an abstract class (interface) called "PlaneFigure" with two abstract methods:
# compute_perimeter() that will implement the formula to compute the perimiter of the plane figure.
# compute_surface() that will implement the formula to compute the surface of the plane figure.

from abc import abstractmethod, ABCMeta

class PlaneFigure(metaclass = ABCMeta):
    
    @abstractmethod
    def compute_perimeter(self):
        return NotImplementedError

    @abstractmethod
    def compute_surface(self):
        return NotImplementedError
    

# 3.2 Create a child class called "Triangle" that inherits from "PlaneFigure" 
# and has as parameters in the constructor "base", "c1", "c2", "h". 
# ("base" being the base, "c1" and "c2" the other two sides of the triangle 
# and "h" the height). Implement the abstract methods with the formula of the triangle.

class Triangle(PlaneFigure):
    
    def __init__(self, base, side1, side2, height):
        self.base = base
        self.side1 = side1
        self.side2 = side2
        self.height = height
    
    def compute_perimeter(self):
        return self.base + self.side1 + self.side2
    
    def compute_surface(self):
        return (self.base * self.height) / 2

# example = Triangle(4,3,5,3)
# example.compute_perimeter()
# example.compute_surface()

# 3.3 Create a child class called "Rectangle" that inherits from "PlaneFigure" 
# and hasx as parameters in the constructor "a", "b" (sides of the rectangle). 
# Implement the abstract methods with the formula of the rectangle.

class Rectangle(PlaneFigure):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def compute_perimeter(self):
        return (self.length + self.width)*2
    
    def compute_surface(self):
        return (self.length * self.width)

# example = Rectangle(2,4)
# example.compute_perimeter()
# example.compute_surface()

# 3.3 Create a child class called "Circle" that inherits from "PlaneFigure" 
# and has as parameters in the constructor "radius" (radius of the circle). 
# Implement the abstract methods with the formula of the circle.

import math

class Circle(PlaneFigure):
    def __init__(self, radius):
        self.radius = radius
    
    def compute_perimeter(self):
        return 2 * math.pi * self.radius
    
    def compute_surface(self):
        return math.pi * (self.radius ** 2)

# example = Circle(3)
# example.compute_perimeter()
# example.compute_surface()

