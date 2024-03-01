import numpy as np
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")
labels = ['CDIA','CONT','AUTO', 'INFO']
color = ['#008fd5', '#fc4f30', '#e5ae37', '#69904f']
slices =[120, 80, 30, 20]
plt.pie(slices, labels = labels, wedgeprops={'edgecolor':'#c0c0c0'})

plt.title('Mi Gráfico de pastel')
plt.tight_layout()
plt.show()

#colores
#Blue = #008fd5
#Red = #fc4f30
#yellow = #e5ae37
#Green = #69904f