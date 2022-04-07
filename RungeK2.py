import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

h=10
x=np.arange(0,101,h)
y=np.zeros(len(x))

def f(x,y):
    return 5*(x)**5-3*(x**2)


#####Obtención de k's y y's 
K1=[0]
K2=[50]
for i in np.arange(0,10):
    k1=h*f(x[i],y[i])
    k2=h*f(x[i]+(1/2)*h , y[i]+(1/2)*k1)
    y[i+1]=y[i]+k2
    K1.append(k1)
    K2.append(k2)


X=[0,10,20,30,40,50,60,70,80,90,100,0]

#####y's Analíticas
analit=[]
for a in np.arange(0,101,h):
    A=((5/6)*(a**6))-(a**3)
    analit.append(A)


######Errores
Error=[]
for z in np.arange(0,11):
    error=-y[z]+analit[z]
    Error.append(error)


#####Gráfica RK2
plt.plot(x,y,'r',label='Runge Kutta (2do orden)')
plt.title('Método Runge Kutta (2do orden, h=10)',fontsize=15)
plt.xlabel('x', fontsize=14)
plt.ylabel('y',fontsize=14)
######Gráfica Analítica
plt.plot(x,analit,'k',label='Analítico')
plt.legend()
plt.show()


######Tabla
table=zip(X,analit,y,K1,K2,Error)
headers=['x', 'y Analítico', 'Runge Kutta 2', 'k1', 'k2','Error']
print(tabulate(table,headers=headers,tablefmt='fancy_grid',stralign='center',floatfmt='.0f'))