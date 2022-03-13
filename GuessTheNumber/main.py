import random

def guess(x):
    randomno = random.randint(1,x)
    guess=0
    while (guess!= randomno):
        guess= int(input(f"Guess the number between 1 and {x} : "))
        if(guess> randomno):
            print("The number you entered is higher than the alloted number.")
            continue
        elif(guess<randomno):
            print("The number you entered is lower than the alloted number.")
            continue
        elif(guess==randomno):
            print("Congratualations! You guessed it ~~ ;)")
            break

def compguess(y, x):
    low = y
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')


m=1
while m!=0:
    who= int(input(f"Welcome to Guess The Number. Do you want to be the Guess-er(Enter 1) or the Guess-ee(Enter 0) ? :"))
    if (who==1):
        print("\nWelcome Back! to - Guess The Number. You have choosen to be the Guess-er.\n")
        y= int(input("Enter the upper limit of the range to start this game: "))
        guess(y)

    elif (who==0):
        o=1
        print("\nWelcome Back! to - Guess The Number. You have choosen to be the Guess-ee.\n")
        while(o!=0):
            y= int(input("Enter the lower limit of the range to start this game: "))
            z= int(input("Enter the upper limit of the range to start this game: "))
            if (y>=z):
                print("Please enter valid numbers, lower limit needs be smaller than the upper limit.")
                o=1
                continue
            elif(z>=y):
                compguess(y, z)
                o=0
    m=int(input(f"\n \nDo you wish to go for another round? Enter 1 for Yes and 0 for No."))
    if m==0:
        break
print("\n \n \nFarewell~~ you're always welcome here so come again sometime :)\n \n \n")
