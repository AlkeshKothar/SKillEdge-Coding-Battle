try:
    def draw(n):
        list1=[]
        if n<=0:
            print("Input should be atleast greater than Zero")
        
        else:
            for i in range(n):  
                temp=[]                                                 #create temp list
                for j in range(i+1):
                    if j==0 or j==i:                                    #adding 1 in start and end
                        temp.append(1)
                    else:
                        temp.append(list1[i-1][j-1] + list1[i-1][j])    #adding the sum of (index postion of curenet and previous)
                list1.append(temp)                                      #add current list as element in list1
            
            for i in range(n):
                for j in range(i+1):
                    print(list1[i][j],end=' ')                           #print the list1 
                print()


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
     print("Invalid Input: Please choose a valid Input")