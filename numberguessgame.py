import  random
number = random.randint(0,200)
history = []
guess_history = history

while True: 
    guess = int(input("Guess a number"))
    history.append(guess)
    if guess == number:
        print ("Congratulations, you got the number correct.")
        break
    print(guess_history)

q   elif guess != number:
print ("Your guess is lower than the actual number")
if guess > number:
            print ("Your guess is higher than the actual number")   
else:
            print (guess, "is lower than the actual number ")


print (history)

