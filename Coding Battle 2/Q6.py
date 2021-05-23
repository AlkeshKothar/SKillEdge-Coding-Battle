x = int(input("Enter the no of rows"))
list1= list1 = (list(range(0,x+1)))


for i in range(1,x+1):          #1,2,3,4,5

    if i>1 and i<x-1:
        a= x - (i+1) 
        print(list1[i], "   " * a , list1[-1],end= "")   #i=2
        
    else:
        for j in range(i,x+1):
         print(j,end="  ")
    print()