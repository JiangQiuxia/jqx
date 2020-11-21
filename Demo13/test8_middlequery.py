# 二分查找法是一种查找有序序列中元素位置的方法，每次查找会用需要查找的数和序列的中值比较大小，如果大于中值，则查找后半部分，如果小于中值，则查找前半部分；
# 接下来在刚才定位的半部分中继续取中值。。。直到查找到当前元素的位置。比如有这样一个有序序列li = [1,2,3,4,5,6,7,8,9,10]，我们需要查找8的位置；
# 那么第一次查找时取中值就是下标4的元素，也就是5，5比8小，那么接下来就在[6，7,8,9,10]中继续查找。直到找到这个元素。现在要求定一个函数，
# 输入一个序列和一个需要查找的值。返回该值所在的位置，并统计比较的次数。

def middle_query():
    str1 = input("请输入有序序列:")
    list1 =str1.split(",")
    value1 = int(input("请输入需要查找得值："))
    count1 = 0
    l = len(list1)
    while True:
        middleValue = int(list1[l // 2])
        count1 += 1
        if middleValue > value1:
            l //= 2
            list1 = list1[0:l]
        elif middleValue < value1:
            l //= 2
            list1 = list1[l:-1]
        elif middleValue == value1:
            print(f"{value1}所在的位置是第{l//2+1}位；统计次数：{count1}")
            break

if __name__ == '__main__':
    middle_query()
