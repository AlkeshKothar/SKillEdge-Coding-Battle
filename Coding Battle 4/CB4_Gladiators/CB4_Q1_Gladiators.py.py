try:
    def draw(n):
        n = int(n)
        if n<=0:
            print("Zero and negative numbers are not allowed")
        else:
            for i in range(n): 
                print(" "*(n-i)+"* "*(i+1)) #pattern 1 --> pyramid
            for i in range(n):
                print(" "*i + " *"*(n-i))  #pattern 2 --> reverse pyramid
    
    if __name__=="__main__":
        inp1 = int(input("Enter the Number of Rows of Patter: "))
        draw(inp1)                                     

except:
    print("Invalid Input, Please enter No. as Input")


#Test cases:

'''
Test case 1:
Input = 5
output : * 
        * *
       * * *
      * * * *
     * * * * *
     * * * * *
      * * * *
       * * *
        * *
         *


Test case 2:
Input = 0
output : Zero and negative numbers are not allowed

Test case 3:
Input = -2
output : Zero and negative numbers are not allowed

Test case 4:
Input = 7.5
output : Zero and negative numbers are not allowed
'''