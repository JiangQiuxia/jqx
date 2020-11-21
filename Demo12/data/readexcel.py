import ast

import xlrd

def read_Excel(file_path):
    xl = xlrd.open_workbook(file_path)
    table = xl.sheets()[0]
    # #str
    # info1 = table.cell_value(1, 0)
    # info2 = table.cell_value(2, 0)
    # i =type(info1)
    # print(i)
    # print(info1)
    # print(info2)
    # dicts = {}
    # dicts['info1'] = info1
    # dicts['info2'] = info2
    # return dicts


def read_data2(file_path):
    xl = xlrd.open_workbook(file_path)
    table = xl.sheets()[0]
    nrows = table.nrows
    list = []
    for i in range(1, nrows):
        rowValue = table.row_values(i)[0]
        print(rowValue)
    #     rowValues = ast.literal_eval(rowValue)
    #     list.append(rowValues)
    # return list
url = "https://petstore.swagger.io/v2/user"
#    \n 代表换行 帖子




if __name__ == '__main__':
    read_data2("userInfo.xls")