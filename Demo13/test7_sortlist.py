# [1,2,3,4,5,22,34,11,45,8]
list1 = [1,2,3,4,5,22,34,11,45,8]
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] > list1[j]:
            # temp = list1[j]
            # list1[j] = list1[i]
            # list1[i] =temp
            list1[i], list1[j] = list1[j], list1[i]
print(list1)





# list1 = [1,2]
# for i in range(0,len(list1)):
#     for j in range(i+1,len(list1)):
#         if list1[i] > list1[j]:
#             list1[j] = list1[i]
#         else:
#             print(list1)
