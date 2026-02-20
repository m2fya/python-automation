numbers = []

count = int(input("How many numbers?: "))

for i in range(count):

	value = int(input("Enter numbers: "))

	numbers.append(value)

print(numbers)
print(len(numbers))
print(min(numbers))
	
