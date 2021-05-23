#Alkesh

x =   int(input("Enter the no of rows"))
list1= list1 = (list(range(1,x+1)))

for i in range(1,x+1):
    
    
    if (i>=3 and i<x):
        a = i-1
        print(list1[0], "   " * (i-2), list1[a], end=" ")
    else:
        for j in range(1,i+1):
            print(j, end="  ")
        
    print()