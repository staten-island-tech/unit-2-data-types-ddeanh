import  random
number = random.randint(0,200)
history = []

while True: 
    guess = int(input("Guess a number"))
    history.append(guess)
    if guess == number:
        print ("Congratulations, you got the number correct.")
        break
    else:
        if guess != number:
            print ("Incorrect")
        if guess > number:
            print ("Your guess is higher than the actual number")   
else:
            print ("Your guess is lower than the actual number")
