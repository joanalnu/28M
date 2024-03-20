#first xlwings code #testing

import xlwings as xw
Path = "/Users/j.alcaide/Desktop/municipals 2019.xlsx"
xb = xw.Book(Path)




# Do something with the workbook
# For example, read data from a worksheet
worksheet = wb.sheets['Sheet1']
data = worksheet.range('A1').expand().value
print(data)

# Close the workbook
wb.close()

