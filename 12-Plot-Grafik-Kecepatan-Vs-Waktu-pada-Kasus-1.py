from Data_1_a_1 import df_euler_methods
import matplotlib.pyplot as plt

plt.style.use('ggplot')

v = df_euler_methods['v']
t = df_euler_methods['t']

fig, ax = plt.subplots(figsize=(10,6))

ax.plot(t, v, color='Green', linestyle = "-.")

plt.title('Kecepatan Gerak Benda Jatuh Tiap Selang Waktu 0.012'
          ' s', loc='center',
          pad=20, fontsize=20, color='Blue')
plt.xlabel('t (s)', fontsize=14, color='Black')
plt.ylabel('Kecepatan Benda (m/s)', fontsize=14, color='Black')
plt.grid(color = 'darkgray', linestyle = ':',
         linewidth = 0.5)
plt.xlim(xmin=0)
plt.ylim(ymin=0)

plt.text(7, 35, '41.20349480771995 m/s \n'
                         '(~ 41.2035 m/s)',
         color = 'red', weight = 'bold')
plt.text(30, 36, 'setelah ~ 42.19215 s',
         color = 'green', weight = 'bold')

plt.annotate('Laju setelah 10 s', xy=(10.001991999999367, 41.20349480771995),
             xytext=(7,38), weight='bold', color='red',
             arrowprops=dict(arrowstyle='->',
                             connectionstyle='angle3', color='red'))
plt.annotate('Laju terminal (~41.66667 m/s)', xy=(42.19215000000272, 41.66666655008769),
             xytext=(30,38), weight='bold', color='Green',
             arrowprops=dict(arrowstyle='->',
                             connectionstyle='arc', color='Green'))

plt.show()
