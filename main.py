import random


# Check pick-up condition
def check_taken(x, take_max, take_min, in_pile):
    if x > take_max:
        print("Sorry, you cannot take more than 2 sticks in once.")
        return False
    elif x > in_pile:
        print("Sorry, you don't have enough stick.")
        return False
    elif x < take_min:
        print("Sorry, you cannot take less than 1 stick.")
        return False
    else:
        return True


# Check if the game over
def is_over(x):
    if x == 0:
        return True


# Check turn >> turn = 1 is bot pick the stick
def whose_turn(x):
    if x == 1:
        return True


# Check bot player condition
def bot_consider(take_max, take_min, in_pile):
    # take min pick-up if there are the minimum pick-up available (no choice : pick then lose)
    if in_pile == take_min:
        return take_min
    # if stick left in a pile is not in the set of losing number
    elif (in_pile+take_max) % (take_max+1) != 0:
        for i in range(take_min, take_max+1):
            if ((in_pile-i)+take_max) % (take_max+1) == 0:
                return i
    else:
        return random.randint(take_min, take_max)


# Check the winner ( turn=0: player, turn=1:computer)
def winner(x, bot, who):
    if x == 0:
        print("\nI,", bot, ", takes the last stick.")
        print(who, "wins ( I,", bot, ", am sad T_T )")
    else:
        print()
        print(who, ", takes the last stick.")
        print("I,", bot, ", wins !!!")


print("\n---------------------------------\n   WELCOME TO STICK IN A PILE  \n---------------------------------")
stick_amount = int(input("How many sticks (N) in the pile? : "))
print("There are", stick_amount, "stick(s) in the pile.")
player = "smart computer"
player1 = input("What is your name? : ")
print()

min_taken = 1
max_taken = 2
pick = 0
turn = 0

if stick_amount == 0:
    print("Sorry, you have no stick in the pile.")

while not is_over(stick_amount):
    if whose_turn(turn):
        pick = bot_consider(max_taken, min_taken, stick_amount)
        print("I," + player + ", takes : ", pick)
        turn = 0
    else:
        pick = int(input(player1 + ", How many stick(s) you will take? (from 1 to " + str(max_taken) + ") : "))
        while not check_taken(pick, max_taken, min_taken, stick_amount):
            pick = int(input(player1 + ", How many stick(s) you will take? (from 1 to " + str(max_taken) + ") : "))
        turn = 1
    stick_amount = stick_amount - pick
    print("There are", stick_amount, "stick(s) left in the pile.\n")

print("Over! There is no stick left in the pile.")
winner(turn, player, player1)

print("\n------------------\n   GOOD BYE  " + player1 + "\n------------------")