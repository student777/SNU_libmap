import xlrd
import xlwt

a = xlrd.open_workbook('archive6.xlsx')
a = a.sheet_by_index(0)
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('Sheet 1', cell_overwrite_ok=True)
for j in [0,1,2,3,4,5,6,7,8,9,10,11,12]:
    for i in [152,154,156,158,160,162,164,166,168]:
        sheet.write(i-151,j,'대'+str(a.cell_value(i,j)))
        sheet.write(i-150,j, str(a.cell_value(i+1,j)))


wbk.save('test.xls')


a = xlrd.open_workbook('archive6.xlsx')
a = a.sheet_by_index(0)
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('Sheet 1', cell_overwrite_ok=True)
for i in range(0, a.nrows):
    for j in range(0, a.ncols):
        x = None
        try:
            x = a.cell_value(i, j)
        except:
            pass
        try:
            if isinstance(x, str):
                x = float(x)
                print((x, type(x)))

        except:
            pass
        sheet.write(i, j, x)

wbk.save('test.xls')


a = xlrd.open_workbook('archive3.xlsx')
a = a.sheet_by_index(0)
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('Sheet 1', cell_overwrite_ok=True)
for j in [23,24]:
    for i in range(0,40):
        sheet.write(2*i, j, '대'+str(a.cell_value(2*i, j)))
        sheet.write(2*i+1, j, str(a.cell_value(2*i+1, j)))


wbk.save('test.xlsx')

