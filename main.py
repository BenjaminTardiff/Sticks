# STICKS
def tryParseInt(variable, exclution=False):
    while type(variable) != int and variable != exclution:
        try:
            int(variable)
            return int(variable)
        except ValueError:
            variable = input("Invlaid input. Please enter an integer: ")
    return variable


def hit(player, playerfingers, target, targetfingers):
    global again
    global game
    again = ""
    game = True
    print(playerfingers)
    attack = tryParseInt(input("Which hand would you like to hit with, 1 or 2? "))
    while attack != 1 and attack != 2:
        attack = tryParseInt(input("Invalid hand. Please enter either a 1 or a 2. "))
    attack = playerfingers[attack - 1]
    while attack == 0:
        attack = tryParseInt(input("Invalid hand. Please enter a non-zero hand. "))
        while attack != 1 and attack != 2:
            attack = tryParseInt(input("Invalid hand. Please enter a non-zero hand. "))
        attack = playerfingers[attack - 1]
    print(str(targetfingers))
    damage = tryParseInt(input("Which hand would you like to hit, 1 or 2? "))
    while damage != 1 and damage != 2:
        damage = tryParseInt(input("Invalid hand. Please enter wither a 1 or a 2. "))
    targetfingers[damage - 1] += attack
    while damage == 0:
        damage = tryParseInt(input("Invalid hand. Please enter a non-zero hand. "))
        while damage != 1 and damage != 2:
            damage = tryParseInt(input("Invalid hand. Please enter a non-zero hand. "))
        targetfingers[damage - 1] += attack
    print()
    for i in range(2):
        if targetfingers[i] >= 5:
            if wrapAround:
                targetfingers[i] %= 5
                if targetfingers == 0:
                    print(target, " lost hand ", i + 1)
                    if targetfingers[1] == 0 and targetfingers[0] == 0:
                        game = False
                        print(target, " loses! ", player, " wins!")
                        again = input("Want to play again? y or n ")
                        while again != "y" and again != "n":
                            again = input("Invalid answer. Please enter y or n. ")
                else:
                    print(target, "'s hand wraped to", targetfingers[i] % 5)
            else:
                targetfingers[i] = 0
                print(target, " lost hand ", i + 1)
                if targetfingers[1] == 0 and targetfingers[0] == 0:
                    game = False
                    print(target, " loses! ", player, " wins!")
                    again = input("Want to play again? y or n ")
                    while again != "y" and again != "n":
                        again = input("Invalid answer. Please enter y or n. ")


def checkSplit(player):
    global splitable
    splitable = False
    if (player[0] == 0 and player[1] % 2 == 0 and player[1] != 0) or (
            player[0] % 2 == 0 and player[1] == 0 and player[0] != 0):
        splitable = True


def split(player):
    split = False
    print(player)
    splitFrom = tryParseInt(input("Which hand would you like to split, 1 or 2? "))
    while splitFrom != 1 and splitFrom != 2:
        splitFrom = tryParseInt(input("Invalid entry. Please enter either 1 or 2 "))
    while not split:
        if splitFrom == 1 and player[0] != 0:
            player[1] = player[0] / 2
            player[0] /= 2
            split = True
        elif splitFrom == 2 and player[1] != 0:
            player[0] = player[1] / 2
            player[1] /= 2
            split = True
        else:
            splitFrom = tryParseInt(input("invalid entry. please enter a non-zero hand."))
            while splitFrom != 1 and splitFrom != 2:
                splitFrom = tryParseInt(input("Invlaid entry. Please enter a non-zero hand."))
    print()

def main():
    p1 = [1, 1]
    p2 = [1, 1]
    game = True
    turn = ""
    again = ""
    splitable = False
    global wrapAround
    wrapAround = input("Wrap around(y/n): ")
    while wrapAround != "y" and wrapAround != "n":
        wrapAround = input("y or n only: ")
    if wrapAround == "y":
        wrapAround = True
    else:
        wraparound = False
    while game:
        print("Player 1")
        checkSplit(p1)
        if splitable:
            turn = input("Would you like to split or hit? ")
            while turn != "split" and turn != "hit":
                turn = input("Invalid entry. Please enter either split or hit. ")
        else:
            turn = "hit"
        if turn == "hit":
            hit("Player 1", p1, "Player 2", p2)
        else:
            split(p1)
        if game:
            print("Player 2")
            splitable = False
            checkSplit(p2)
            if splitable:
                turn = input("Would you like to split or hit?")
                while turn != "split" and turn != "hit":
                    turn = input("Invalid entry. Please enter either split or hit")
                if turn == "hit":
                    hit("Player 2", p2, "Player 1", p1)
                else:
                    split(p2)
            else:
                hit("Player 2", p2, "Player 1", p1)
        if again == "y":
            game = True
            p1 = [1, 1]
            p2 = [1, 1]
            print("\n\n\n")


main()