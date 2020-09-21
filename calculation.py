import win32com.client
from datetime import date, timedelta
import numpy as np


def from_file(name):
    el = []
    with open(f'.\\data\\{name}') as f:
        for line in f:
            el.append(float(line.replace(',', '.').strip()))
    return el


def line_func(y, x, x1):
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y)[0]
    return [m*i + c for i in x1]


# Переменные, короые нужно будет вводить при запуске программы
max_t = 18
t_gr = [114, 70]
S = 4325.2
d1 = date(2020, 1, 1)  # начальная дата

# X значения
t_nv = from_file('T_nv.txt')
temperature = from_file('weather.txt')

# # Y значения
t1 = from_file('T1.txt')
t2 = from_file('T2.txt')
m1 = from_file('M1.txt')
m2 = from_file('M2.txt')
q = from_file('Q.txt')

t1_y = np.array([t1 for _, t1 in sorted(zip(temperature, t1))])
t2_y = np.array([t2 for _, t2 in sorted(zip(temperature, t2))])
m1_y = np.array([m1 for _, m1 in sorted(zip(temperature, m1))])
m2_y = np.array([m2 for _, m2 in sorted(zip(temperature, m2))])
q_y = np.array([q for _, q in sorted(zip(temperature, q))])
ud_nagrev_y = [70*0.073/22 for i in range(len(temperature))]


t1_2_y = [((max_t-t_gr[0])/56 * i + (19*max_t + 9*t_gr[0])/28) for i in t_nv]
t2_2_y = np.array([((max_t-t_gr[1])/56 * i + (19*max_t + 9*t_gr[1])/28) for i in t_nv])
t1_2sk_y = np.array([i if i > 70 else 70 for i in t1_2_y])
q_s_y = np.array([(i*1000)/S for i in q_y])
delta = timedelta(days=len(temperature)-1)         # timedelta
date = np.array([d1 + timedelta(i) for i in range(delta.days + 1)])


t1_apr_y = np.array(line_func(t1_y, temperature, t_nv))
t2_apr_y = np.array(line_func(t2_y, temperature, t_nv))
q_apr_y = np.array(line_func(q_y, temperature, t_nv))
q_s_apr_y = np.array(line_func(q_s_y, temperature, t_nv))

print(ud_nagrev_y)
