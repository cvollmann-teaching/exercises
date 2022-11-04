#!/usr/bin/env python
# coding: utf-8
# ### Notebook Environment
# 
# Im unteren Beispiel verschwindet durch im Environment gespeicherte Variablen
# ein Fehler. Die Variable `a` is nämlich undefiniert. Das kann dazu führen, dass vor der Abgabe des Programmes ein Fehler nicht Sichtbar ist, und das Programm bei den Korrekteuren der Abgabe garnicht funktioniert.
# 
# Deshalb ist es wichtig vor der Abgabe immer einmal `Restart the kernel, and re-run the whole notebook` als Test auszuführen.
b = 1
for k in range(10):
    b += a
a = b
print("b = ", a)
