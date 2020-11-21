# for i in range(1, 10):
#     for j in range(1, i + 1):
#         sum1 = i * j
#         print(str(i) + "*" + str(j) + "=" + str(sum1),end =" ")
#         if i == j:
#             print("\n")

# list1 = [9,8,7,6,5,4,3,2,1]
# for i in list1:
#     for j in range(1,i+1):
#         sum1 = i * j
#         print(str(i) + "*" + str(j) + "=" + str(sum1),end =" ")
#         if i == j:
#             print("\n")

for i in range(9,0,-1):
    for j in range(1,i+1):
        sum1 = i * j
        # print(str(i) + "*" + str(j) + "=" + str(sum1),end =" ")
        print(f"{i}*{j}={sum1}", end=" ")
        if i == j:
            print("\n")
