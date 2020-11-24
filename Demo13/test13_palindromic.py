'''输入: 121
输出: true
示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。'''

def palindromic(number):
    str1 = str(number)
    str2 = str1[::-1]
    if str1==str2:
        return True
    else:
        return False

if __name__ == '__main__':
    print(palindromic(9))