try:
    def find_uniq(list1):
        if list1[0]!= list1[1] and list1[1] == list1[2]:
            print("The Unique Value is : {}".format(list1[0]))      #first check if 1st element is unique
        else:
            for i in range(len(list1)):
                if list1[i] != list1[i+1]:                          #else, just compare adjacent, the unique turns out and break
                    print("The Unique Value is : {}".format(list1[i+1]))
                    break

    if __name__=="__main__":
        list1= []
        n = int(input("Enter the number of elements : "))            #user input for n no. of inputs
        for i in range(0, n):
            number = int(input("Enter the numbers : "))
            list1.append(number)

    find_uniq(list1)
    print("\nBelow are some usecases")
    find_uniq([1,1,1,2,1,1])
    find_uniq([0,0,0.55,0,0])

except:
    print("Please Enter only numbers")


        #code with sort funtion but high complexity
        #list2 = sorted(list1)                                       #sort the array
        #if list2[0] != list2[1]:
        #    print("The Unique Value is : {}".format(list2[0]))      #if unique is smaller, its the index 0 surely
        #else:
        #    print("The Unique Value is : {}".format(list2[-1]))     #if unique is larger, its the last index -1 surely
