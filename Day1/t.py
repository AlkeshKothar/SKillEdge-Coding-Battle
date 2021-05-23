row = 4

for i in range(row):
    for j in range(0,row-1-i):
        print(end=" ")
    for j in range(0,i+1):
        print("* ",end="")
    print() 