n= 17
r1 = ((n-1)//2) 
r= n //2
s= 1
q = (r1*3)-2
lit = n+3
for i in range(r1+1):
    if i< (r1):
        print("---" * r + ".|." * s + "---"*r)
        r-=1
        s+=2
    else:
        print("-" * q +"WELCOME" +"-" * q)
s-=2
r+=1
for i in range(r1,0,-1):
    
    print("---" * r + ".|." * s + "---"*r)
    r+=1
    s-=2
''' Notes: 
n   no of lines    no of dash for welcome (formula: ((no of lines *3)-2)  )
7=      3            7
9=      4            10
11=     5            13 
13=     6            16
15=     7            19
17=     8            22
19=     9            25
'''