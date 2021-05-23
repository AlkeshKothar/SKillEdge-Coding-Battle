try:
    def draw(n):
        if n<=0:
            print("Input should be more than 0")
        elif n==1:
            print("*")
        else:

            i=1
            while i<n:                      #print the upper half portion pattern ie. start to max(n)
                print("*" * i)          
                i+=1
                if i == n:
                    a= n
                    while a>=0:             #print the lower half portion patter ie. max to start(1)
                        print("*" * a)
                        a-=1

    if __name__=="__main__":


        inp1 = int(input("Enter the Number of Rows of Patter: "))
        draw(inp1)


except:
    print("Invalid Input, Please enter No. as Input")


'''
Enter the Number of Rows of Patter: 5
*
**
***
****
*****
****
***
**
Enter the Number of Rows of Patter: 3
*
**
***
**
*

Enter the Number of Rows of Patter: 0
Input should be more than 0    


Enter the Number of Rows of Patter: y
Invalid Input, Please enter No. as Input
'''