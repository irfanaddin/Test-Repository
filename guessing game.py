import random
secret_number = random.randint(1, 100)

#Asking the player how many attempts they want
attempts = int(input("How many attempts do you want? "))
# Start the game
while True:
# asking what the player's guess is
  guess = int(input("Guess a number between 1 and 100: "))
# Checking here if the guess is correct
  if guess == secret_number:
    print("You guessed it right!")
    break
# Checking to see if the guess is too high or too low

  elif guess > secret_number:
    print("Guess lower")
    attempts -= 1
  else:
    print("Guess higher")
# lowering the number of attempts the user has left
    attempts -= 1
# Checking to see if the player has run out of attempts
  if attempts == 0:
    print("You ran out of attempts!")
    break

# Display the number of remaining attempts

print("You have", attempts, "attempts remaining")
print("The number was", secret_number)