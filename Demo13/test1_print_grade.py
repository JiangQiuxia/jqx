while True:
    grade = int(input("请输入成绩："))
    if 0<=grade<60:
        print("不及格")
    elif 60<=grade<80:
        print("及格")
    elif grade>=80:
        print("优秀")
        break
    else:
        print("异常输入")
