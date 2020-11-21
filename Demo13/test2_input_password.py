# 现在有一个银行保险柜，有两道密码。
# 想拿到里面的钱必须两次输入的密码都要正确。
# 如果第一道密码都不正确，那直接把你拦在外面；
# 如果第一道密码输入正确，才能有权输入第二道密码。
# 只有当第二道密码也输入正确，才能拿到钱

first_password = "123456"
second_password = "654321"
i = 0
while True:
    password1 = str(input("请输入密码："))
    if password1 != first_password and i <= 2:
        if i < 2:
            print("密码错误")
            i = i + 1


        else:
            print("密码已输入错误3次")
            break
    else:
        print("密码正确")
        while True:
            password2 = str(input(("请再次输入密码：")))
            if password2 == second_password:
                print("成功拿到钱")
                break
            else:
                print("第二次输入密码错误，请再次输入：")
