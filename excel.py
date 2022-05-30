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

def get_sheets(filename):
    file = pd.ExcelFile(filename)
    print(file.sheet_names)


def writeto_cell(filename, sheetname, row, col, data):
    file = pd.ExcelFile(filename)
    sheet = pd.read_excel(file, sheetname)
    numof_cols = sheet.shape[1]
    numof_rows = sheet.shape[0]

    if(row >=0 and row < numof_rows and col >=0 and col <= numof_cols):
        sheet.iloc[row, col] = data
        print(sheet.iloc[row, col])
    else:
        print("Invalid row/column number")


show_partial(file_name, sheet_name, 1, 5, 1, 1)
get_sheets(file_name)
writeto_cell(file_name, sheet_name, 0, 1, 'Momo')
iterate_sheet(file_name, sheet_name, 5)




