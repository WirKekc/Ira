import win32com.client
import numpy as np

Excel = win32com.client.Dispatch("Excel.Application")
wb = Excel.Workbooks.Open(u'D:\\Downloads\\Графики_Угданская_7.xlsx')
sheet = wb.Worksheets(u'Лист1')

max_t = 18
t_gr = 114

# X значения
x = np.array([r[0].value for r in sheet.Range(f"I3:I143")])
x1 = np.array([r[0].value for r in sheet.Range(f"U3:U60")])
x_date = np.array([r[0].value for r in sheet.Range(f"K3:K143")])

# Y значения
t1_y = np.array([r[0].value for r in sheet.Range(f"B3:B143")])
t2_y = np.array([r[0].value for r in sheet.Range(f"C3:C143")])
m1_y = np.array([r[0].value for r in sheet.Range(f"E3:E143")])
m2_y = np.array([r[0].value for r in sheet.Range(f"F3:F143")])
q_y = np.array([r[0].value for r in sheet.Range(f"H3:H143")])
# значения, которые можно вычеслить в питоне
# t1_2sk_y = np.array([r[0].value for r in sheet.Range(f"W3:W60")])
# t1_apr_y = np.array([r[0].value for r in sheet.Range(f"Y3:Y60")])
# t2_apr_y = np.array([r[0].value for r in sheet.Range(f"Z3:Z60")])
# t2_2_y = np.array([r[0].value for r in sheet.Range(f"X3:X60")])
# q_apr_y = np.array([r[0].value for r in sheet.Range(f"AC3:AC60")])
# q_s_y = np.array([r[0].value for r in sheet.Range(f"P3:P143")])
# q_s_apr_y = np.array([r[0].value for r in sheet.Range("AD3:AD60")])
# ud_nagr_y = np.array([r[0].value for r in sheet.Range("O3:O143")])
# m1_date_y = np.array([r[0].value for r in sheet.Range("L3:L143")])
# m2_date_y = np.array([r[0].value for r in sheet.Range("M3:M143")])

t1_2sk_y = [((max_t-t_gr)/56 * i + (19*max_t + 9*t_gr)/28) for i in x1]
#t1_2sk_y = (max_t-t_gr)/56 * x1[1] + (19*max_t + 9*t_gr)/28
print(t1_2sk_y)
