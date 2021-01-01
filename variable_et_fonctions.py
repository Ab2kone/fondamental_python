# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

########### LES VARIABLES ET FONCTIONS ################

#### fonction f(x)

f = lambda x: x**2
print(f(5))

def e_potentielle(masse, hauteur, g=9.81):
    E = masse * hauteur * g
    print(E,'Joules')

e_potentielle(80, 50)


######## exo #########
def fibonacci(n):
    a = 0
    b = 1
    while a < n :
        print(a)
        a, b = b, a+b

fibonacci(20)
