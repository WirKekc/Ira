from pyxll import xl_func
from pylab import *
from scipy.linalg import *
import win32com.client
import numpy as np

# Excel = win32com.client.Dispatch("Excel.Application")
# wb = Excel.Workbooks.Open(u'D:\\Downloads\\Графики.xlsx')
# sheet = wb.Worksheets(u'Лист1')


@xl_func("float[][] x: float", "float[][] y: float")
def par_func(x, y):


    # def line_func(start, end):
    #     return [r[0].value for r in sheet.Range(f"{start}:{end}")]
    #
    # y = np.array(line_func('B5', 'B145'), float)
    array_x = np.array(x, float)
    array_y = np.array(y, float)
    # x = np.array(line_func('C5', 'C145'), float)
    #
    m = vstack((array_x ** 2, x, ones(141))).T
    s = lstsq(m, array_y)[0]
    # print(s)
    return s

