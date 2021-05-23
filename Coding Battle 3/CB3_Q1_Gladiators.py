n= int(input("Enter the No of Patters you wish to see:"))
if n == 0:
    print("Invalid input")
else:
    #for printing rows
    for i in range(1,n+1):
        # for printing columns
        for j in range(1,i+1):
            print(j,end=" ")
        # for printing numbers in decreasing order
        for j in range(i-1,0,-1):
            print(j,end=" ")
        print()
