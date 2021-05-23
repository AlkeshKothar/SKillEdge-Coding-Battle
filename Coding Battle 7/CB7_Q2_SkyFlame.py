try:
    def pattern(n):
        if n<=0 or n%2==0:
            print("Zero, negative and even numbers are not allowed")
        else:
            r1 = ((n-1)//2) 
            q= n-r1-2
            for i in range(0,r1+1):
                if i<r1:
        
                    print("-"*(((n-(i+r1))*3)-3)+".|."*(i+(i+1)) +"-"*(((n-(i+r1))*3)-3))  
                else:
                    print("-" * ((q*3)+1) +"WELCOME" +"-" * ((q*3)+1))
            for i in range(r1-1,-1,-1):
                print("-"*(((n-(i+r1))*3)-3)+".|."*(i+(i+1)) +"-"*(((n-(i+r1))*3)-3)) 
            
               
    if __name__=="__main__":
        n = int(input("Enter the No of Rows you want (Odd No's Only): "))
        pattern(n)
        print("\nTest Cases are as follows:")

        print("Input as zero")
        pattern(0)

        print("Input as negative number")
        pattern(-5)

        print("Input as float number")
        pattern(8.6)


        print("Input as string")
        pattern("z")
        
except Exception as e:
    print("Invalid Input")