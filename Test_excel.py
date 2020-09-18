import win32com.client
import numpy as np


Excel = win32com.client.Dispatch("Excel.Application")
wb = Excel.Workbooks.Open(u'D:\\Downloads\\Графики_Угданская_7.xlsx')
sheet = wb.Worksheets(u'Лист1')


def line_func(startX, endX, startY, endY, row, col1, col2):
    x = np.array([r[0].value for r in sheet.Range(f"{startX}:{endX}")])
    y = np.array([r[0].value for r in sheet.Range(f"{startY}:{endY}")])
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y)[0]
    # m = str(m).replace('.', ',')
    # c = str(c).replace('.', ',')
    sheet.Cells(row, col1).value = m
    sheet.Cells(row, col2).value = c
    val1 = sheet.Cells(row, col1).value
    val2 = sheet.Cells(row, col2).value
    return val1, val2

# print(str(m).replace('.', ','), str(c).replace('.', ','))


print(line_func('I3', 'I143', 'B3', 'B143', 11, 19, 20))
print(line_func('I3', 'I143', 'C3', 'C143', 12, 19, 20))
print(line_func('I3', 'I143', 'E3', 'E143', 13, 19, 20))
print(line_func('I3', 'I143', 'F3', 'F143', 14, 19, 20))
print(line_func('I3', 'I143', 'H3', 'H143', 15, 19, 20))
print(line_func('I3', 'I143', 'P3', 'P143', 16, 19, 20))
wb.Save()



