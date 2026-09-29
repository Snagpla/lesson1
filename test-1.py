secret = 27
attempts = 0 
won = False 

while attempts < 5:
    guess = int(input ("Guess the secret number (1-50): "))
    attempts +=1

    if guess == secret:
        print (" you won! you guessed the secret number!")
        won = True
        break

    difference = abs (secret - guess)

    if difference <= 3:
        print ("Hot!")
    elif difference <=10:
        print ("warm")
    elif difference <=20:
        print ("cold")
    else:
        print ("Icey cold")

    remaining = 5 - attempts

    print ("Remaining lives: ", end= "")
    for i in range (remaining):
        print ("❤️", end="")

if not won:
    print ("you ran out of attempts")
    print ("The secret number was:", secret)