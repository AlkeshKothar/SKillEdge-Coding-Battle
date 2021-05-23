try:
    def pattern(n):
        n=int(n)
        if n<=0:
            print("Zero and negative numbers are not allowed")
        else:
            for i in range(1,n+1):
                if i == 1:
                    print(i)
                else:
                    print(f"{i}"+f"*{i}"*(i-1)) #pattern 1 i.e. i*i
            for i in range(n,0,-1):
                if i == 1:
                    print(i)
                else:
                    print(f"{i}"+f"*{i}"*(i-1)) #prints reverse pattern 1 

    if __name__=="__main__":
        n = int(input("Enter the Number of Rows of Patter: "))
        pattern(n)

        print("\nOutput of Different Test Case as below")

        print("Test Case with Input as 3\n")
        pattern(3)

        print("\nTest Case with Input as 1")
        pattern(1)

        print("\nTest Case with Input as 0")
        pattern(0)

        print("\nTest Case with Input as y ie String")
        pattern("y")
except Exception as e :
    print("Invalid Input:Input should be Number")