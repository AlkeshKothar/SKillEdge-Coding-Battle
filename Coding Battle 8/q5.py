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
    
except:
    pass

s= "abc##d######"
b= backSpace(s)
print(b)