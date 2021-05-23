try:
    def draw(n):
        if n<=0:
            print("Input No should be greater than zero")
        if n==1:
            print("*")
            print("*1*")
            print("*")    
        else:
            for i in range(1,n+1):                      #print upper half of pattern
                if i==1:
                    print("*")
                    print("*1*",end="")             
                if i>1:
                    print("*",end="")                   
                    for j in range(1,i):                #incremental series
                        print(j,end="")
                    for i in range(j+1,0,-1):           #decremental series
                        print(i,end="")
                    print("*",end="")
                print()
            for i in range(n-2,-1,-1):                  #print lower half of pattern
                if i>0:
                    print("*",end="")
                    for j in range(1,i+1):              #incremental series 
                        print(j,end="")
                    for k in range(j+1,0,-1):           #decremental series
                        print(k,end="")
                    print("*",end="")
                    print()
                if i==0:
                    print("*1*")
                    print("*")
    if __name__=="__main__":
        n = int(input("Enter the Number of Rows of Patter: "))
        draw(n)

        print("\nOutput of Different Test Case as below")

        print("Test Case with Input as 3\n")
        draw(3)

        print("Test Case with Input as 1\n")
        draw(1)

        print("Test Case with Input as 0")
        draw(0)

        print("Test Case with Input as y ie String")
        draw("y")

except:
    print("Invalid Input:Input should be Number")