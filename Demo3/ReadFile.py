user_file=open('user_info.txt','r')
lines=user_file.readlines()
user_file.close()

for line in lines:
    username=line.split(',')[0]
    password=line.split(',')[1]
    print(username,password)
    # print(line)

    # 绝对路径：C:/aQiuxia/Practise/user_info.txt


