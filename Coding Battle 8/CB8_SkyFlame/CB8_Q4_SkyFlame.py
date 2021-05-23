try:
    def encode(msg):
        encoded_msg= ""
        for char in msg:                        #loop checks if vowel, and replaces with adjacent value
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
                encoded_msg+=char               #if not vowel, simply add
        return encoded_msg

    def decode(msg):
        decoded_msg= ""
        for char in msg:                        #loop checks if vowel, and replaces with adjacent value
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
                decoded_msg+=char               #if not vowel, simply add
        return decoded_msg

    if __name__=="__main__":
        msg=input("Enter your message: ")
        c= int(input("Select your choice: \nPress 1 to encode and Press 2 to decode : "))
        if c == 1:
            a= encode(msg)
            print("Your Encoded message is :", a)
        if c== 2:
            b= decode(msg)
            print("Your Decoded message is :", b)

        print("\nTestCase for encode 'Hello'")
        print(encode("hello"))
        print("\nTestCase for decode 'h2ll4'")
        print(decode("h2ll4"))
        

        
except:
    print("Please Enter the input correclty and select you choice as 1 and 2 only")