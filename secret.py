import random

secret = random.randint(1, 20)

guess = int(raw_input("Can you guess the secret number (pick a number between 1 and 20)?"))

if guess == secret:
    print "Congratulations! You guessed correctly!"
elif guess > 20 or guess < 1:
    print "Please pick a number between 1 and 20"
else:
    print "Sorry - your guess was wrong - the secret number is " + str(secret)

