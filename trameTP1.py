
from numpy import *
from pylab import *

""" YANNICK GNAGO """


""" Fonctions de validation """
def f1(x):
    return 1
""" interval : [-1,12]
    valeur   : 13
"""

def f2(x):
    return 2*x+1
""" interval : [-1,12]
    valeur   : 156
"""

def f3(x):
    return x**3 + 2*(x**2)+ x +1
""" interval : [-1,12]
    valeur   : 6420,91
"""


""" Formules d'intergration """
""" 1) Rectangle Gauche """
def RectangleGauche(f,a,b):
    return (b-a)*f(a)
""" 2) Rectangle Droit """
def RectangleDroit(f,a,b):
    return (b-a)*f(b)
""" 3) Trapeze """
def Trapeze(f,a,b):
    return ((b-a)/2)*(f(a)+f(b))
""" 4) Simpson """
def Simpson(f,a,b):
    return ((b-a)/6)*(f(a)+f(b)+4*f((a+b)/2))


""" Formules d'intergration composites """
""" 1) Rectangle Gauche """
def RectangleGaucheComp(f,a,b,n):
    somme=0
    h=float(b-a)/n
    x=a
    for i in range(0,n):
        somme=somme+f(x)
        x=x+h
    return h*somme
""" 2) Rectangle Droit """
def RectangleDroitComp(f,a,b,n):
    somme=0
    h=(b-a)/n
    x=a
    for i in range(1,n+1):
        somme=somme+f(x)
        x=x+h
    return h*somme
""" 3) Trapeze """
def TrapezeComp(f,a,b,n):
    somme=0
    h=float(b-a)/n
    x=a
    for i in range(0,n):
        somme=somme+(f(x)+f(x+h))/2
        x=x+h
    return h*somme
""" 4) Simpson """
def SimpsonComp(f,a,b,n):
    h=float(b-a)/n #pas
    somme=0
    x=a
    for i in range(0,n):
        somme=somme+f(x)+4*f((2*x+h)/2)+f(x+h)
        x=x+h
    return (h/6)*somme


""" Calcul de l'erreur """
def ErreurRectangleGauche(f,a,b,y0):
    return abs(y0-RectangleGauche(f,a,b))
def ErreurRectangleDroit(f,a,b,y0):
    return abs(y0-RectangleDroit(f,a,b))
def ErreurTrapeze(f,a,b,y0):
    return abs(y0-Trapeze(f,a,b))
def ErreurSimpson(f,a,b,y0):
    return abs(y0-Simpson(f,a,b))
""" Calcul de l'erreur formules composites"""
def ErreurRectangleGaucheComp(f,a,b,n,y0):
    return abs(y0-RectangleGaucheComp(f,a,b,n))

def ErreurRectangleDroitComp(f,a,b,n,y0):
    return abs(y0-RectangleDroitComp(f,a,b,n))

def ErreurTrapezeComp(f,a,b,n,y0):
    return abs(y0-TrapezeComp(f,a,b,n))

def ErreurSimpsonComp(f,a,b,n,y0):
    return abs(y0-SimpsonComp(f,a,b,n))

""" Programme """
""" - Valider les formules
    - Valider les formules composites
    - Ordre des methodes composites
"""


disp("CALCUL DE L'INTEGRALE D'UNE FONCTION f ENTRE a ET b")
a = int(input('Entrer a : '))
b = int(input('Entrer b : '))
n=int(input("entrer le nombre de subdivision:"))

"""Calcul d'integrale avec qq formules de Newton-Cotes"""
def method_integration(f,a,b,n,m):
    "m: 0=RectangleGauche, 1=RectangleGauche, 2=Trapeze, 3=simpson"
    if m==0:
        return RectangleGaucheComp(f,a,b,n)
    if m==1:
        return RectangleDroitComp(f,a,b,n)
    if m==2:
        return TrapezeComp(f,a,b,n)
    if m==3:
        return SimpsonComp(f,a,b,n)
def formule_newton(f, a, b,n,m):
    "n: nombre de subdivisions"
    subdivision= np.linspace(a,b, n+1)
    return np.sum([method_integration(f,subdivision[i],subdivision[i+1],n,m) for i in range(n)])

""" Calcul de l'erreur de facon generale """
def Erreur_integration(f,a,b,n,m,y0):
    "m: 0=RectangleGauche, 1=RectangleGauche, 2=Trapeze, 3=simpson"
    if m==0:
        return abs(y0-RectangleGaucheComp(f,a,b,n))
    if m==1:
        return abs(y0-RectangleDroitComp(f,a,b,n))
    if m==2:
        return abs(y0-TrapezeComp(f,a,b,n))
    if m==3:
        return abs(y0-SimpsonComp(f,a,b,n))
    

disp("""VALIDATION DES PROGRAMMES avec f1(x)=1   f2(x)=2x+1   f3(x)=x^3+2x^2+x+1""")
f1=lambda x:1
f2=lambda x:2*x+1
f3=lambda x:x**3 + 2*(x**2)+ x +1
print("l'integrale de f1 entre",a," et",b,"par la methode de rectangle a gauche est:", method_integration(f1,a,b,n,0))
print("l'integrale de f1 entre", a," et", b ,"par la methode de rectangle a droite est:", method_integration(f1,a,b,n,1))
print("l'integrale de f1 entre", a," et", b ,"par la methode de trapeze est:", method_integration(f1,a,b,n,2))
print("l'integrale de f2 entre", a," et", b ,"par la methode de trapeze est:", method_integration(f2,a,b,n,2))
print("l'integrale de f1 entre", a," et", b ,"par la methode de simpson est:", method_integration(f1,a,b,n,3))
print("l'integrale de f2 entre", a," et", b ,"par la methode de simpson est:", method_integration(f2,a,b,n,3))
print("l'integrale de f3 entre", a," et", b ,"par la methode de simpson est:", method_integration(f3,a,b,n,3))
    
fonction=eval(input("entrer la fonction f (ex: lambda x: 2*x+1):"))
valeur_exacte=float(input("Donner la valeur calculé de l'intégrale entre ["+str(a)+","+str(b)+"]:"))
#f=lambda x: 2*(x)+1
f=fonction
y0=valeur_exacte

disp("Resultat de l'integrale de f avec les formules de NewtonCotes:")
for M in [0,1,2,3]:
    print("la valeur de l'integrale de f pour m=",M,"est:", method_integration(f, a, b,n,M))

disp("Affichage des erreurs:")
for M in [0,1,2,3]:
    print ("l'erreur de calcul de l'integrale de f pour m=",M,"est", Erreur_integration(f,a,b,n,M,y0))

"""Droite des methodes_d'integration de log(erreur) en fonction de (log N)"""
def ordre_courbe(f, a, b,y0):
    N = arange(2,100,2)
    for M in [0,1,2,3]:
        Erreur_integration_vect =[log(Erreur_integration(f,a,b,n,M,y0)) for n in N]
        plot(log(N),Erreur_integration_vect,'*')
        legend(['m=0','m=1','m=2','m=3'])
        xlabel('$\log(N)$')
        ylabel('$\log(Erreur)$')
        title("Nuage des points des formules de Newton-Cotes de f .(log(N),log(erreur)) ")
        show()