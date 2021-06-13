try:
    def add_letters(list2):

        list1= ['z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l','m','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
        suma = 0
        
        for i in list2:
            z=list1.index(i)            #grab the index postion from list1 a, add it to sum
            suma += z

        if suma>26:
            suma = suma-26              #handle overflow by simply subtracting 26 if more than 26

        output= list1[suma]             #return the value corresponding to suma, ie index
        print("Your output is : {}".format(output))

    if __name__=="__main__":
        list2 = []
        n = int(input("Enter the number of arguments : "))        #user will give input
        for i in range(0, n):
            input_letter = str(input("Enter letter {} : ".format(i+1)))
            final_letter = input_letter.lower()                   # user need not to worry about upper or lower case
            list2.append(final_letter)

        add_letters(list2)
        print("\nBelow are few Test Cases")
        add_letters(['a','b','c'])
        add_letters(['a','b'])
        add_letters(['z'])
        add_letters(['z','a'])
        add_letters(['y','c','b'])
        add_letters([])

except:
    print("Invalid Input: Please choose a valid Input")
