from numpy import *
from pylab import *

""" Aa ichatou Mouhammadou Sow """


""" Fonctions de validation """

import numpy as np

def puissance4(x):
    return  x**3 + 2*(x**2)+ x +1

def sin_function(x):
    return np.sin(x)
  
def cos_function(x):
    return np.cos(x)

def atan_machin(x):
    return np.atan((x**2+x)/(x**4+x**2+1))
    

#from functions import puissance4
#from utils import plot_order


a = int(input('donner la valeur de a : '))
b = int(input('donner la valeur de b : '))
input_value = float(input("Donner la vraie valeur de l'intégrale(x^4,"+str(a)+","+str(b)+"): "))

plot_order(input_value,puissance4, a, b)


from utils import integrale_newton
from functions import puissance4, sin_function, cos_function

a = int(input('donner la valeur de a : '))
b = int(input('donner la valeur de b : '))
n = int(input('donner nombre de subdivisions n : '))

for k in [0,1,2,3]:
    print('\nIntegrale x^4: a=', a,', b=', b, ',m=',k,',n=0',n)
    print(integrale_newton(puissance4, a, b,k,n))

for k in [0,1,2,3]:
    print('\nIntegrale sin: a=', a,', b=', b, ',m=',k,',n=0',n)
    print(integrale_newton(sin_function, a, b,k,n))
    
    
for k in [0,1,2,3]:
    print('\nIntegrale cos: a=', a,', b=', b, ',m=',k,'n=',n)
    print(integrale_newton(cos_function, a, b,k,n)) 
    
  # 1.  
""" Formules d'intergration """
""" 1) Rectangle Gauche """
def RectangleGauche(f,a,b):
    return  (b - a)*f(a)

""" 2) Rectangle Droit """
def RectangleDroit(f,a,b):
    return (b - a)*f(b)

""" 3) Trapeze """
def Trapeze(f,a,b):
    return  (b - a)*((f(a) + f(b))/2)

""" 4) Simpson """
def Simpson(f,a,b):
    return ((b - a)/6)*(f(a) + 4*f((a + b)/2) + f(b))
# 2.
""" Formules d'intergration composites """

def integrale_newton(f, a, b,m, n):
    """
    f: function
    a: lower bound
    b: upper bound
    n: number of subdivisions
    m: 0=RectangleGauche, 1=RectangleGauche, 2=Trapeze, 3=Simpson(1/3)
    """
    sub = np.linspace(a,b, n+1)
    return np.sum([integrale(f,sub[i],sub[i+1],m) for i in range(n)])
# 3.
""" Calcul de l'erreur """
def rest(input_value, f, a,b,m,n):

    return abs(input_value - integrale_newton(f, a, b,m, n))
# 4.
def plot_order(input_value, f, a, b):
    
    N_list = np.arange(2,1000,2)
    for m in [0,1,2,3]:
        rest_list =[np.log(rest(input_value, f, a, b, m,N)) for N in N_list]
        plt.plot(np.log(N_list),rest_list, label='m='+str(m))
    plt.legend()
    plt.xlabel('$\log(N_k)$')
    plt.ylabel('$\log(R_{N_k}(f))$')
    plt.show()


    

