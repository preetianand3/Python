from random import randint

while True:
    num = randint(0, 100)
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<**GUESSING_GAME_CHALLENGE**>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n \n")

    print("					WELCOME TO GUESS ME!")
    print("		I'm thinking of a number between 1 and 100")
    print("		If your guess is more than 10 away from my number, I'll tell you you're COLD")
    print("		If your guess is within 10 of my number, I'll tell you you're WARM")
    print("		If your guess is farther than your most recent guess, I'll say you're getting COLDER")
    print("		If your guess is closer than your most recent guess, I'll say you're getting WARMER")
    print("					LET'S PLAY!\n \n")

    print("I'm thinking of a number between 1 and 100.\n")

    i = 0
    guesses = [0]


    #while True:
        guess = int(input("What is your guess? > "))
        guesses.append(guess)
        k += 1
        if guess < 1 or guess > 100:
            print("OUT OF BOUNDS")
            continue
        elif guess == num:
            print("YAY!")
            score = len(guesses)
            print("You Won In {} Guesses".format(score-1))

            with open('highscore.txt', mode='r+') as myNewFile:
                content = myNewFile.read()
                highscore = int(content) if content else 0
                if highscore > score:
                    print("You broke the previous HIGHSCORE")
                    myNewFile.seek(0)
                    myNewFile.write(str(score))
                    myNewFile.truncate()
            break
        elif i == 0:
            if abs(num-guess) <= 10:
                print("WARM!")
            else:
                print("COLD!")
        else:
            if abs(num-guess)<abs(num-guesses[-2]):
                print("WARMER!")
            else:
                print("COLDER!")
        i += 1
