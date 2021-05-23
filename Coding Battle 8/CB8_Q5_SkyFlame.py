try:
    def backSpace(S):
        list1=[]

        for char in S:
            if char != "#":                 #add elements to list
                list1.append(char)
            if char == "#":
                if len(list1)>0:            #use pop to remove whenever we encounter, but if len is 0, skip as ntg to del
                    list1.pop()
        a = ""
        finalString = a.join(list1)
        return finalString
    if __name__=="__main__":
        s= input("Enter a string : ")
        print(backSpace(s))
        print("Test cases:") 
        print("Output for -->abc#d##c")
        print(backSpace("abc#d##c"))
        print("Output for -->abc##d######")
        print(backSpace("abc##d######"))
        print("Output for -->######")
        print(backSpace("######"))
except:
    print("Error Occured")