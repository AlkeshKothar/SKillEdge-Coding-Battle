try:
    def Likes(list1):
        if not list1:
            print("No one liked this")                                                          #for no likes
        
        elif len(list1)==1:
            print("{} liked this".format(list1[0]))                                             #for single item
    
        elif len(list1)== 2:
            print("{} and {} liked this".format(list1[0],list1[1]))                             #for dual items
    
        elif len(list1)==3:
            print("{}, {} and {} liked this".format(list1[0],list1[1],list1[2]))                 #for triple item
    
        else:
            print("{}, {} and {} other liked this".format(list1[0],list1[1],len(list1) - 2))     #for more than 3 items

    if __name__=="__main__":
        list1 = []
        n = int(input("Enter number of People : "))        #user will give input
        for i in range(0, n):
            names = str(input("Enter name : "))
            list1.append(names)

    Likes(list1)
    print('\nExamples of few input are as below')
    Likes([])
    Likes(["Peter"])
    Likes(["Jacob","Alex"])
    Likes(["Max","John","Mark"])
    Likes(["Alex","Jacob","Mark","Max"])

except:
    print("Invalid Input: Please choose a valid Input")