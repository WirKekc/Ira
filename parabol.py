from pylab import *
from scipy.linalg import *
import win32com.client
import numpy as np


Excel = win32com.client.Dispatch("Excel.Application")
wb = Excel.Workbooks.Open(u'D:\\Downloads\\Графики.xlsx')
sheet = wb.Worksheets(u'Лист1')


def line_func(start, end):
    return [r[0].value for r in sheet.Range(f"{start}:{end}")]


y = np.array(line_func('I3', 'I143'), float)
x = np.array(line_func('B3', 'B143'), float)

m = vstack((x**2, x, ones(141))).T
s = lstsq(m, y)[0]
print(s)
