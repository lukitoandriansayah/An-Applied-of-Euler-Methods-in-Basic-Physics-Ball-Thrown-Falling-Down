import pandas as pd
import numpy as np
from Data_1_a_1 import df
from Data_1_a_1 import df_euler_methods
import matplotlib.pyplot as plt

plt.style.use('ggplot')

x = df_euler_methods['x']
t = df_euler_methods['t']

fig, ax = plt.subplots(figsize=(10,6))

ax.plot(t, x, color='Red', linestyle = "-.")

plt.title('Jarak tempuh Gerak Benda Jatuh Tiap Selang Waktu 0.012'
          ' s', loc='center',
          pad=20, fontsize=20, color='Blue')
plt.xlabel('t (s)', fontsize=14, color='Black')
plt.ylabel('Jarak Tempuh Benda (m)', fontsize=14, color='Black')
plt.grid(color = 'darkgray', linestyle = ':',
         linewidth = 0.5)
plt.xlim(xmin=0)
plt.ylim(ymin=0)

plt.annotate('Jarak tempuh setelah \n'
             'mencapai Laju terminal \n'
             '~ 1672.41068 m \n atau 1.67241 km', xy=(42.19215000000272, 1672.4106802511492),
             xytext=(47,1500), weight='bold', color='blue',
             arrowprops=dict(arrowstyle='->',
                             connectionstyle='arc', color='blue'))
plt.show()