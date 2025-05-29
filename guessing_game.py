import random
attempts_list = []

def show_score():
    if  not attempts_list:
        print("There's no currently high score, start playing")
    else:
        print(f"The current high score is: {min(attempts_list)} attemptes")

attepts = 0
rand_number = random.randint(1,10)

print("Hello player! Welcom to the guessing game!")
player_name = input("what's your name? ")
wanna_play = input(
    f"Hi {player_name}, would you like to play guessing game?"
    "(Enter Yes/No): ").lower()
if wanna_play == "no":
    print("that's cool, Thanks")
    exit()
else:
    show_score()

while wanna_play == "yes":
    try:
        guess = int(input("pick anumber bettwen 1 and 10: "))
        if guess < 1 or guess > 10 :
            raise ValueError("please, guess anumber within the given range ")
        
        attepts +=1
        if guess == rand_number:
            print("Nice, you got it!")
            print (f"it took you {attepts} attempts")
            wanna_play = input("Would you like to play again? (Enter Yes/NO)  ").lower()

            attempts_list.append(attepts)

            if wanna_play == "no":
                print("That's cool, have agood day")
            else:
                attepts = 0
                rand_number = random.randint(1,10)
                show_score()
                continue  
        elif guess > rand_number:
            print("It's lower")
        else:
            print("It's higher")
    except ValueError as err:
        print(err)











