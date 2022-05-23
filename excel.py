import pandas as pd

file = pd.ExcelFile('file.xlsx')
employee_info = pd.read_excel(file, 'EmployeeInfo')

#iterate through each row
for index, row in employee_info.iterrows():
    print(index, row['Name'], row['Designation'])

print(employee_info.iloc[0:5]) # getting row 0 to 4
print(employee_info.iloc[0:5, 0:1]) #gettging row 0 to 4 and column 0
