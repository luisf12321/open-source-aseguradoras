# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import time

tiempo_inicio = time.time()

i = 0.05

print '---------- Pólizas ----------'
df_polizas = pd.read_csv('polizas.csv')
df_polizas['pnnx'] = None
print df_polizas.head()
print df_polizas.describe()

print '---------- Tabla Mortalidad ----------'
df_tabla_mortalidad = pd.read_csv('tabla_mortalidad.csv')
df_tabla_mortalidad['px'] = 1-df_tabla_mortalidad['qx']
print df_tabla_mortalidad.head()

print '---------- Tabla Vt ----------'
df_tabla_vt = pd.DataFrame({'Vt': range(0,100), 't': range(0,100)}).astype('float')
def Vt(df_tabla_vt):
    df_tabla_vt['Vt'] = pow(i+1, -df_tabla_vt['t'])
    return df_tabla_vt
df_tabla_vt.apply(Vt, axis=1)
df_tabla_vt['Vt1'] = df_tabla_vt['Vt'].shift(1)
print df_tabla_vt.head()

print '---------- Valores únicos de edad ----------'
print sorted(df_polizas['edad'].unique())

print '---------- Plazo máximo ----------'
print df_polizas['plazo'].max()

print '---------- Tabla x/t vacía ----------'
df_tabla_xt = pd.DataFrame({'x': sorted(df_polizas['edad'].unique())})
for t in range(0, df_polizas['plazo'].max()):
    df_tabla_xt[t] = int(t)
print df_tabla_xt.head()


'''
print '---------- Llenado de x/t ----------'
def multiplica(df_tabla_xt):
    x = df_tabla_xt['x']
    indice_x0 = x - 12

    Vt = df_tabla_vt['Vt'].ix[0:n-1].reset_index(drop=True)
    Vt1 = df_tabla_vt['Vt1'].ix[0:n-1].reset_index(drop=True)
    tPx = df_tabla_mortalidad['px'].ix[indice_x0:indice_x0+n-1].reset_index(drop=True)
    qxt =df_tabla_mortalidad['qx'].ix[indice_x0:indice_x0+n-1].reset_index(drop=True)

    df_tabla_xt['Vt1xtPxxQxt'] = Vt1 * tPx * qxt
    df_tabla_xt['VttPx'] = Vt * tPx

    
    return df_tabla_xt
df_tabla_xt.apply(multiplica, axis=1)

print df_tabla_xt.head()
'''

print '----------'
print 'Tiempo: ' + str(time.time() - tiempo_inicio) + ' segs.'
