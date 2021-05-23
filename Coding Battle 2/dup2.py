x= 5


for i in range(1,x+1):

    if i == 1:

        for j in range(1,i+1):

            print(" " * (x-i),end="")
            print("1",end="")

    elif i>1 and i<x:



        for j in range(1,x-i+1):
            print(" ",end="")
    
        for j in range(1,i+1):   #i=2,3,4   
            if j == 1:
                print(j,end="")
            elif j== i:
                print(j,end=" ")
            else:
                print(" ",end="")




    else:
        for j in range(1,x+1):
            print(j,end=" ")
    print()