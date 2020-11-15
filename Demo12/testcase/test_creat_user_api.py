import ast

import pytest

from data.readexcel import read_Excel
from user.creat_user_api import creat_User_Api, get_Api


@pytest.mark.user
def test_Creat_User_Api():
    dicts = read_Excel('C:/aQiuxia/Practise/jqx/Demo12/data/userInfo.xls')
    data_str1 = dicts['info1']
    data1 = ast.literal_eval(data_str1)
    creat_User_Api("https://petstore.swagger.io/v2/user",data1)

@pytest.mark.baidu
def test_Get_Api():
    get_Api("https://www.baidu.com")