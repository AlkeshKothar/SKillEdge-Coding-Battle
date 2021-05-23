#Payal


input = int(input("Enter the no of rows"))
for i in range(input):
    for j in range(input):
        if j==0 or i==0 or i+j==(input-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()