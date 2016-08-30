import random
amountOfPicks = input ("Please enter the amount of picks you would like")
#while amountOfPicks != amountOfPicks.isnumeric():
#    amountOfPicks = input("Please enter the amount of picks you would like")
quickPicks = []
secondCounter = 0
counter = 0
numbers = 6
#while secondCounter < int(amountOfPicks):
while counter < numbers:
    quickPicks.append(random.randrange(1,45))
    counter += 1
    #secondCounter =+1
print(quickPicks[::])