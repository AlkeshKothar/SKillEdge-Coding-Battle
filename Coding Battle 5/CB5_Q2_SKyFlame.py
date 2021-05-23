try:
    def draw(n):
        k=1
        if n==0:
            print("Input should be more than Zero")
        for i in range(n):                              #prints the upper half of patter
            for j in range(i):
                print(k,end="*")                        #print number with ending *
                k+=1
                j+=1
                j-=1
            for j in range(i+1,i+2):                    #print the end digit with no ending * 
                print(k,end="")
                k+=1
            print()

        for i in range(n,0,-1):                         #prints the lower half of patter
            k-=i
            if i ==n:
                for j in range(i-1):                    #print the first line of lower pattern
                    print(k,end="*")
                    k+=1
                for j in range(1):                      
                    print(k,end="")
                    k=k-2
                print()
            else:
                k=k-i+2
                for j in range(i-1):                    #prints number with ending *
                    print(k,end="*")
                    k+=1
                for j in range(1):                      #prints the digit with no ending *
                    print(k,end="")
                    k=k-2
                print()

    if __name__=="__main__":
        n = int(input("Enter the Number of Rows of Patter: "))
        draw(n)

        print("\nOutput of Different Test Case as below")

        print("Test Case with Input as 3\n")
        draw(3)

        print("\nTest Case with Input as 1")
        draw(1)

        print("\nTest Case with Input as 0")
        draw(0)

        print("\nTest Case with Input as y ie String")
        draw("y")

except:
    print("Invalid Input:Input should be Number")