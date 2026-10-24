# Topics: loops, if-elif-else, comparisons, counter, break.
# Fixed secret number keeps this example within the syllabus topics.
secret = 37
found = False
print("Guess the number from 1 to 100. You have 5 attempts.")
for turn in range(1, 6):
    guess = int(input("Attempt " + str(turn) + ": "))
    if guess == secret:
        print("Correct! You guessed the number.")
        found = True
        break
    elif guess < secret:
        print("Too low.")
    else:
        print("Too high.")
if found == False:
    print("Game over. The number was", secret)
