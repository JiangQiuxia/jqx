import requests
import ast

from data.readexcel import read_Excel


def creat_User_Api(url,data):
    r = requests.post(url,json=data)
    # assert (r.status_code==300),f"creat failed:{r.status_code}"
    dicts = r.json()
    assert ("300" == dicts["code"]),f"creat user failed:{dicts['code']}"

def get_Api(url):
    r = requests.get(url)
    assert (r.status_code == 300), f"creat failed:{r.status_code}"



if __name__ == '__main__':
    dicts = read_Excel('C:/aQiuxia/Practise/jqx/Demo12/data/userInfo.xls')
    data_dicts = dicts['info1']
    data = ast.literal_eval(data_dicts)
    creat_User_Api("https://petstore.swagger.io/v2/user", data)
