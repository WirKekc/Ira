import matplotlib.pyplot as plt
from calculation import t1_y, t2_y, t1_2sk_y, t1_apr_y, t2_apr_y, t2_2_y, q_y, q_apr_y, m1_y, m2_y, q_s_y,\
    q_s_apr_y, ud_nagrev_y, temperature, t_nv, m1, m2, date


fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(
    nrows=5, ncols=1,
    figsize=(50, 50)  # размер окна вывода
)
# Table T
# dots
ax1.scatter(x=temperature, y=t1_y, label="t1_y", marker='o', c='r', alpha=0.5, s=9)
ax1.scatter(x=temperature, y=t2_y, label="t2_y", marker='o', c='y', alpha=0.5, s=9)
# lines
ax1.plot(t_nv, t1_2sk_y, alpha=0.9, label="t1_2", lw=3, mec='y', mew=2, ms=5)
ax1.plot(t_nv, t1_apr_y, alpha=0.9, label="t1_apr_y", lw=3, mec='c', mew=2, ms=5)
ax1.plot(t_nv, t2_apr_y, alpha=0.9, label="t2_apr_y", lw=3, mec='m', mew=2, ms=5)
ax1.plot(t_nv, t2_2_y, alpha=0.9, label="t2_2_y", lw=3, mec='k', mew=2, ms=5)
# Расшифровка линий и точек в графике
ax1.legend()
ax1.grid(True)
# Наименование график, оси Х и У
ax1.set_title('Т')
ax1.set_xlabel('Температура наружного воздуха, °С')
ax1.set_ylabel('Температура, °С')

# Table Q
# dots
ax2.scatter(x=temperature, y=q_y, label="q_y", marker='o', c='r', alpha=0.5, s=9)
# lines
ax2.plot(t_nv, q_apr_y, alpha=0.9, label="q_apr_y", lw=3, mec='y', mew=2, ms=5)
# Расшифровка линий и точек в графике
ax2.legend()
ax2.grid(True)
# Наименование график, оси Х и У
ax2.set_title('Q')
ax2.set_xlabel('Температура наружного воздуха, °С')
ax2.set_ylabel('Тепловая энергия, Гкал')


# Table М по температуре
# dots
ax3.scatter(x=temperature, y=m1_y, label="m1_y", marker='o', c='r', alpha=0.5, s=9)
ax3.scatter(x=temperature, y=m2_y, label="m2_y", marker='o', c='y', alpha=0.5, s=9)
# Расшифровка линий и точек в графике
ax3.legend()
ax3.grid(True)
# Наименование график, оси Х и У
ax3.set_title('М по температуре')
ax3.set_xlabel('Температура наружного воздуха, °С')
ax3.set_ylabel('Масса, т')

# Table Q/S
# dots
ax4.scatter(x=temperature, y=q_s_y, label="q_s_y", marker='o', c='r', alpha=0.5, s=9)
# lines
ax4.plot(temperature, ud_nagrev_y, alpha=0.9, label="ud_nagr_y", lw=3, mec='y', mew=2, ms=5)
ax4.plot(t_nv, q_s_apr_y, alpha=0.9, label="q_s_apr_y", lw=3, mec='k', mew=2, ms=5)
# Расшифровка линий и точек в графике
ax4.legend()
ax4.grid(True)
# Наименование график, оси Х и У
ax4.set_title('Q/S')
ax4.set_xlabel('Температура наружного воздуха, °С')
ax4.set_ylabel('Удельная суточная тепл.нагрузка, Гкал/кв.м')

# Table М по дате
# lines
ax5.plot(date, m1, alpha=0.9, label="m1", lw=3, mec='y', mew=2, ms=5)
ax5.plot(date, m2, alpha=0.9, label="m2", lw=3, mec='k', mew=2, ms=5)
# Расшифровка линий и точек в графике
ax5.legend()
ax5.grid(True)
# Наименование график, оси Х и У
ax5.set_title('М по дате')
ax5.set_xlabel('Дата')
ax5.set_ylabel('Масса, т')

plt.show()
