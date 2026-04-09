the_space = input("How many pieces of space are avaiable?")
the_space = float(the_space)

a = the_space % 2

print (a)

if a > 1:
    print("正在种植西兰花")

else:
    print("正在种植花椰菜")