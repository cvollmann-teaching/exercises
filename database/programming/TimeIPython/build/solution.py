#!/usr/bin/env python
# coding: utf-8
# ### Manuelles Compilieren vom Sourcecode
# 
# Die folgenden Zeilen müssen so in die entsprechenden Dateien kopiert oder ausgeführt werden.
# 
# Datei **sourceCode.py**
# 
# `print("Hello World")`
# 
# Ausführung in der **shell**
# 
# `python -m py_compile sourceCode.py`
# 
# 
# ### Time 
# 
# %time ist ein Magical command um schnell die Ausführungszeit fon Funktionen zu messen. Um genaure Informationen bei kleinen Funktionen zu bekommen bietet sich %timeit an. Dabei wird die Messung oft iteriert und ein Mittelwert zurück gegeben.
# Beispielprogramm zu Berechnung der Fakultät
def fac(n):
    m = 1
    if n > 1:
        m = fac(n-1)
    return m*n
get_ipython().run_line_magic('time', 'fac(10)')
get_ipython().run_line_magic('timeit', 'fac(10)')
