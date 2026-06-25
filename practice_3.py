def find_extremes(numbers):
	if not numbers:
		return None

	minimum = numbers[0]
	maximum = numbers[0]

	for num in numbers:
		if num < minimum:
			minimum = num
		if num > maximum:
			maximum = num
			
	return minimum, maximum
		
print(find_extremes([5, 2, 9, 1, 7]))
print(find_extremes([-10, 0, 50, 23]))
	  