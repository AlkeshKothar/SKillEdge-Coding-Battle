n = int(input("Enter the No of Rows of Pattern you wish to see: "))     #taking the number of rows

if n == 0:                                                              #checking if we have valid input
    print("invalid input")
else:
    lst = (list(range(1,n+1)))                                          #creating a list with values from 1 to n

    for i in range(0, len(lst)):    
        x = lst[: i + 1 :]                                              #putting the sub list in a variable
        for i in x:                                                     #PRINTING THE NUMBERS IN THE VARIABLE
            print(i, end=" ")
        print("")