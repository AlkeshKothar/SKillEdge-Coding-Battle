try:
    def draw(n):   
        a=3
        n = int(n)
        if n<=0 :                                       #checker as for 0 and 1, the pattern wont run
            print("Input should be more than 0")

        elif n==1:
            print("*")
            print("*")
        else:
            for i in range(n):                          #print the  upper part of hollow traingle
                if i>1:
                    print(" " * (n-i-1),end="")             
                    print("*"   ,end="")
                    print(" " * a  ,end="")
                    print("*"   ,end="")
                    a+=2            
                    print()
                else:
                    print(" "*(n-i-1)+"* "*(i+1))
                    
                    
            for i in range(n,0,-1):                     #print the lower part of hollow traingle
                if i>1:
                    print(" "* (n-i),end="")
                    print("*",end="")
                    print(" "* (a-2),end="")
                    print("*",end="")
                    a-=2
                    print()
                else:
                    print(" "*(n-i-1)+" * "*(i))

    if __name__=="__main__":
        inp1 = int(input("Enter the Number of Rows of Patter: "))
        draw(inp1)

except:
    print("Invalid Input, Please enter No. as Input")


'''Test Cases
Enter the Number of Rows of Patter: 5
    * 
   * *
  *   *
 *     *
*       *
*       *
 *     *
  *   *
   * *
    *

Enter the Number of Rows of Patter: 3
  * 
 * *
*   *
*   *
 * *
  *
Enter the Number of Rows of Patter: 0
Input should be more than 1

Enter the Number of Rows of Patter: start
Invalid Input, Please enter No. as Input
'''