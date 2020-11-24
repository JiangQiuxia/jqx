# 给定一个字符串（以字符数组的形式给出）和一个偏移量，根据偏移量原地旋转字符串(从左向右旋转)。
#
# 样例
#
# 样例 1:
#
# 输入: str="abcdefg", offset = 3 输出: str = "efgabcd"  样例解释: 注意是原地旋转，即str旋转后为"efgabcd"

str1 = input("请输入字符串：")
offset = int(input("请输入偏移量："))
# str1 ="abcdefg"
# offset = 4
l = len(str1)
str2 = str1[-offset:]
str3 = str1[:l-offset]
str4 = str2+str3
print(str4)