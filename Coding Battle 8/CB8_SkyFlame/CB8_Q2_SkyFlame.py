try:
    def reverse(num):
        if num<0:
            num = str(num)  #typecasting integer to string
            print(int(num[0] + num[:0:-1]))  #first prints sign of number and then prints reverse of nubmer
        else :
            num = str(num)   #typecasting integer to string
            print(int(num[::-1]))   #prints reverse of number
    num=int(input("Enter a number : "))
    reverse(num)
    print("Test Cases")
    print("Output for --->123")
    reverse(123)
    print("Output for --->-456")
    reverse(-456)
    print("Output for --->1000")
    reverse(1000)
except Exception as e:
    print("Error Occured, Please provide input correctly")