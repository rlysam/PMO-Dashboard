import json
import openpyxl

# load json data from _low.json file
with open('_low.json') as f:
    data = json.load(f)

# create a new Excel workbook and select the active worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active

# write headers to the first row of the worksheet
headers = ["Business Unit", "Username", "Email"]
worksheet.append(headers)

# iterate through each row of data and write to the worksheet
for row in data:
    worksheet.append(row)

# save the workbook to a new Excel file
workbook.save(filename="output.xlsx")
