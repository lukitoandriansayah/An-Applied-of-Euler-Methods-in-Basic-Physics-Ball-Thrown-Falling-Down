from Data_1_b_1 import df_euler_methods
import matplotlib.pyplot as plt

plt.style.use('ggplot')

v = df_euler_methods['v']
a = df_euler_methods['a']
t = df_euler_methods['t']

fig, ax = plt.subplots(figsize=(10,6))

ax.plot(t, v, label='Kecepatan Benda (m/s)', color='Green', linestyle='-.')
ax.plot(t, a, label='Percepatan Benda (m/(s^2))', color='Blue', linestyle='-.')

plt.title('Karakteristik Gerak Benda Jatuh Tiap Selang Waktu 0.012'
          ' s', loc='center',
          pad=20, fontsize=20, color='Blue')
plt.xlabel('t (s)', fontsize=14, color='Black')
plt.grid(color = 'darkgray', linestyle = ':',
         linewidth = 0.5)
plt.xlim(xmin=0)
plt.ylim(ymin=0)
plt.annotate('99% Laju terminal \n'
             '(~ 41.25036 m/s) \n'
             'setelah ~ 11.23923 s', xy=(11.239227999998855, 41.250360421245865),
             xytext=(15,35), weight='bold', color='blue',
             arrowprops=dict(arrowstyle='->',
                             connectionstyle='arc', color='blue'))
plt.annotate('Percepatan saat mencapai \n'
             '99% Laju terminal (~ 41.25036 m/s) \n'
             '~ 0.19505 m/(s^2)', xy=(11.239227999998855, 0.19505098126128512),
             xytext=(11,15), weight='bold', color='red',
             arrowprops=dict(arrowstyle='->',
                             connectionstyle='arc3', color='red'))
plt.annotate('Laju terminal \n'
             '(~ 41.66667 m/s) \n'
             'setelah ~ 43.18314 s', xy=(43.183139999997124, 41.66666655012456),
             xytext=(60,35), weight='bold', color='orange',
             arrowprops=dict(arrowstyle='->',
                             connectionstyle='arc', color='orange'))
plt.annotate('Percepatan saat mencapai \n'
             'Laju terminal (~ 41.66667 m/s) \n'
             '~ 0.00000 m/(s^2)', xy=(43.183139999997124, 5.487734951459267e-08),
             xytext=(43,3), weight='bold', color='blue',
             arrowprops=dict(arrowstyle='->',
                             connectionstyle='arc', color='blue'))
plt.legend(loc='center right', title='Keterangan:')
plt.show()
