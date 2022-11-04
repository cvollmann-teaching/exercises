#!/usr/bin/env python
# coding: utf-8
# ### Addieren von Zahlen
# (i)
def addInt(a,b):
    """
    Addiert zwei Zahlen a, b
    """
    a = float(a)
    b = float(b)
    return a + b
# (ii), (iv) Test verschiedene Fälle
a = input("a = ")
b = input("b = ")
print(addInt(a,b))
# Die Umwandlung liefert eine Fehlermeldung, wenn unerwartete Eingaben kommen. Damit kann man sich leicht gegen falsche Eingaben schützen. Zudem wird natürlich str in float umgewandelt.
addInt(2.0,3.1)
addInt("2.0","3.0")
