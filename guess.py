import math


low = int(input("Enter the lower boundary: "))
high = int(input("Enter the higher boundary: "))

max_guesses = math.ceil(math.log(high - low + 1, 2))
print("Think of a number between", low, "and", high)
print("I will guess it in at most", max_guesses, "guesses.")

guesses = 0

while guesses < max_guesses and low <= high:
    guess = (low + high) // 2
    print("My guess is:", guess)

    hint = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ")
    guesses += 1

    if hint == 'c':
        print("I guessed your number in", guesses, "guesses!")
        break
    elif hint == 'h':
        high = guess - 1
    elif hint == 'l':
        low = guess + 1
    else:
        print("Invalid input. Use h, l, or c.")
        guesses -=1

    if low > high:
        print("Cheating detected! Your hints are inconsistent.")
        break
