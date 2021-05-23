n= int(input("Enter the No of Patters you wish to see:"))
stars= 9                                                    #we set a count of "*" before i
lasts = 8                                                   #we set a count of "*" after i
for i in range(1,n+1):                                      #No of times, we run loop in range n
                                       #We use length 17 as its the optimim for single digit no
    b= str(i)
    d= "*"
    z=(b+d)*i                                           #joining no and * after it, int to str then added
        
    print("*" * (stars-i),end="")                       #prints * befre no  
    print(z,end="")                                     #prints number + * 
    print("*"*(lasts-i),end="")                         #prints * after no
    print()   
                                                  #we break the loop as required only once for each 1
        
