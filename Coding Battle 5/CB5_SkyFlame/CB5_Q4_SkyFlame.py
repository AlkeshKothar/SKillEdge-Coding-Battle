try:
    def draw(n):
        k=1                                                 #start no from 1 to so on
        if n<=0:
            print("Input should be greater than Zero")
        else:
            for i in range(n):
                for j in range(i+1):                        #prints no as in range and increments by 1
                    print(k,end=" ")
                    j+=1    
                    j-=1
                    k+=1
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