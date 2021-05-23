x= int(input("Enter the No of Rows of Pattern you wish to see: "))      #taking the number of rows in the pattern


for i in range(1,x+1):  
    if i==1:                                                            #print first num as it is, no modification req
        for j in range(1,i+1):                                          
            print(j,end=" ")
    elif i>2 and i<x:                                                   #to modify pattern form 3rd row to 2nd last    
        for j in range(1,i+1):   
            if j == 1:
                print(j,end="")
            elif j== i:                                                 
                print(" " * (i-1),end="")                               #print space before last value
                print(j,end=" ")                                        #print the value
            else:
                print(" ",end="")                                       #if not last value, smply print space

    else:
        for j in range(1,i+1):                                          #to print last line with no mofidicaton
            print(j,end=" ")

    print()