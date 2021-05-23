try:
    def camelCase(line1):

        line2= ""                           #we create a blank string, that we will use to return the answer
        for letter in line1:                
            if letter.isupper():            # .isupper() fun checks if letter is uppercase or lowercase
                line2 += " " + letter       # if its upper, we say add a space and the letter, hence we used a blank
            else:
                line2 += letter             # if its lower, we say add it as it is as its a same word
        return line2

    if __name__=="__main__":
        line1=input("Enter the string : ")
        a= camelCase(line1)
        print(a)
        
        print("\n Test case with input: TTT")
        b= camelCase("TTT")
        print(b)

        print("\n Test case with input: theWorldIsGood")
        c= camelCase("theWorldIsGood")
        print(c)
except:
    print("Invlaid Input: Please enter string")