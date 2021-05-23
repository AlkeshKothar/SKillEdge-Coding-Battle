n = int(input("Enter the No of Rows of Pattern you wish to see: "))     #taking the number of rows in the pattern

lst = (list(range(1,n+1)))                                              #creating list using range 



for i in range(len(lst), 0, -1):                                        #loop from length of list to 0 as it jumps -1
    x = lst[:i:]                                                        #putting the required sublist in a variable
    for i in x:                                                         #printing the numbers in the list
        print(i, end=" ")
    print("")