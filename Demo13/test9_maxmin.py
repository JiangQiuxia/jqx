# 一些四位数,百位数字都是3,十位数字都是6,并且它们既能被2整除,又能被 3整除,
# 求这样的四位数中最大的和最小的两数各是几?

def maxandmin():
    list1 = []
    for number in range(1000, 10000):
        if number % 2 == 0 and number % 3 == 0:
            str_number = str(number)
            if str_number[1] == '3' and str_number[2] == '6':
                list1.append(number)
    max_value = max(list1)
    min_value = min(list1)
    print(min_value,max_value)

if __name__ == '__main__':
    maxandmin()
