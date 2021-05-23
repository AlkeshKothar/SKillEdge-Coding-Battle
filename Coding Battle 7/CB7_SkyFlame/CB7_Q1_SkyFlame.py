try:
    def pattern(n):
        if n<=0 or n%2==0:
            print("Zero, negative and even numbers are not allowed")
        else:
            n= n*2
            for i in range(1, n // 2 + 1):
                num1 = n - i
                for j in range(0, num1):
                    print(" ", end="")
                    num2 = 2 * i  - 1
                for j in range(0, num2):
                    if j == 0 or j == num2 - 1 or i == n // 2  or j == num2 // 2:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print("")


            for i in range((n // 2-1), 0, -1):
                num1 = n - i
                for j in range(0, num1):
                    print(" ", end="")
                num2 = 2 * i  - 1
                for j in range(0, num2):
                    if j == 0 or j == num2 - 1 or j == num2 // 2:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print("")

    if __name__=="__main__":
        n = int(input("Enter the No of Rows you want (Odd No's Only):"))
        pattern(n)
        print("\nTest Cases are as follows:")
        print("Input as zero")
        pattern(0)

        print("Input as negative number")
        pattern(-5)

      
except Exception as e:
    print("Invalid Input")