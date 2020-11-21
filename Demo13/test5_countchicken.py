for i in range(0,101):
    for n in range(0,101):
        for m in range(0,101):
            if i+n+m ==100 and i*5+3*n+(1/3)*m == 100:
                print(f"公鸡：{i},母鸡：{n},小鸡{m}")
