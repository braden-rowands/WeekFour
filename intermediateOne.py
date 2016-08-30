cycles = int(5)
numbers = []
for i in range (1,cycles+1):
    number = int("Please enter a positive whole number")
    numbers.append(number)

firstNumber = numbers[0]
print("first number is {}".format(firstNumber))

lastNumber = numbers [5]
print("last number is {}".format(lastNumber))

for i in numbers:
    smallest = numbers [0]
    if numbers < smallest:
        smallest = numbers
    i += 1

for i in numbers:
    highest = numbers [0]
    if numbers > highest:
        highest = numbers
    i += 1

for i in numbers:
    total = numbers + numbers
    i += 1
average = total / 5

