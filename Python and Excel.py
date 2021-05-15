pip install xlrd
import xlrd
book=xlrd.open_workbook(sample.xls)
print(book.nsheets)

# Put list data into a Excel file.
import os, sys
from openpyxl import Workbook
from datetime import datetime
dt = datetime.now()
list_values = [["01/01/2016", "05:00:00", 3],
               ["01/02/2016", "06:00:00", 4],
               ["01/03/2016", "07:00:00", 5],
               ["01/04/2016", "08:00:00", 6],
               ["01/05/2016", "09:00:00", 7]]
wb = Workbook()
sheet = wb.active
sheet.title = 'data'
row = 1
sheet['A'+str(row)] = 'Date'
sheet['B'+str(row)] = 'Hour'
sheet['C'+str(row)] = 'Value'
for item in list_values:
    row += 1
    sheet['A'+str(row)] = item[0]
    sheet['B'+str(row)] = item[1]
    sheet['C'+str(row)] = item[2]
filename = 'data_' + dt.strftime("%Y%m%d_%I%M%S") + '.xlsx'
wb.save(filename)
os.chdir(sys.path[0])
os.system('start excel.exe "%s\\%s"' % (sys.path[0], filename, ))


