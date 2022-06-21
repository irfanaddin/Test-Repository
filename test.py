print("Welcome to NBA Questionaire to test your NBA knowledge! Lets see how far you get, you get to play with 6 fouls! Try not to foul out! ")
name = input("What is your name? ")
age = int(input("How old are you?  "))

print("Hello", name, "you are", age, "years old. ")
fouls = 0
score = 0
if fouls >= 6:
    print("Fouled out! Keep your hands to yourself Patrick Beverly 2.0! ")
if age >= 13:
    print("Great! You are old enough to play! ")
    wants_to_play = input("Would you like to continue to the game?         (YES or NO) ").lower()
else:
    print("Sorry, you are not old enough to play.")

####################  
  
if wants_to_play == "yes":
    print("What time is it? ITS NBA GAME TIME!")

####################
      
LVL1A = input("This is LVL1A. A. correct or B. incorrect").upper()

  
if LVL1A == "A":
    LVL2A = input("This is LVL2A. A. correct or B. incorrect").upper()
    score += 100

else:
    LVL2B = input("This is LVL2B.  A. correct or B. incorrect").upper()
    fouls += 1
    score -= 50

       
####################

if LVL2A == "A":
    LVL3A = input("This is LVL3A. A. correct or B. incorrect").upper()
    score += 100

else:
    LVL3B = input("This is LVL3B. A. correct or B. incorrect").upper()
    fouls += 1
    score -= 50

####################

if LVL2B == "A":
    LVL3B = input("This is LVL3B.  A correct  B. incorrect").upper()
    score += 100
else:
    LVL3C = input("This is LVL 3C.  A. correct  B. incorrect").upper()
    score -= 50
    fouls += 1

####################
      
if LVL3A == "A":
  LVL4A = input("This is LVL4A. A. correct or B. incorrect").upper()
  score += 100

else:
  LVL4B = input("This is LVL4B. A. correct or B. incorrect").upper()
  fouls += 1
  score -= 50

if LVL3B == "A":
    LVL4B = input("This is LVL4B. A. correct  or B. incorrect")
else: 
    LVL4C = input("This is LVL4C.  A. correct or B. incorrect" )

####################
      
if LVL4A == "A":
  LVL5A = input("This is LVL5A. A. correct or B. incorrect").upper()
  score += 100

else:
    LVL5B = input("This is LVL5B. A. correct  B. incorrect").upper()
    score -= 50
    fouls += 1


if LVL4B == "A":
    LVL5B = input("This is LVL5B. A. correct  B. incorrect").upper()
    score += 100
else:
    LVL5C = input("This is LVL5C.  A. correct  B. incorrect").upper()
    score -= 50
    fouls += 1


if LVL4C == "A":
    LVL5C = input("This is LVL5C.  A. correct  B. incorrect")
    score += 100
else:
    LVL5D = input("This LVL5D.  A. correct  B. incorrect")
    score -= 50
    fouls += 1

    #
    ##
    #
    ##
    ####################

if LVL5A == "A":
    print("You win!")
    print("Your final score is", score, "and you had", fouls, "fouls.")

else:
    print("You lose!")
    print("Your final score is", score, "and you had", fouls, "fouls.")

if LVL5B == "A":
    print("You win!")
    print("Your final score is", score, "and you had", fouls, "fouls.")

else:
    print("You lose!")
    print("Your final score is", score, "and you had", fouls, "fouls.")

if LVL5C == "A":
    print("You win!")
    print("Your final score is", score, "and you had", fouls, "fouls.")

else:
    print("You lose!")
    print("Your final score is", score, "and you had", fouls, "fouls.")

if LVL5D == "A":
    print("You win!")