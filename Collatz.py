def collatz(number):
	if number % 2 == 0:	# If number divided (modulus) has no remainder -- is evenly divisible by two
		return number // 2 # Then return number divided by (floor-no remainder) type. Note that this isn't the .XX value, its if the number 7 is divided by 2, there is only one evenly leftover
	elif number % 2 == 1:  # If the number has one left over from modulo math
		return 3 * number + 1 #then multiply number by three and then add one
print("Please enter a number")

try:				# Try (exception handling)
	number = int(raw_input()) # Manually put in the number variable
	while number != 1:     # Run program while number doesn't equal zero
		collatz(number)    # Run the collatz function on the number variable
		print number	# Print the result
		number = collatz(number)  # change value of number to the result
	else:
		print('You win. The number is now one!')   # if the loop ends, print this
except ValueError:
		print('Please enter an integer')			# If there is a value error, as in you input a string, this wil lreturn
	