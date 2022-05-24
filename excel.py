import pandas as pd

file_name = 'file.xlsx'
sheet_name = 'EmployeeInfo'

def iterate_sheet(filename, sheetname, upto_row):
    file = pd.ExcelFile(filename)
    sheet = pd.read_excel(file, sheetname)
    numof_cols = sheet.shape[1]
    numof_rows = sheet.shape[0]

    if(upto_row <= numof_rows and upto_row >= 0):
        print(sheet.iloc[0:upto_row, 0:numof_cols])
    else:
        print('Invalid number of rows')

def show_partial(filename, sheetname, startrow, endrow, startcol, endcol):
    file = pd.ExcelFile(filename)
    sheet = pd.read_excel(file, sheetname)
    numof_cols = sheet.shape[1]
    numof_rows = sheet.shape[0]
    
    if(startrow >=0 and endrow <= numof_rows and startcol >=0 and endcol <= numof_cols):
        print(sheet.iloc[startrow-1 : endrow, startcol-1 : endcol])
    else:
        print("Invalid row/column number")

#iterate through each row

#print(employee_info.iloc[0:5]) # getting row 0 to 4
#print(employee_info.iloc[0:5, 0:1]) #gettging row 0 to 4 and column 0

#print(len(employee_info.index)) #get number of rows
#print(file.sheet_names) # get sheet names as list

#print(type(employee_info.iloc[0, 0])) #get cell value

show_partial(file_name, sheet_name, 1, 5, 1, 1)




