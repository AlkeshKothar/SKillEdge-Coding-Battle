#Alkesh

n = int(input("Enter the no of rows of Traingle"))
for i in range(0,n):   #0 1 2 3 
    for s in range(0,n-i-1):   # 
        print(end=" ")
    for j in range(0,i+1):
        if ((i>=2 and i<n-1) and (j>0 and j<i)):
            print(end="  ")
        else:
            print("*",end=" ")
    print()