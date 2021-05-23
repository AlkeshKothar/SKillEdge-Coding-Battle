try:
    def camel(str):
        for i in str:
            if i.isupper()==True:  #checks for the uppercase alphabet
                str = str.replace(i,f" {i}") #adds space before capital alphabet
                  
        print(str)
    str=input("Enter a string :")
    camel(str)

    
    print("Test Cases")
    print("For string --->camelCase")
    camel("camelCase")
    print("For string --->identifier")
    camel("identifier")
    
except Exception as e:
    print("Error occured")