import requests
from parameterized import parameterized


# @parameterized.expand("https://www.baidu.com",300)
def get_baidu(url, code, params):
    r = requests.get(url, params=params)
    # assert (r.status_code == 300),"status code error:"+str(r.status_code)
    assert (r.status_code == code), f"status code error:{r.status_code}"


def post_swagger(url, data, header):
    #payload-json;form data-data
    r = requests.post(url, json=data, headers=header)
    assert (r.status_code == 200), f"failed:{r.status_code}"
    print(r.status_code)
    dicts = r.json()
    assert ("180595048610224679" == dicts["message"]),f"response message error:{dicts['message']}"


if __name__ == '__main__':
    get_baidu("https://petstore.swagger.io/v2/user/", 300, "1111")
    header = {

    }
    data = {
        "id": 0,
        "username": "string",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }
    # post_swagger("https://petstore.swagger.io/v2/user",data,header)


# 1. post, get, put, delete
# 2. 搭框架，不要继承unittest
# 3. pytest参数化，数据放在excel里面
# 4. 报告html
