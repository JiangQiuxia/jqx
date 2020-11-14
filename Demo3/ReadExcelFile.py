import xlrd

xl=xlrd.open_workbook('user_info2.xlsx')

table=xl.sheets()[0]

rows=table.nrows
print(rows)

for row in range(rows):
    data=str(table.row_values(row))
    print(data)
