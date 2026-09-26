# mymath.py

import math
from statistics import mean, median, mode

# Arithmetic operators
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Trigonometric functions
def sine(angle):
    return math.sin(math.radians(angle))

def cosine(angle):
    return math.cos(math.radians(angle))

def tangent(angle):
    return math.tan(math.radians(angle))


# Statistical functions
def find_mean(data):
    return mean(data)

def find_median(data):
    return median(data)

def find_mode(data):
    return mode(data)
                                                                             