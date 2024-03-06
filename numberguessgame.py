import  random
number = random.randint(0,10)
history = []
guess_history = history

while True:
    guess = int(input("Guess a number"))
    history.append(guess)
    if guess == number:
        print ("Congratulations, you got the number correct. Here are your previous guesses." ,print(guess_history))
        break
    print(guess_history),

if guess != number:
    if guess > number:
        print( guess,"is higher than the actual number")
if guess != number:
    if guess < number:
        print( guess, "is lower than the actual number")