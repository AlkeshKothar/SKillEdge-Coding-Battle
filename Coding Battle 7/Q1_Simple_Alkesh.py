n = 9
flag=0
print(" " * (n-1)+ "*")
for i in range((n-1),1,-1):
    print(' ' * (i-1),end="")
    print("*",end="")
    print(' ' * flag,end="")
    print("*",end="")
    print(' ' * flag,end="")
    print("*",end="")
    flag+=1
    print()
print("*" * ((n*2)-1))
flag-=1
for i in range(n-2):
    print(' ' * (i+1),end="")
    print("*",end="")
    print(' ' * flag,end="")
    print("*",end="")
    print(' ' * flag,end="")
    print("*",end="")
    flag-=1
    print()
print(" " * (n-1)+ "*")