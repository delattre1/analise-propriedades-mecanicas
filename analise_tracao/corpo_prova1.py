import pandas as pd
import matplotlib.pyplot as plt
import math
from math import pi

def calcula_area_secao_transv(diametro):
    raio = diametro/2
    return (raio**2)*math.pi

def calcula_tensao(forca, sec_transv):
    return forca/sec_transv

df_corpo_prova_1 = pd.read_csv("ensaio_tracao_cp_1.csv",decimal=",",delimiter=";")[:-1]
df_corpo_prova_2 = pd.read_csv("ensiao_tracao_cp_2.csv",decimal=",",delimiter=";")[:-1]
df_corpo_prova_3 = pd.read_csv("ensaio_tracao_cp_3.csv",decimal=",",delimiter=";")[:-1]

#grafico tensao X deformacao - até 1%
diametro_cp1 = 8.5*0.001
diametro_cp2 = .0086
diametro_cp3 = .00865
l0 = 63.3 #tamanho inciial da barra

sec_transv1 = calcula_area_secao_transv(diametro_cp1)
tensao1 = calcula_tensao(df_corpo_prova_1["Force (N)"], sec_transv1)
df_corpo_prova_1["Tensão"] = tensao1

sec_transv2 = calcula_area_secao_transv(diametro_cp2)
tensao2 = calcula_tensao(df_corpo_prova_2["Force (N)"], sec_transv2)
df_corpo_prova_2["Tensão"] = tensao2

sec_transv3 = calcula_area_secao_transv(diametro_cp3)
tensao3 = calcula_tensao(df_corpo_prova_3["Force (N)"], sec_transv3)
df_corpo_prova_3["Tensão"] = tensao3



#coef angular da reta m = y-y0/x-x0
#reta 1 
x1 = 0.15
x2 = 0.2
y1 = df_corpo_prova_1['Tensão'][df_corpo_prova_1['Strain (%)'] == x1].values[0]
y2 = df_corpo_prova_1['Tensão'][df_corpo_prova_1['Strain (%)'] == x2].values[0]
coef1 = ((y2-y1)/(x2-x1))

x_paralela = df_corpo_prova_1['Strain (%)'].to_list()
y_paralela = [i * coef1 for i in x_paralela]
x_paralela = [i + 0.2 for i in x_paralela]


plt.plot(df_corpo_prova_1['Strain (%)'][:811],df_corpo_prova_1['Tensão'][:811], label="CP - 1")
plt.plot(x_paralela, y_paralela)
plt.ylim(0,3.5e8)
plt.show()