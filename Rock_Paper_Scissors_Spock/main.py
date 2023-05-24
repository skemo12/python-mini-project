""" Rock scissors paper simulator """
from random import SystemRandom


# WINNING PATTERNS
# Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard,
# Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard,
# Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock,
# Rock crushes Scissors

WIN = [
    ("scissors", "paper"),
    ("paper", "rock"),
    ("rock", "lizard"),
    ("lizard", "Spock"),
    ("Spock", "scissors"),
    ("scissors", "lizard"),
    ("lizard", "paper"),
    ("paper", "Spock"),
    ("Spock", "rock"),
    ("rock", "scissors"),
]

# INSTRUCTIONS
print(
    "There are 6 rounds.\nYou are playing against Computron.\n\
    You will win if you have a higher point.\n\
    Enter scissors, paper, rock, lizard or Spock.\n\
    LIVE LONG AND PROSPER🖖\n"
)

# CHOICES FOR THE COMPUTRON TO CHOOSE FROM
CHOICES = ["scissors", "paper", "rock", "lizard", "Spock"]

# TO COUNT THE NUMBER OF ROUNDS
COUNT = 0
# TO COUNT THE PLAYER'S POINTS
PLAYERPOINTS = 0
# TO COUNT THE COMPUTRONS' POINTS
COMPUTERPOINTS = 0

CRYPTO_GENERATOR = SystemRandom()

# WHILE LOOP TO SET THE NUMBER OF ROUNDS
while COUNT != 6:
    # INPUT FOR PLAYER'S CHOICE
    PLAYER = input("What is your move? ")
    # COMPUTRON RANDOMLY SELECT CHOICE FROM CHOICES LIST
    COMPUTER = CRYPTO_GENERATOR.choice(CHOICES)
    # UNCOMMENT THE LINE BELOW IF YOU WISH TO SEE COMPUTRONS' CHOICE
    # print(computer)

    # DIFFERENT CHOICES
    if PLAYER != COMPUTER:
        # CHECK FOR PATTERNS
        PLAYERWINS = (PLAYER, COMPUTER)
        COMPUTERWINS = (COMPUTER, PLAYER)
        if PLAYERWINS in WIN:
            if PLAYERWINS == WIN[0]:
                # print("✂ cuts 📃 \nYou Won!")
                print("Scissors cuts paper \nYou Won!")
            elif PLAYERWINS == WIN[1]:
                print("Paper covers rock \nYou Won!")
            elif PLAYERWINS == WIN[2]:
                print("Rock crushes lizard \nYou Won!")
            elif PLAYERWINS == WIN[3]:
                print("Lizard poisons Spock \nYou Won!")
            elif PLAYERWINS == WIN[4]:
                print("Spock smashes scissors \nYou Won!")
            elif PLAYERWINS == WIN[5]:
                print("Scissors decapitates lizard \nYou Won!")
            elif PLAYERWINS == WIN[6]:
                print("Lizard eats paper \nYou Won!")
            elif PLAYERWINS == WIN[7]:
                print("Paper disproves Spock \nYou Won!")
            elif PLAYERWINS == WIN[8]:
                print("Spock vapourizes rock \nYou Won!")
            elif PLAYERWINS == WIN[9]:
                print("Rock crushes scissors \nYou Won!")
            PLAYERPOINTS += 1
        elif COMPUTERWINS in WIN:
            if COMPUTERWINS == WIN[0]:
                print("Scissors cuts paper \nComputron Wins!")
            elif COMPUTERWINS == WIN[1]:
                print("Paper covers rock \nComputron Wins!")
            elif COMPUTERWINS == WIN[2]:
                print("Rock crushes lizard \nComputron Wins!")
            elif COMPUTERWINS == WIN[3]:
                print("Lizard poisons Spock \nComputron Wins!")
            elif COMPUTERWINS == WIN[4]:
                print("Spock smashes scissors \nComputron Wins!")
            elif COMPUTERWINS == WIN[5]:
                print("Scissors decapitates lizard \nComputron Wins!")
            elif COMPUTERWINS == WIN[6]:
                print("Lizard eats paper \nComputron Wins!")
            elif COMPUTERWINS == WIN[7]:
                print("Paper disproves Spock \nComputron Wins!")
            elif COMPUTERWINS == WIN[8]:
                print("Spock vapourizes rock \nComputron Wins!")
            elif COMPUTERWINS == WIN[9]:
                print("Rock crushes scissors \nComputron Wins!")
            COMPUTERPOINTS += 1
        # PLAYER DID NOT INPUT scissors, paper, rock, lizard or Spock
        else:
            print("Invalid response \nComputron Wins!")
            COMPUTERPOINTS += 1

    # DRAW, SAME CHOICES
    elif PLAYER == COMPUTER:
        print("Draw, Player and Computron gets 1 point")
        PLAYERPOINTS += 1
        COMPUTERPOINTS += 1

    # EMPTY LINE FOR A NEATER/CLEARER VIEW
    print("")

    # INCREMENT TO CONTROL THE NUMBER OR ROUNDS
    COUNT += 1

# COMPARISON TO DETERMINE WHO IS THE CHAMPION
if PLAYERPOINTS > COMPUTERPOINTS:
    print("You are the champion! 🏆")
elif PLAYERPOINTS == COMPUTERPOINTS:
    print("You are both champions!! 🏆🏆")
else:
    print("Computron is the champion, Try Again! 💻")
