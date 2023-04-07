import random

answer = random.randint(1, 100)
counter = 0

# python does not have do-while loop, 
# so while True then break used to do the same functionality
while True:
    counter += 1
    number = int(input("Please input your guess number: "))
    if number < answer:
        print("Your number is smaller than the answer.")
    elif number > answer:
        print("Your number is greater than the answer.")
    else:
        print("Congratz! You got the currect number!")
        break

print("You guessed %d times." %counter)