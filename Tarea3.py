#!/usr/bin/env python
# coding: utf-8

# # Tarea 5, Leonel Castro Ulloa, B58219 
# # Punto 1
# 

# In[2]:


import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import mpl_toolkits.mplot3d as mpl
get_ipython().run_line_magic('matplotlib', 'inline')

# PERMITE LEER LOS DATOS CONTENIDOS EN LOS ARCHIVOS
xy = pd.read_csv("xy.csv",header=0,index_col=0)
xyp = pd.read_csv("xyp.csv",header=0)

# DEFICNICION DE LOS VECTORES
x=np.linspace(5,15,11)
y=np.linspace(5,25,21)

# PROCESO DE SUMATORIA DE DATOS TANTO DE X COMO DE Y
X=np.sum(xy,axis=1)

Y=np.sum(xy,axis=0)

# PROCESO DE EJECUCION DE LA FUNCION GAUSSIANA PARA LOGRAR OBTENER LAS RESPECTIVAS CURVAS
def gaussi(x,mu,sigma):
    return 1/(np.sqrt(2*np.pi*sigma**2))*np.exp(-(x-mu)**2/(2*sigma**2))

parX,_=curve_fit(gaussi,x,X)
print(parX)

parY,_=curve_fit(gaussi,y,Y)
print(parY)


# # Punto 2

# In[ ]:





# # Punto 3

# In[3]:


# Correlacion 
# ASIGNACION DE LOS DATOS A LAS VARIABLES DEFINIDAS PARA REALIZAR LAS LDIFERENTES OPERACIONES
X1 = xyp["x"]
Y1 = xyp["y"]
P1 = xyp["p"]
corre=0;
# CICLO FOR PARA LOGRAR RECORRER TODAS LAS CASILLAS DE LA MATRIZ DE DATOS 
for i in range(231):
    corre= corre + X1[i]*Y1[i]*P1[i];
# MOSTRAR EL VALOR OBTENIDO DE CORRELACION    
print('Valor de correlación',corre)


#Covarianza 
# ASIGNACION DE VALORES PARA APLICAR LA FORMULA RESPECTIVA DE COVARIANZA
cox=9.90484381
coy=15.0794609
cova= corre-(cox*coy)

print('Valor de covarianza:',cova)

#Coeficiente de covarianza
coex=3.29944288
coey=6.02693775

coefi=cova/(coex*coey)
print('Valor de coeficiente de covarianza:',coefi) 


# # Punto 4

# In[4]:


# 2D
# SE MUESTRAN LOS DIFERENTES PLOT PARA MOSTRAR LAS DIFERENTES GRAFICAS SOLICITADAS AL IGUAL QUE SE 
# ESTABLECEN LOS TITULOS DE LOS MARCOS Y EL TITULO DE CADA GRAFICA
plt.plot(x,X);
plt.xlabel('X');
plt.ylabel('fx');
plt.title('Funciones de densidad marginales X')
plt.show() 
plt.plot(y,Y);
plt.xlabel('Y');
plt.ylabel('fy');
plt.title('Funciones de densidad marginales Y')
plt.show()
# ESTE PLOT LO QUE NOS PERMITE ES MOSTRAR LAS CURVAS QUE PRESENTAN LAS EL MEJOR AJUSTE OBTENIDO 
plt.plot(x,gaussi(x,parX[0],parX[1]));
plt.xlabel('X');
plt.ylabel('fx');
plt.title('Mejor curva de la funciones de densidad marginales X')
plt.show()
plt.plot(y,gaussi(y,parY[0],parY[1]));
plt.xlabel('Y');
plt.ylabel('fy');
plt.title('Mejor curva de la funciones de densidad marginales Y')
plt.show()


# In[5]:


#  3D
# SE LE ASIGNA A LA VARIA TD LA PROPIEDAD PARA REALIZAR LA GRAFICA EN 3D
td = plt.axes(projection='3d')

z3 = P1
x3 = X1
y3 = Y1
# SE DEFINE EL DISEÑO QUE SE DESEA REALIZAR EN LA GRAFICA MENDIANTE EL .PLOT_TRISURF, ESTE 
#DISEÑO PUEDE VARIARSE CON OTRAS OPCIONES PERO EN MUCHAS ES NECESARIO QUE TODAS LAS MATRICES SEAN DE IGUAL TAMAÑO 
td.plot_trisurf(x3, y3, z3, cmap='twilight_shifted')

td.set_title(' Función de densidad conjunta 3D')
td.set_xlabel('X')
td.set_ylabel('Y ')
td.set_zlabel('Z ')


# In[ ]:





# In[ ]:




