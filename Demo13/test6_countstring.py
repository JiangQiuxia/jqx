# asdfghdaghsgsgagsags 统计这个字符串里面每个字母出现的次数
str1 = "asdfghdaghsgsgagsags"
str2 = set(str1)
str3 = list(str2)
for i in range(0,len(str3)):
    times1 = str1.count(str3[i])
    print(f"{str3[i]}:{times1}")
