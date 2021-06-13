try:
    def odd_Ascender(list1):
        for i in range(len(list1)):
            for j in range(i+1,len(list1)):
                if list1[i] % 2 !=0 and list1[j] % 2 !=0 and list1[i]> list1[j]:  #if no is odd, also LHS < RHS
                    list1[i],list1[j] = list1[j],list1[i]                         #if LHS < RHS, swap as we need assending order
        print(list1)

    if __name__=="__main__":
        list1= []
        n = int(input("Enter the number of elements : "))            #user input for n no. of inputs
        for i in range(0, n):
            number = int(input("Enter the numbers : "))
            list1.append(number)
    
    odd_Ascender(list1)
    print("Below are some Test Case")
    odd_Ascender([7,1])
    odd_Ascender([5,8,6,3,4])
    odd_Ascender([9,8,7,6,5,4,3,2,1,0])
    
except:
    print("Please Enter only numbers")