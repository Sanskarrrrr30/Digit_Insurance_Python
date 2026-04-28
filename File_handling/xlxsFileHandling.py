import xlrd

# # # reading an excel file using xlrd module
workbook = xlrd.open_workbook("data.xlsx")
sheet = workbook.sheet_by_index(0)  # Get the first sheet
print("Number of rows:", sheet.nrows)
print("Number of columns:", sheet.ncols)
# Read and print the content of the sheet
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        cell_value = sheet.cell_value(row, col)
        print(cell_value, end="\t")
    print()  # New line after each row