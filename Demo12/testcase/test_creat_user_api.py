import ast

import pytest

from data.readexcel import *
from user.creat_user_api import creat_User_Api, get_Api


list1 = read_data2('C:/aQiuxia/Practise/jqx/Demo12/data/userInfo.xls')
# data_str1 = dicts['info1']
# data1 = ast.literal_eval(data_str1)
# data_str2 = dicts['info2']
# data2 = ast.literal_eval(data_str2)
@pytest.mark.user
@pytest.mark.parametrize("url,data",[(url,list1[0]), (url, list1[1])])
def test_Creat_User_Api(url,data):

    creat_User_Api(url,data)

# @pytest.mark.baidu
# def test_Get_Api():
#     get_Api("https://www.baidu.com")