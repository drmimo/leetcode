def reverse(x):
        #Starting first with reversing the integer
	#Trying all the time to use a pythonic way
        reverseAbs = int(str(abs(x))[::-1])

	#Checking if the integer is negative
        if x < 0:
	#When  it is negative we check if it doesn't pass the 32-bits representation
            if -reverseAbs < -2147483648:
		#If it passes the 32-bits representation, we return a 0
                return 0
            else:
		#If it doesn't pass 32-bits representation, we return the negative reversed integer
                return -reverseAbs
        else:
	#When the integer is positive
            if reverseAbs > 2147483647:
		#If it passes the 32-bits representation of a positive number, we got a 0
                return 0
            else:
		#If it is represented in less than 32-bits, we give it as return value
                return reverseAbs

#321
print(reverse(123))

#-12
print(reverse(-21))
