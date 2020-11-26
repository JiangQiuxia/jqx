import xlrd
import json


def read_excel():
    file = open('data/bike_code.json', 'r', encoding='utf-8')
    dicts_json = json.load(file)
    xl = xlrd.open_workbook("data/V5.xls")
    table = xl.sheets()[0]
    dicts = {}
    for i in range(4, 37):
        locale = table.cell_value(i, 2)
        count = 0
        list1 = []
        list2 =[]
        #put bike code from excel into dicts
        for j in range(11, 40):
            str1 = table.cell_value(i, j)
            str2 = str1.lower()
            if str2 == 'yes':
                list1.append(table.cell_value(2, j))
                count = count + 1
        dicts[locale] = {}
        dicts[locale]['total amount'] = count
        for n in range(0, len(list1)):
            is_correct = False
            for k, v in dicts_json.items():
                if list1[n] == v:
                    list2.append(k)
                    dicts[locale][list1[n]] = k
                    is_correct = True
                    break
            if not is_correct:
                print(f"{locale}:{list1[n]}数据异常")
    print(dicts)


if __name__ == '__main__':
    read_excel()