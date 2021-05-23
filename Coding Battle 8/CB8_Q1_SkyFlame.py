try:
    def parts_sum(ls):
        if len(ls)==0:                              #zero will be added at last postion hence
            final_list = [0]
            return final_list
        else:
            final_list = []                         #create a empty list which we will return
            count = len(ls)

            while count>0:                          #loop as no of times of element
                new_ele = sum(ls)                           
                final_list.append(new_ele)          #sum and add to list we created
                ls.pop(0)
                count-=1
            final_list.append(0)                    #add "0" at last and return the list
            return final_list

    if __name__=="__main__":
        temp_list = []
        n = int(input("Enter the list size : "))   #take list from user
        if n<=0:
            print("The size should be atleast more than Zero")
        else:
            for i in range(1, n+1):
                print("Enter the element",i)
                item = int(input())
                temp_list.append(item)
            a= parts_sum(temp_list)
            print("The solution is: ",a)

        print("\nTest case for list [1,2,3,4,5,6]")
        print(parts_sum([1,2,3,4,5,6]))

except:
    print("Plese enter elemetns one by one correctly")
