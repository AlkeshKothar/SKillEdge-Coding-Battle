
n= int(input("Enter no"))
n= n*2
for i in range(1, n // 2 + 1):
    		
	num1 = n - i
	for j in range(0, num1):
		print(" ", end="")
	star_num = 2 * i  - 1
	for j in range(0, star_num):
		
		if j == 0 or j == star_num - 1 or i == n // 2  or j == star_num // 2:
			print("*", end="")
		else:
			print(" ", end="")
	print("")


      
for i in range((n // 2-1), 0, -1):
	num1 = n - i
	for j in range(0, num1):
		print(" ", end="")
	star_num = 2 * i  - 1
	for j in range(0, star_num):
		if j == 0 or j == star_num - 1 or j == star_num // 2:
			print("*", end="")
		else:
			print(" ", end="")
	print("")





