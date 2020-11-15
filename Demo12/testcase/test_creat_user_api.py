import ast

import pytest

from data.readexcel import read_Excel
from user.creat_user_api import creat_User_Api

@pytest.mark.user
def test_Creat_User_Api():
    dicts = read_Excel('C:/aQiuxia/Practise/jqx/Demo12/data/userInfo.xls')
    data_str = dicts['info1']
    data = ast.literal_eval(data_str)
    creat_User_Api("https://petstore.swagger.io/v2/user",data)