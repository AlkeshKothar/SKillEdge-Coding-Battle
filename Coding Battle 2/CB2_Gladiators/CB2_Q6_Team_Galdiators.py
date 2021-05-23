#Alkesh, we run loop once as there's no mentioned of space complexity, so peference to time complexity.


x = int(input("Enter the No of Rows of Pattern you wish to see:"))  #taking the number of rows
list1= list1 = (list(range(0,x+1)))                                 #we are creating a list to grab element as per index value


for i in range(1,x+1):                                              #no of rows, the loop shall go  

    if i>1 and i<x-1:                                               #to modify changes rows from second to third last
        a= x - (i+1) 
        print(list1[i], "   " * a , list1[-1],end= "")              #we print first and last value with added spaces here
        
    else:                       
        for j in range(i,x+1):                                      #simply print the last statesments
         print(j,end="  ")
    print()