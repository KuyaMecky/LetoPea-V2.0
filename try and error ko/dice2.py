import random
import turtle

col = ("red", "blue", "white", "orange", "purple",
       "green", "grey", "brown", "violet", "yellow", "LimeGreen",
       "OrangeRed", "SlateBlue", "YellowGreen",
       "LightSeaGreen", "gold", "DodgerBlue", "DarkMagenta",
       "NavyBlue", "DarkRed", "DarkGreen", "DeepPink")


def dicemove(turd=None):
    turd.hideturtle()
    turd.pendown()
    turd.begin_fill()
    turd.left(90)
    turd.forward(100)
    turd.right(90)
    turd.forward(100)
    turd.right(90)
    turd.forward(100)
    turd.right(90)
    turd.forward(100)
    turd.right(180)
    turd.end_fill()
    turd.penup()


def dicedots(dotty=None, numg=None):
    if numg == 1:
        dotty.hideturtle()
        dotty.forward(100 / 2)
        dotty.left(90)
        dotty.forward(100 / 2)
        dotty.dot(15)
        dotty.left(180)
        dotty.forward(100 / 2)
        dotty.right(90)
        dotty.forward(100 / 2)
        dotty.right(180)

    elif numg == 2:
        dotty.hideturtle()
        dotty.forward(100 / 3)
        dotty.left(90)
        dotty.forward(100 / 3)
        dotty.dot(15)
        dotty.right(90)
        dotty.forward(100 / 3)
        dotty.left(90)
        dotty.forward(100 / 3)
        dotty.dot(15)
        dotty.forward(100 / 3)
        dotty.left(90)
        dotty.forward(100 / 1)
        dotty.left(90)
        dotty.forward(100 / 1)
        dotty.left(90)
        dotty.forward(100 / 3)

    elif numg == 3:
        dotty.hideturtle()
        dotty.forward(100 / 4)
        dotty.left(90)
        dotty.forward(100 / 4)
        dotty.forward(100 / 2)
        dotty.dot(15)
        dotty.right(90)
        dotty.forward(100 / 2)
        dotty.right(90)
        dotty.forward(100 / 2)
        dotty.dot(15)
        dotty.right(90)
        dotty.forward(100 / 4)
        dotty.right(90)
        dotty.forward(100 / 4)
        dotty.dot(15)
        dotty.forward(100 / 2)
        dotty.left(90)
        dotty.forward(100 / 2)
        dotty.left(90)
        dotty.forward(100)
        dotty.left(90)

    elif numg == 4:
        dotty.hideturtle()
        dotty.forward(100 / 4)
        dotty.left(90)
        dotty.forward(100 / 4)
        dotty.dot(15)
        dotty.forward(100 / 2)
        dotty.dot(15)
        dotty.right(90)
        dotty.forward(100 / 2)
        dotty.dot(15)
        dotty.right(90)
        dotty.forward(100 / 2)
        dotty.dot(15)
        dotty.forward(100 / 4)
        dotty.right(90)
        dotty.forward(100 / 1)
        dotty.right(180)
        dotty.forward(100 / 3)

    elif numg == 5:
        dotty.hideturtle()
        dotty.forward(100 / 4)
        dotty.left(90)
        dotty.forward(100 / 4)
        dotty.dot(15)
        dotty.forward(100 / 2)
        dotty.dot(15)
        dotty.right(90)
        dotty.forward(100 / 2)
        dotty.dot(15)
        dotty.right(90)
        dotty.forward(100 / 2)
        dotty.dot(15)
        dotty.right(90)
        dotty.forward(100 / 4)
        dotty.right(90)
        dotty.forward(100 / 4)
        dotty.dot(15)
        dotty.forward(100 / 2)
        dotty.left(90)
        dotty.forward(100 / 2)
        dotty.left(90)
        dotty.forward(100)
        dotty.left(90)
    elif numg == 6:
        dotty.hideturtle()
        dotty.forward(100 / 4)
        dotty.left(90)
        dotty.forward(100 / 4)
        dotty.dot(15)
        dotty.forward(100 / 4)
        dotty.dot(15)
        dotty.forward(100 / 4)
        dotty.dot(15)
        dotty.right(90)
        dotty.forward(100 / 2)
        dotty.dot(15)
        dotty.right(90)
        dotty.forward(100 / 4)
        dotty.dot(15)
        dotty.forward(100 / 4)
        dotty.dot(15)
        dotty.forward(100 / 4)
        dotty.right(90)
        dotty.forward(100 / 1)
        dotty.right(180)
        dotty.forward(100 / 3)
    else:
        pass


def byefelicia():
    print("\n" * 100)
    print("""
    -------------------------------------------------
    |                @}>---}--------                |
    | This python version of Petals around the Rose |
    |           has been brought to you by:         |
    |                  KUYAMECKY                    |
    |                                               |
    |                                               |
    |            with a little help from            |
    |            python's turtle module!            |
    |                                               |
    |              Hope you enjoyed it!             |
    -------------------------------------------------
    \n""")
    turd = turtle.getturtle()
    turd.reset()
    s = turtle.getscreen()
    s.bgcolor("black")
    turtle.color('red')
    style = ('Courier', 21, 'bold')
    turtle.write('@}>---}----- Timothy Swallow -----(---<{@', font=style, align='center')
    turtle.hideturtle()
    turtle.exitonclick()


def main():
    ped = 0
    print("\n" * 100)
    print("                   @}>---}-------- Petals around the Rose --------(---<{@")
    print("\n")
    while True:
        ask = input("          Would you care to read a little history about Petals around the Rose? y/n ")
        rules = ask.lower()
        if rules == "y":
            print("\n" * 100)
            print("""
             @}>---}--------                                                               --------(---<{@
                                              Tang na mocha productions
             @}>---}--------                                                                --------(---<{@
                    \n""")
            break
        elif rules == "n":
            break
        else:
            pass
    while True:
        ask = input("                            Would you like to see the rules for Petals around the Rose? y/n ")
        rules = ask.lower()
        if rules == "y":
            print("\n" * 100)
            print("""
                Petals around the Rose is played by rolling 5 dice and matching your guess with the roll value provided.
                             While the provided value may seem random, I assure you it is not.
            \n
                                    @}>---}--------      ¯\_(o_o)_/¯       --------(---<{@
            \n
                                     There are only two rules to Petals around the Rose:
            \n
                               Rule 1: The players guess can only be zero or an even number.
                               Rule 2: The name of the game is extremely relevant.""")
            break
        elif rules == "n":
            break
        else:
            pass
        ##while True:
    while True:
        print("\n")
        start = input("                  @}}>----- Would you like to play a round of Petals around the Rose? -----<{{@ y/n ")
        game = start.lower()
        if game == "y":
            s = turtle.getscreen()
            turd = turtle.getturtle()
            dotty = turtle.getturtle()
            turd.reset()
            s.bgcolor("black")
            turd.speed(5)
            turd.width(5)
            turd.pencolor(random.choice(col))
            dotty.pencolor(random.choice(col))
            turd.fillcolor(random.choice(col))
            dot = dotty.pencolor()
            fill = turd.fillcolor()
            while True:
                if dot == fill:
                    pen = turd.pencolor(random.choice(col))
                else:
                    break
            turd.penup()
            turd.hideturtle()
            turd.forward(-325)

            print("\n" * 100)
            for x in range(1, 6):
                numg = random.randint(1, 6)
                if numg == 3:
                    ped += 2
                elif numg == 5:
                    ped += 4
                else:
                    pass
                dicemove(turd)
                turd.begin_fill()
                turd.end_fill()
                dicedots(dotty, numg)
                turd.forward(140)
            while True:
                try:
                    guess = int(input("--------(---<{@ Enter your guess: "))
                    plrguess = str(guess)
                except ValueError:
                    print("Please choose 0 or an even number")
                else:
                    if (guess % 2) != 0:
                        print("Please choose 0 or an even number")
                    else:
                        break
            if guess == ped:
                print("\n" * 100)
                while True:
                    print(" (¯`·._.·(¯`·._.· Good job! You guessed correctly! Your guess was", plrguess + ".",
                          "The value for this round was", str(ped) + ",", "·._.·´¯)·._.·´¯)")
                    ped = 0
                    print("\n")
                    turd = turtle.getturtle()
                    turd.reset()
                    s = turtle.getscreen()
                    s.bgcolor("red")
                    turtle.color('yellow')
                    style = ('Courier', 35, 'bold')
                    turtle.write('@}~}~~~ Congrats! ~~~{~{@', font=style, align='center')
                    turtle.hideturtle()
                    break
                print("                             @}~}~~~  But the question is, can you do it again?  ~~~{~{@")
                print("\n")
                while True:
                    ver = input(
                        "             Maybe you should consider verifing your understanding and giving it another go? y/n ")
                    if ver == "y":
                        turd.reset()
                        break
                    elif ver == "n":
                        print("\n" * 100)
                        print("Another time then!")
                        print("\n")
                        byefelicia()
                        input("Press enter to exit...")
                        turtle.exitonclick()
                        end
                    else:
                        pass

            else:
                print("\n" * 100)
                peds = str()
                print("               (⋗_⋖) Unfortunately, you are incorrect. Your guess was", plrguess, "and this round's value was",
                      str(ped) + ".", "(⋗_⋖)")
                print("\n")
                ped = 0
                while True:
                    turd = turtle.getturtle()
                    turd.reset()
                    s = turtle.getscreen()
                    s.bgcolor("black")
                    turtle.color('grey')
                    style = ('Courier', 40, 'bold')
                    turtle.write('¯\_(o_o)_/¯', font=style, align='center')
                    turtle.hideturtle()
                    break
                    print("\n")
                while True:
                    last = input("        ¯\_(o_o)_/¯ Confused yet? Better luck next time. Maybe you should give it another go? ¯\_(o_o)_/¯ y/n ")
                    if last == "y":
                        break
                    elif last == "n":
                        print("\n * 100")
                        print("Another time then!")
                        print("\n")
                        byefelicia()
                        input("Press enter to exit...")
                        end
                    else:
                        turd.reset()
                        pass

        elif game == "n":
            print("\n * 100")
            print("Another time then!")
            print("\n")
            byefelicia()
            input("Press enter to exit...")
            end
        else:
            #        turd.reset()
            pass


if __name__ == '__main__':
    main()