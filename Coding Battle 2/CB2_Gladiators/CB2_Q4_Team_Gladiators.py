#riya

# no of iterations
n = int(input("Enter the No of Rows of Pattern you wish to see: "))
# initial value
num = 1
# space before numbers
gap = n - 1
for j in range(1, n + 1):
    num = j
    for i in range(1, gap + 1):
        print(" ", end="")
    gap = gap - 1

    # for printing particular interval of numbers
    for i in range(1, j + 1):
        print(num, end="")
        num = num + 1
    # for printing decreasing order
    num = num - 2
    for i in range(1, j):
        print(num, end="")
        num = num - 1

    print()