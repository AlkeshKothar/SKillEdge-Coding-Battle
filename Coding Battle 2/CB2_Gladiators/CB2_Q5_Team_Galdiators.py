x= int(input("Enter the No of Rows of Pattern you wish to see:"))  #taking the number of rows


for i in range(1,x+1):                                             #loop no of rows

    if i == 1:                                                     #specially for row1

        for j in range(1,i+1):

            print(" " * (x-i),end="")                              #print spaces before elemt
            print("1",end="")                                      #print the first element as it will be 1 eventually

    elif i>1 and i<x:                                              #to modify changes rows from second to second last

        for j in range(1,x-i+1):            
            print(" ",end="")                                      #print spaces before 1st ele
    
        for j in range(1,i+1):                                      
            if j == 1:
                print(j,end="")                                    #after the spaces, print first ele
            elif j== i:
                print(" " * (i-1),end="")                          #print spaces after 1st print of row
                print(j,end=" ")                                   #if its the last element, print last value
            else:
                print(" ",end="")                                  #if its not the last elementt, print spaces

    else:
        for j in range(1,x+1):                                     #loop once and print last line with no modofications
            print(j,end=" ")
    print()
