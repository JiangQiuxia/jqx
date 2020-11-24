import xlrd


def read_excel(file_path):
    xl = xlrd.open_workbook(file_path)
    table = xl.sheets()[0]
    company_email = table.cell_value(1, 0)
    VIP_email = table.cell_value(1, 1)
    member_email = table.cell_value(1, 2)
    dicts = {}
    dicts['company_email'] = company_email
    dicts['VIP_email'] = VIP_email
    dicts['member_email'] = member_email
    print(type(company_email))
    # return dicts


if __name__ == '__main__':
    read_excel('url.xls')
