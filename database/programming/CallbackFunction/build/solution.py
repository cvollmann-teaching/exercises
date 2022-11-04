#!/usr/bin/env python
# coding: utf-8
# ### Nested Functions with **kwargs
from random import random
def algorithm(xstart, callback = None, **kwargs):
    """
    dummy algorithm.
    
    :param xstart: float
    :param callback: callback function with signature callback(xstart, **kwargs)
    :param **kwargs: additional parameters for callback
    """
    for _ in range(10):
        if callback:
            callback(xstart, **kwargs)
        xstart += (random()-.5)
    return xstart
def callback(x):
    """
    callback function. Prints the iterate x whenever it is called in the outer algorithm.
   
    :param x: Current iterate
    """
    print(x)
xfinal = algorithm(1, callback=callback)
print("xfinal: ", xfinal)
# **Vorteil der Nutzung von \*\*kwargs**
# 
# Wir definieren nun `callback()` neu, ohne `algorithm()` zu verändern. Das bedeutet, 
# der Nutzer von `algorithm()` kann seine callback-Funktion nach belieben definieren und einsetzten und muss dazu (den eventuell schrecklich komplizierten) Algorithmus nicht anfassen!
def callback(x, threshold=0.0):
    """
    callback function. Prints the iterate x if its called and x > threshold.
   
    :param x: Current iterate
    :param threshold: threshold=0.0 (optional)
    """
    if x > threshold:
        print(x)
xfinal = algorithm(1, callback=callback, threshold=1.6)   
print("xfinal: ", xfinal)
