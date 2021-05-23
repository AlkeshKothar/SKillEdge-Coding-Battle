try:
    def encode(msg):
        encoded_msg= ""
        for char in msg:
            if char =="a":
                encoded_msg=encoded_msg+"1"
            elif char =="e":
                encoded_msg=encoded_msg+"2"
            elif char =="i":
                encoded_msg=encoded_msg+"3"
            elif char =="o":
                encoded_msg=encoded_msg+"4"
            elif char =="u":
                encoded_msg=encoded_msg+"5"
            else:
                encoded_msg+=char
        print("Your Encoded message is : ",encoded_msg)

    def decode(msg):
        decoded_msg= ""
        for char in msg:
            if char =="1":
                decoded_msg=decoded_msg+"a"
            elif char =="2":
                decoded_msg=decoded_msg+"e"
            elif char =="3":
                decoded_msg=decoded_msg+"i"
            elif char =="4":
                decoded_msg=decoded_msg+"o"
            elif char =="5":
                decoded_msg=decoded_msg+"u"
            else:
                decoded_msg+=char
        print("Your Decoded message is : ",decoded_msg)

    if __name__=="__main__":
        msg=input("Enter your message: ")
        c= int(input("Select your choice: \nPress 1 to encode and Press 2 to decode : "))
        if c == 1:
            a= encode(msg)
        if c== 2:
            b= decode(msg)
except:
    print("Please Enter the input correclty and select you choice as 1 and 2 only")