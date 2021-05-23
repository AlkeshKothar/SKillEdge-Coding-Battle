x= int(input("Enter the No of Rows "))


for i in range(1,x+1):  #1,2,3,4,5,6
    if i==1:

        for j in range(1,i+1):
            print(j,end=" ")
    elif i>2 and i<x:
        for j in range(1,i+1):   #i=2,3,4   12   123  1234  12345
            if j == 1:
                print(j,end="")
            elif j== i:
                print(" " * (i-1),end="")
                print(j,end=" ")
            else:
                print(" ",end="")

    else:
        for j in range(1,i+1):
            print(j,end=" ")

    print()