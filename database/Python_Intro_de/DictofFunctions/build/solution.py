#!/usr/bin/env python
# coding: utf-8
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Dictionary-von-Funktionen" data-toc-modified-id="Dictionary-von-Funktionen-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Dictionary von Funktionen</a></span></li></ul></div>
# ### Dictionary von Funktionen
def add(a,b):
    return a+b
def mul(a,b):
    return a*b
compute = {"add": add, "mul": mul}
a = float(input("a = "))
b = float(input("b = "))
funName = input("Operation = ")
c = compute[funName](a,b)
print("\n", funName, "({:2.1f},{:2.1f}) = {:2.1f}".format(a,b,c), sep="")
