import xlrd

def read_Excel(file_path):
    xl = xlrd.open_workbook(file_path)
    table = xl.sheets()[0]
    info1 = table.cell_value(1, 0)
    info2 = table.cell_value(2, 0)
    # print(info1)
    # print(info2)
    dicts = {}
    dicts['info1'] = info1
    dicts['info2'] = info2
    return dicts

if __name__ == '__main__':
    read_Excel("userInfo.xls")