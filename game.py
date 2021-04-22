# Importing modules
import sys, time, colorama, math, random, art, termcolor, progress, progressbar, alive_progress

from colorama import Fore, Back, Style
from progress.bar import Bar
from alive_progress import alive_bar

# Typewriter effect
def fasttext(words):    # Just for use in the intro
	for c in words:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.05)
def medtext(words):     # For use in in-game dialogue 
	for c in words:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.1)


# Boat Parts Progress Bar
parts = 0.0
max_parts = 5
parts_dashes = 5
remaining_parts = max_parts - int(parts)

def bar_parts():
    dash_converter_parts = int(max_parts/parts_dashes)
    current_parts_dashes = int(parts/dash_converter_parts)
    remaining_parts_dashes = parts_dashes - current_parts_dashes
    parts_display = "-" * current_parts_dashes
    remaining_parts_display = " " * remaining_parts_dashes

    print(Fore.WHITE + Back.GREEN + "\u001b[1mBoat Parts : |" + parts_display + remaining_parts_display + "| \u001b[0m")

# Food Parts Progress Bar
food = 0.0
max_food = 5
food_dashes = 5

def bar_food():
    dash_converter_food = int(max_food/food_dashes)
    current_food_dashes = int(food/dash_converter_food)
    remaining_food_dashes = food_dashes - current_food_dashes
    food_display = "-" * current_food_dashes
    remaining_food_display = " " * remaining_food_dashes

    print(Fore.WHITE + Back.RED + "\u001b[1mFood : |" + food_display + remaining_food_display + "| \u001b[0m")

# Intro
name = input("Input your name: ")
print(Fore.CYAN + """
                                      \ _ /
                                    -= (_) =-
   .\/.                               /   \.
\.\//o\.\                      ,\/.     |                ,~
//o\.\|,\/.   ,.,.,  ,\/.   ,\ //o\.\               (     |\.
  |  |//o\  /###/#\ //o\   /o\.\ |            ~~~~~~(    /| \.
^^|^^|^~|^^^|' '|:|^^^|^^^^^|^^  |^^^""""""""  ~~~~~("~~~=(   /_|__\  ~~~
 .|'' . |  '''""'"''. |`===`|''   '"" "" "   (" ~~~~(  \_S_G_/ ~~ 
""")
fasttext(Fore.RED + f"\u001b[1mWelcome to 'Get Your Ship Together', {name}! \nYour boat 'Ships & Giggles' has been shipwrecked and its parts are scattered across this desert island.\nFind all the missing parts of your boat and collect enough food to make it back home. The progress bars below will fill each time you find a boat part or an item of food.\n\n" + "\u001b[0m")

bar_parts()
bar_food()
medtext(Fore.RED + "\u001b[1m\nCAN YOU ESCAPE THE ISLAND?\n"  + "\u001b[0m") 

fasttext(Fore.WHITE + "\nYou can start by exploring the Beach or the Jungle." + "\u001b[0m")

# Game
def start():
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.WHITE + f"\n\nWhere do you want to go, {name}?\n1. Beach\n2. Jungle\n" + "\u001b[0m")
        answer = input("> ")
        if answer == "1" or answer == "Beach" or answer == "beach" or answer == "BEACH":
            with alive_bar(100) as bar:   # default setting
                for i in range(100):
                    time.sleep(0.001)
                    bar()       
            beach()
        elif answer == "2" or answer == "Jungle" or answer == "jungle" or answer == "JUNGLE":
            with alive_bar(100) as bar:   # default setting
                for i in range(100):
                    time.sleep(0.001)
                    bar()           
            jungle()
        else:   # Need to fix this so it lets you input a proper answer
            fasttext("Invalid Input, Try Again")
            start()


# Settings
# Beach
def beach():
    
    medtext(Fore.YELLOW + "\u001b[1m\nThe Beach\n" + "\u001b[0m")
    print(Fore.YELLOW + """
              |
            \ _ /
          -=  0 =-
            /  \         _\/_
              |          //o\  _\/
      _____ _ __ __ ____ _ | __/o\\ _
    =-=-_-__=_-= _=_=-=_,-'|'-  |-,_
     =- _=-=- -_=-=_,-          | 
        =- =- -=.--
    """)
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.YELLOW + "\nTo your left, you see a set of footprints and to your right, you see a cluster of boulders. Which would you like to explore?" + "\u001b[0m")
        fasttext(Fore.YELLOW + "\n1. Footprints\n2. Boulders\n" + "\u001b[0m")
        answer = input("> ")
        if answer == "1" or answer == "footprint" or answer == "footprints" or answer == "Footprint" or answer == "Footprints" or answer == "FOOTPRINT" or answer == "FOOTPRINTS":
            footprints2()
        elif answer == "2" or answer == "boulder" or answer == "boulders" or answer == "Boulder" or answer == "Boulders" or answer == "BOULDER" or answer == "BOULDERS":
            boulder1()
        else:
            fasttext("Invalid Input, Try Again")
            beach()

def boulder1():
    medtext(Fore.YELLOW + "\u001b[1m\nThe Boulders" + "\u001b[0m") 
    print(Fore.YELLOW + """
             ,-.
            /   \   ,-.  
        ,-./     \ /   \ 
       /   \  ,-. /     \\
      /  .-.\/   '-.     \\
    _/__/___\\\__/___\_____\ 
    """)
    fasttext(Fore.YELLOW + "\nYou explored the boulders but found nothing.\n" + "\u001b[0m")
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:    
        fasttext(Fore.YELLOW + "\nAs you continue around the island, you see some sand dunes in the distance. You also notice a small oasis with an object protruding out of the water. Where do you want to go next?" + "\u001b[0m")
        fasttext(Fore.YELLOW + "\n1. Sand Dunes\n2. Oasis\n" + "\u001b[0m")
        answer = input("> ")
        if answer == "1" or answer == "Dunes" or answer == "Dune" or answer == "dunes" or answer == "dune" or answer == "DUNES" or answer == "DUNE" or answer == "Sand Dunes" or answer == "sand dunes" or answer == "SAND DUNES" or answer == "SANDDUNES" or answer == "SAND dunes" or answer =="sand DUNES":
            dunes1()
        elif answer == "2" or answer == "Oasis" or answer == "oasis" or answer == "OASIS":
            oasis1()
        else: 
            fasttext("Invalid Input, Try Again")
            boulder1()

def dunes1():
    medtext(Fore.YELLOW + "\u001b[1m\nThe Sand Dunes" + "\u001b[0m")
    print(Fore.YELLOW + """
                       _                              ./;;::::::;;;;;;;;\.
                      /;|                            ./;;;:::::::;;;;;;;;\___                              
                 ,-._/;;\                            .|;;;;;;;:::::::;;;;;;:::\..    
             _.-;;::::;;;;\                          ./;;;;;;;;;:::::::::::;;;;;|   
            /;;::;;;;;;;;;;\                      .../;;;;;:::::::::;;;:::::;;;;;\    
        _.-;::::::;;;;;;;;;;\                    ..:/;;;;::::::::::;;;;;:::::;;;;;;
    _.-;;;::::::::::;;;;;;;;;\                   ./;;;;;:::::::::;;;;;::::;;;;;;;;;;\                                  
    ;;;;;:::::::::::::;;;;;;;;|                  /;;;;:::::::::;;;;;;;;;::;;;;;;;;;;;\.
    ;;;;;:::::::::::::;;;;;;;;|                 /;;;;;:::::;;;;;;;;;;;:::::;;;;;;;;:::\.
    ;;;;;;;;:::::::;;;;;;;::::|     . o         |;;;;;;;;;::::::::::::::::::::::::::;;;|
    ;;;;;;;;::::;;;;;;;;;;;;;;|     \/0\_+      /;;;;;;;:::::::::::::::::::::::::;;;;::| 
    ;;;;;;;;::::::::::::::;;;;;\     /O\.      /;;;;;;;:::::::::::::::::::::::::::;;;;;; 
    :::::::;;;;;;;;;;;;;;::::;;;\   _| /_     /;;;;;;;:::::::::::::::::::::::::::::;;;;;
    """)
    fasttext(Fore.YELLOW + "\nYou explored the sand dunes but found nothing.\n" + "\u001b[0m")
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.YELLOW + "\nCarrying on down the beach, you discover a small oasis with an object protruding out of the water as well as some fallen palm trees in the distance. Which way do you want to go?" + "\u001b[0m")
        fasttext(Fore.WHITE + "\n1. Oasis\n2. Palm Trees\n" + "\u001b[0m")
        answer = input("> ")
        if answer == "1" or answer == "Oasis" or answer == "oasis" or answer == "OASIS":
            oasis1()
        elif answer == "2" or answer == "Palm Trees" or answer == "Palm Tree" or answer == "palm trees" or answer == "palm tree" or answer == "PALM TREES" or answer == "PALM TREE" or answer == "PALMTREE" or answer =="PALM tree" or answer == "palm TREE":
            palmtrees1()
        else: 
            fasttext("Invalid Input, Try Again")
            dunes1()

def oasis1():
    global parts_oasis
    global parts
    medtext(Fore.YELLOW + "\u001b[1m\nThe Oasis" + "\u001b[0m")
    print("""   
        \|/                            \|/  
        -0-           _                -0-
        /|\         >(')____,          /|\\
         |           (` =~~/            | 
       ~^~^`---'~^~^~^`---'~^~^~^`---'~^~^
    """) 
    if parts_oasis == 0:
        fasttext(Fore.YELLOW + f"\nYou explored The Oasis but found nothing.\n" + "\u001b[0m")
    else:
        parts_oasis -= 1
        parts +=1
        remaining_parts = max_parts - int(parts)    
        print(Fore.YELLOW + """
        ===========(8888)
        ===========(8888)
        """)
        fasttext(Fore.YELLOW + f"\nWell done, {name}! You found an oar protruding out of the oasis. There are now {remaining_parts} boat parts left.\n" + "\u001b[0m")
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.YELLOW + "\nYou carry on down the beach. Straight ahead you see some palm trees that have fallen over. You also notice some disturbed sand where an object may be buried. Which way will you go?" + "\u001b[0m")
        fasttext(Fore.WHITE + "\n1. Palm Trees\n2. Disturbed Sand\n" + "\u001b[0m")
        answer = input("> ")
        if answer == "1" or answer == "Palm Trees" or answer == "Palm Tree" or answer == "palm trees" or answer == "palm tree" or answer == "PALM TREES" or answer == "PALM TREE" or answer == "PALMTREE" or answer =="PALM tree" or answer == "palm TREE":
            palmtrees1()
        elif answer == "2" or answer == "Disturbed Sand" or answer == "DISTURBEDSAND" or answer == "disturbed sand" or answer == "DISTURBED SAND" or answer == "DISTURBED sand" or answer == "disturbed SAND":
            sand1()
        else: 
            fasttext("Invalid Input, Try Again")
            oasis1()

def palmtrees1():
    global food_palmtrees
    global food
    medtext(Fore.YELLOW + "\u001b[1m\nThe Fallen Palm Trees" + "\u001b[0m")
    print(Fore.YELLOW + """
         __ _.--..--._ _
      .-' _/   _/\_   \_'-.
     |__ /   _/\__/\_   \__|
       |___/\_\__/  \___|
              \__/
              \__/
               \__/
                \__/
             ____\__/___
       . - '             ' -.
      /                      |
    """)
    if food_palmtrees == 0:
        fasttext(Fore.YELLOW + f"\nYou explored The Fallen Palm Trees but found nothing.\n" + "\u001b[0m")
    else:
        food_palmtrees -= 1
        food +=1
        remaining_food = max_food - int(food)
        fasttext(Fore.YELLOW + f"\nYou found some coconuts by the palm tree. Great work, {name}! You only need {remaining_food} more items of food.\n" + "\u001b[0m")
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.YELLOW + "\nStraight ahead, you see some disturbed sand where an object might be buried. You also see the set of footprints which indicates you are near the starting point." + "\u001b[0m")
        fasttext(Fore.WHITE + "\n1. Disturbed Sand\n2. Footprints\n" + "\u001b[0m")
        answer = input("> ")
        if answer == "1" or answer == "Disturbed Sand" or answer == "DISTURBEDSAND" or answer == "disturbed sand" or answer == "DISTURBED SAND" or answer == "DISTURBED sand" or answer == "disturbed SAND":
            sand1()
        elif answer == "2" or answer == "Footprints" or answer == "footprints" or answer == "FOOTPRINTS" or answer == "foot prints" or answer == "Foot prints" or answer == "FOOT PRINTS":
            footprints1()
        else: 
            fasttext("Invalid Input, Try Again")
            palmtrees1()

def sand1():
    medtext(Fore.YELLOW + "\u001b[1m\nThe Disturbed Sand" + "\u001b[0m")
    global parts_sand
    global parts
    if parts_sand == 0:
        fasttext(Fore.YELLOW + f"\nYou explored the disturbed sand but found nothing.\n" + "\u001b[0m")
    else:
        parts_sand -= 1
        parts += 1
        remaining_parts = max_parts - int(parts)
        fasttext(Fore.YELLOW + f"\nWell done, {name}! You found the rope buried in the sand. There are now {remaining_parts} boat parts left.\n" + "\u001b[0m")
        print(Fore.YELLOW + """        
      -._.-""\"-.-""\"-..-""\"-.-""\"-.-""\"-.-""\"-.-""\"-.-"\""-._.-"-'
    =. _'.    '.    '.     '.    '.    '.    '.    '.    '. '_
   .-'.-. \     \     \      \     \     \     \     \     \'-_.
    .-'-__.'".___.'.___.'.____.'.___.'.___.'.___.'.___.'.___.'._-.
        """)
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.YELLOW + "\nJust ahead are a set of footprints indicating you are near the start point.\n" + "\u001b[0m")
        footprints1()

def footprints1():       
    medtext(Fore.YELLOW + "\u001b[1m\nThe Footprints" + "\u001b[0m")
    print(Fore.YELLOW + """
     oOOO() 
     /  _)
     |  (
     \__)  ()OOOo
            (_  |
             )  |
     oOOO()  (__/
     /  _)
     |  (
     \__)  ()OOOo
            (_  |
             )  |
             (__/
    """)
    global food_footprints
    global food
    if food_footprints == 0:
        fasttext(Fore.YELLOW + f"\nYou explored the footprints but found nothing.\n" + "\u001b[0m")
    else:
        food_footprints -= 1
        food +=1
        remaining_food = max_food - int(food)
        fasttext(Fore.YELLOW + f"\nThe footprints have led you to a dead fire where some fish has been cooked. Great work, {name}! You only need {remaining_food} more items of food.\n" + "\u001b[0m")
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.YELLOW + "\nYou have reached the starting point\n" + "\u001b[0m")
        start()      

def footprints2():  
    medtext(Fore.YELLOW + "\u001b[1m\nThe Footprints" + "\u001b[0m")
    print(Fore.YELLOW + """
     oOOO() 
     /  _)
     |  (
     \__)  ()OOOo
            (_  |
             )  |
     oOOO()  (__/
     /  _)
     |  (
     \__)  ()OOOo
            (_  |
             )  |
             |__/
    """) 
    global food_footprints
    global food
    if food_footprints == 0:
        fasttext(Fore.YELLOW + f"\nYou explored the footprints but found nothing.\n" + "\u001b[0m")
    else:
        food_footprints -= 1
        food +=1
        remaining_food = max_food - int(food)
        fasttext(Fore.YELLOW + f"\nThe footprints have led you to a dead fire where some fish has been cooked. Great work, {name}! You only need {remaining_food} more items of food.\n" + "\u001b[0m")
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.YELLOW + "\nYou carry on searching the beach. Straight ahead, you notice some disturbed sand where an object may be buried. You also see some palm trees that have fallen. Which would you like to explore?" + "\u001b[0m")
        fasttext(Fore.YELLOW + "\n1. Disturbed Sand\n2. Palm Trees\n" + "\u001b[0m")
        answer = input("> ")
        if answer == "2" or answer == "Palm trees" or answer == "palm trees" or answer == "PALM TREES" or answer == "Palm Trees":
            palmtrees2()
        elif answer == "1" or answer == "Disturbed sand" or answer == "disturbed sand" or answer == "DISTURBED SAND" or answer == "Disturbed Sand":
            sand2()
        else:
            fasttext("Invalid Input, Try Again")
            footprints2()

def sand2():
    medtext(Fore.YELLOW + "\u001b[1m\nThe Disturbed Sand" + "\u001b[0m")
    global parts_sand
    global parts
    if parts_sand == 0:
        fasttext(Fore.YELLOW + f"\nYou explored the disturbed sand but found nothing.\n" + "\u001b[0m")
    else:
        parts_sand -= 1
        parts += 1
        remaining_parts = max_parts - int(parts)
        fasttext(Fore.YELLOW + f"\nWell done, {name}! You found the rope buried in the sand. There are now {remaining_parts} boat parts left.\n" + "\u001b[0m")
        print(Fore.YELLOW + """        
      -._.-""\"-.-""\"-..-""\"-.-""\"-.-""\"-.-""\"-.-""\"-.-"\""-._.-"-'
    =. _'.    '.    '.     '.    '.    '.    '.    '.    '. '_
    .-'.-. \     \     \      \     \     \     \     \     \'-_.
        .-'-__.'".___.'.___.'.____.'.___.'.___.'.___.'.___.'.___.'._-.
        """)
    bar_parts()
    bar_food()    
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m") 
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.YELLOW + "\nStraight ahead, you see the palm trees as well as an oasis with something protruding out of the water. Which would you like to explore?" + "\u001b[0m")
        fasttext(Fore.YELLOW + "\n1. Palm Trees" + "\n2. Oasis\n" + "\u001b[0m")
        answer = input("> ")  
        if answer == "1" or answer == "Palm trees" or answer == "Palm Trees" or answer == "PALM TREES" or answer == "palm trees":
            palmtrees2()
        elif answer == "2" or answer == "Oasis" or answer == "2. Oasis" or answer == "OASIS":
            oasis2()
        else:
            fasttext("Invalid Input, Try Again")
            sand2()

def palmtrees2():
    global food_palmtrees
    global food
    medtext(Fore.YELLOW + "\u001b[1m\nThe Fallen Palm Trees" + "\u001b[0m")  
    print(Fore.YELLOW + """
        __ _.--..--._ _
     .-' _/   _/\_   \_'-.
    |__ /   _/\__/\_   \__|
       |___/\_\__/  \___|
              \__/
              \__/
               \__/
                \__/
             ____\__/___
       . - '             ' -.
      /                      |
    """)  
    if food_palmtrees == 0:
        fasttext(Fore.YELLOW + f"\nYou explored The Fallen Palm Trees but found nothing.\n" + "\u001b[0m")
    else:
        food_palmtrees -= 1
        food +=1
        remaining_food = max_food - int(food)
        fasttext(Fore.YELLOW + f"\nYou found some coconuts by the palm tree. Great work, {name}! You only need {remaining_food} more items of food.\n" + "\u001b[0m")
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.YELLOW + "\nAs you continue around the island, you notice a small oasis with an object protruding out of the water. You also see a set of dunes. Which would you like to explore?" + "\u001b[0m")
        fasttext(Fore.YELLOW + "\n1. Oasis" + "\n2. Sand Dunes\n" +"\u001b[0m")
        answer = input("> ")
        if answer == "1" or answer == "Oasis" or answer == "1. Oasis" or answer == "OASIS" or answer == "oasis":
            oasis2()
        elif answer == "2" or answer == "Dunes" or answer == "Dune" or answer == "dunes" or answer == "dune" or answer == "DUNES" or answer == "DUNE" or answer == "Sand Dunes" or answer == "sand dunes" or answer == "SAND DUNES" or answer == "SANDDUNES" or answer == "SAND dunes" or answer =="sand DUNES":
            dunes2()
        else:
            fasttext("Invalid Input, Try Again")
            palmtrees2()

def oasis2():
    global parts_oasis
    global parts
    medtext(Fore.YELLOW + "\u001b[1m\nThe Oasis" + "\u001b[0m")
    print(Fore.YELLOW + """   
        \|/                            \|/  
        -0-           _                -0-
        /|\         >(')____,          /|\\
         |           (` =~~/            | 
       ~^~^`---'~^~^~^`---'~^~^~^`---'~^~^
    """) 
    if parts_oasis == 0:
        fasttext(Fore.YELLOW + f"\nYou explored The Oasis but found nothing.\n" + "\u001b[0m")
    else:
        parts_oasis -= 1
        parts +=1
        remaining_parts = max_parts - int(parts)    
        print(Fore.YELLOW + """
        ===========(8888)
        ===========(8888)
        """)
        fasttext(Fore.YELLOW + f"\nWell done, {name}! You have found an oar protruding from the oasis. There are now {remaining_parts} boat parts left.\n" + "\u001b[0m")
    bar_parts()
    bar_food()    
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.YELLOW + "\nAhead, you see the sand dunes. You also see the boulders which indicate you are nearing the start point. Which do you choose?" + "\u001b[0m")
        fasttext(Fore.YELLOW + "\n1. Sand Dunes" + "\n2. Boulders\n" + "\u001b[0m")
        answer = input ("< ")
        if answer == "1" or answer == "Dunes" or answer == "Dune" or answer == "dunes" or answer == "dune" or answer == "DUNES" or answer == "DUNE" or answer == "Sand Dunes" or answer == "sand dunes" or answer == "SAND DUNES" or answer == "SANDDUNES" or answer == "SAND dunes" or answer =="sand DUNES":
            dunes2()
        elif answer == "2" or answer == "boulder" or answer == "boulders" or answer == "Boulder" or answer == "Boulders" or answer == "BOULDER" or answer == "BOULDERS":
            boulder2()
        else:
            fasttext("Invalid Input, Try Again")
            oasis2()

def dunes2():
    medtext(Fore.YELLOW + "\u001b[1m\nThe Sand Dunes" + "\u001b[0m")
    print(Fore.YELLOW + """
                                                         .:..:...:....:..
                    _                                  ./;;::::::;;;;;;;;\.
                   /;|                                ./;;;:::::::;;;;;;;;\___                              
              ,-._/;;\                               .|;;;;;;;:::::::;;;;;;:::\..    
         _.-;;::::;;;;\                              ./;;;;;;;;;:::::::::::;;;;;|   
        /;;::;;;;;;;;;;\                          .../;;;;;:::::::::;;;:::::;;;;;\    
    _.-;::::::;;;;;;;;;;\                       ..:/;;;;::::::::::;;;;;:::::;;;;;;
    _.-;;;::::::::::;;;;;;;;;\                   ./;;;;;:::::::::;;;;;::::;;;;;;;;;;\                                  
    ;;;;;:::::::::::::;;;;;;;;|                  /;;;;:::::::::;;;;;;;;;::;;;;;;;;;;;\.
    ;;;;;:::::::::::::;;;;;;;;|                 /;;;;;:::::;;;;;;;;;;;:::::;;;;;;;;:::\.
    ;;;;;;;;:::::::;;;;;;;::::|     . o         |;;;;;;;;;::::::::::::::::::::::::::;;;|
    ;;;;;;;;::::;;;;;;;;;;;;;;|     \/0\_+      /;;;;;;;:::::::::::::::::::::::::;;;;::| 
    ;;;;;;;;::::::::::::::;;;;;\     /O\.      /;;;;;;;:::::::::::::::::::::::::::;;;;;; 
    :::::::;;;;;;;;;;;;;;::::;;;\   _| /_     /;;;;;;;:::::::::::::::::::::::::::::;;;;;
    """)
    fasttext(Fore.YELLOW + "\nYou explored the sand dunes but found nothing.\n" + "\u001b[0m")
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.YELLOW + "\nJust ahead, you see the boulders, indicating that you are near the starting point.\n" + "\u001b[0m")
        boulder2()

def boulder2():
    medtext(Fore.YELLOW + "\u001b[1m\nThe Boulders" + "\u001b[0m") 
    print(Fore.YELLOW + """
             ,-.
            /   \   ,-.  
        ,-./     \ /   \ 
       /   \  ,-. /     \\
      /  .-.\/   '-.     \\
    _/__/___\\\__/___\_____\ 
    """)
    fasttext(Fore.YELLOW + "\nYou explored the boulders but found nothing.\n" + "\u001b[0m")
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.YELLOW + "\nYou've reached the starting point" + "\u001b[0m")
        start()


# Jungle
def jungle():
    medtext(Fore.LIGHTGREEN_EX + "\u001b[1m\nThe Jungle\n" + "\u001b[0m")
    print(Fore.LIGHTGREEN_EX + """
                ,@@@@@@@,
        ,,,.   ,@@@@@@/@@,  .oo8888o.
     ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
    ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
    %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
    %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
    `&%\ ` /%&'   |.|        \ '|8'
        |o|       | |         | |
        |.|       | |         | |
     \\/ ._\.^, __/  ,\_      /.  \_
    """)
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.LIGHTGREEN_EX + "\nTo your left, you see an overgrowth of vegetation and to your right, you see a dark cave. Which would you like to explore?" + "\u001b[0m")
        fasttext(Fore.LIGHTGREEN_EX + "\n1. Overgrowth\n2. Cave\n" + "\u001b[0m")
        answer = input("> ")
        if answer == "1" or answer == "Overgrowth" or answer == "overgrowth" or answer == "OVERGROWTH":
            overgrowth2()
        elif answer == "2" or answer == "Cave" or answer == "cave" or answer == "CAVE":
            cave1()
        else:   # Need to fix this so it lets you input a proper answer
            fasttext("Invalid Input, Try Again")
            jungle()

def cave1():
    medtext(Fore.LIGHTGREEN_EX + "\u001b[1m\nThe Cave" + "\u001b[0m")
    print(Fore.LIGHTGREEN_EX +"""
             _____________                  
            /             \___                 
              _ \          _  \                  
             /   \       _/m\  \                 
           _/    /      /MMmm\  \_                 
          /      \     |MMMMmm|   \__                   
         |        \   /MMMMMMm|      \             
         /        \  |MMMMMMmm\      \___                
        /           \|MMMMMMMMmm|____.'  /\_         
        |           /'___|  |______...,,'   \      
    """)
    fasttext(Fore.LIGHTGREEN_EX + "\nYou explored the cave but found nothing.\n"+ "\u001b[0m")    
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.LIGHTGREEN_EX + "\nAs you continue through the jungle, you see ruins of an abandoned civilisation as well as some flat plains. Which do you choose to explore?" + "\u001b[0m")
        fasttext(Fore.LIGHTGREEN_EX + "\n1. Ruins\n2. Flat Plains\n" + "\u001b[0m")
        answer = input("> ")
        if answer == "1" or answer == "Ruins" or answer == "ruins" or answer == "RUINS":
            ruins1()
        elif answer == "2" or answer == "plains" or answer == "flat plains" or answer == "Plains" or answer == "Flat Plains" or answer == "Flat plains" or answer == "PLAINS" or answer == "FLAT PLAINS":
            plains1()
        else:   # Need to fix this so it lets you input a proper answer
            fasttext("Invalid Input, Try Again")
            cave1()    

def ruins1():
    global parts_ruins
    global parts
    medtext(Fore.LIGHTGREEN_EX + "\u001b[1m\nThe Ruins" + "\u001b[0m")
    print(Fore.LIGHTGREEN_EX + """
      / \               /| 
     /   \             / |  
    |_____|           |___\.
    |   |      _   _  |  /
    | O |_   _| |_| |_| O\.
    |-  | \_/      _  | -| 
    |   |   - _^_     |  \.
    |  _|    //|\\   - |   |
    |   |   ///|\\\    |  -|
    |-  |_  |||||||   ||||| 
    |   | \ |||||||   |||||  
    \ __|__||||||||___|___|   
    """)
    if parts_ruins == 0:
        fasttext(Fore.LIGHTGREEN_EX + f"\nYou explored The Ruins but found nothing.\n" + "\u001b[0m")
    else:
        parts_ruins -= 1
        parts +=1
        remaining_parts = max_parts - int(parts)    
        fasttext(Fore.LIGHTGREEN_EX + f"\nWell done, {name}! You found the hull within the ruins. There are now {remaining_parts} boat parts left.\n" + "\u001b[0m")
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.LIGHTGREEN_EX + "\nAfter exploring the ruins, you see the flat plains. You also notice a ditch in the distance. Which do you choose to explore?" + "\u001b[0m")
        fasttext(Fore.LIGHTGREEN_EX + "\n1. Flat Plains\n2. Ditch\n" + "\u001b[0m")
        answer = input("> ")
        if answer == "1" or answer == "plains" or answer == "flat plains" or answer == "Plains" or answer == "Flat Plains" or answer == "Flat plains" or answer == "PLAINS" or answer == "FLAT PLAINS":
            plains1()
        elif answer == "2" or answer == "Ditch" or answer == "ditch" or answer == "DITCH":
            ditch1()
        else:   # Need to fix this so it lets you input a proper answer
            fasttext("Invalid Input, Try Again")
            ruins1()    

def plains1():
    medtext(Fore.LIGHTGREEN_EX + "\u001b[1m\nThe Flat Plains" + "\u001b[0m")
    print(Fore.LIGHTGREEN_EX + """
                      _
                  _(_)_                          wWWWw   _
      @@@@       (_)@(_)   vVVVv     _     @@@@  (___) _(_)_
     @@()@@ wWWWw  (_)\    (___)   _(_)_  @@()@@   Y  (_)@(_)
      @@@@  (___)    `|/     Y    (_)@(_)  @@@@   \|/   (_)
       /      Y      \|     \|/    /(_)    \|      |/     |
    \ |     \ |/      | /  \ | /   \|/      |/    \|     \|/
    \\\|//   \\\|//   \\\\|//  \\\\|///  \\|///  \\\\|//  \\\|//  \\\|// 
    """)
    fasttext(Fore.LIGHTGREEN_EX + "\nYou explored the plains but found nothing.\n" + "\u001b[0m")    
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.LIGHTGREEN_EX + "\nYou notice a ditch in the distance just ahead of some trees where something appears to be caught in the branches. Which do you choose to explore?" + "\u001b[0m")
        fasttext(Fore.LIGHTGREEN_EX + "\n1. Ditch\n2. Trees\n" + "\u001b[0m")
        answer = input("> ")
        if answer == "1" or answer == "Ditch" or answer == "ditch" or answer == "DITCH":
            ditch1()
        elif answer == "2" or answer == "tree" or answer == "trees" or answer == "Tree" or answer == "Trees" or answer == "TREE" or answer == "TREES":
            trees1()
        else:   # Need to fix this so it lets you input a proper answer
            fasttext("Invalid Input, Try Again")
            plains1()    

def ditch1():
    medtext(Fore.LIGHTGREEN_EX + "\u001b[1m\nThe Ditch" + "\u001b[0m")
    print(Fore.LIGHTGREEN_EX + """
                         8a .
                               `.  _
    ___________  s,    _____     /_/   ______________
               .Jktbc._       _ ./
              xft#kTJ:   _.  (_)/)  -._
             cf8#6C. ,  (   ( ,-'      )
           ` `"P:'.     '-._\_\___.---'
    """)
    fasttext(Fore.LIGHTGREEN_EX + "\nYou explored the ditch but found nothing.\n" + "\u001b[0m")  
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.LIGHTGREEN_EX + "\nIn the trees ahead, you notice something caught in the branches. You also notice a waterfall not far away. Which do you choose?" + "\u001b[0m")
        fasttext(Fore.LIGHTGREEN_EX + "\n1. Trees\n2. Waterfall\n" + "\u001b[0m")
        answer = input("> ")
        if answer == "1" or answer == "tree" or answer == "trees" or answer == "Tree" or answer == "Trees" or answer == "TREE" or answer == "TREES":
            trees1()
        elif answer == "2" or answer == "Waterfall" or answer == "waterfall" or answer == "WATERFALL":
            waterfall1()
        else:   # Need to fix this so it lets you input a proper answer
            fasttext("Invalid Input, Try Again")
            ditch1()  

def trees1():
    global food_trees
    global food
    global parts_trees
    global parts
    medtext(Fore.LIGHTGREEN_EX + "\u001b[1m\nThe Trees" + "\u001b[0m")
    print(Fore.LIGHTGREEN_EX + """
         oxoxoo  oxoxooxoo oxoxooooo xoox                           
       ooxoxo oo   oxoxoooxx ooxoxoxoox oxoxo                                
      oooo xxoxoo ooo oooxoooo xxoxoo ooo ooox                                  
      oxo o oxoxo  xoxxoxooxo oooxoxoox xoxxo                     
       oxo xooxooooooooxoxoxoxo xooxoooo oox                             
         ooo\oo\  /o/o\  \/ ooo\oo\  /o/o                                    
            \  \/ /   \    /   \  \/ /
             |   /     |  |     |   /              
             |  |      |  |     |  |                    
             |  |      | 0|     |  |                                 
             | o|      |  |     | D|                       
             |  |      |  |     |  |                     
      ______/____\____/    \___/____\____                            
    """)
    if food_trees == 0:
        fasttext(Fore.LIGHTGREEN_EX + f"\nYou explored The Trees but found nothing.\n" + "\u001b[0m")
    else:
        food_trees -= 1
        food +=1
        remaining_food = max_food - int(food)
        parts_trees -= 1
        parts += 1
        remaining_parts = max_parts - int(parts)
        fasttext(Fore.LIGHTGREEN_EX + f"\nWell done, {name}! You found the sail caught in the branches.  There are now {remaining_parts} boat parts left. You also found some bananas. You only need {remaining_food} more items of food.\n" + "\u001b[0m")
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.LIGHTGREEN_EX + "\nYou see a waterfall nearby as well as a bunker. Which do you choose to explore?" + "\u001b[0m")
        fasttext(Fore.LIGHTGREEN_EX + "\n1. Waterfall\n2. Bunker\n" + "\u001b[0m")
        answer = input("> ")
        if answer == "1" or answer == "Waterfall" or answer == "waterfall" or answer == "WATERFALL":
            waterfall1()
        elif answer == "2" or answer == "Bunker" or answer == "bunker" or answer == "BUNKER":
            bunker1()
        else:   # Need to fix this so it lets you input a proper answer
            fasttext("Invalid Input, Try Again")
            trees1()

def waterfall1():
    global food_waterfall
    global food
    medtext(Fore.LIGHTGREEN_EX + "\u001b[1m\nThe Waterfall" + "\u001b[0m")
    print(Fore.LIGHTGREEN_EX + """
       _________....-~___~-.______
    ~~~                            ~~~~-----...___________..--------
                                               |   |     |
                                               | |   |  ||
                                               |  |  |   |
                                               |'. .' .`.|
    ___________________________________________|0oOO0oO0o|____________
     -          -         -       -      -    / '  '. ` ` \    -    -
          --                  --       --   /    '  . `   ` \    --
    ---            ---          ---       /  '                \ ---
         ----               ----        /       ' ' .    ` `    \  ----
    -----         -----         ----- /   '   '        `      `   \.
         .-~~-.          ------     /          '    . `     `    `  \.
    """)
    if food_waterfall == 0:
        fasttext(Fore.LIGHTGREEN_EX + f"\nYou explored The Waterfall but found nothing.\n" + "\u001b[0m")
    else:
        food_waterfall -= 1
        food +=1
        remaining_food = max_food - int(food)
        fasttext(Fore.LIGHTGREEN_EX + f"\nIn the stream leading to the waterfall, you found some wild salmon. Good work, {name}! You only need {remaining_food} more items of food.\n" + "\u001b[0m")
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.LIGHTGREEN_EX + "\nYou see a bunker nearby as well as an overgrowth indicating you are nearing the starting point. Which do you choose?" + "\u001b[0m")
        fasttext(Fore.LIGHTGREEN_EX + "\n1. Bunker\n2. Overgrowth\n" + "\u001b[0m")
        answer = input("> ")
        if answer == "1" or answer == "Bunker" or answer == "bunker" or answer == "BUNKER":
            bunker1()
        elif answer == "2" or answer == "Overgrowth" or answer == "overgrowth" or answer == "OVERGROWTH":
            overgrowth1()
        else:   
            fasttext("Invalid Input, Try Again")
            waterfall1()

def bunker1():
    global parts_bunker
    global parts
    medtext(Fore.LIGHTGREEN_EX + "\u001b[1m\nThe Bunker" + "\u001b[0m")
    print(Fore.LIGHTGREEN_EX + """
              ___________
     ________/=====    ,.|`##
    /=====      _,yTi^Tr#####
    |__,.,,:,&%7@o=;#$fH######
    """)
    if parts_bunker == 0:
        fasttext(Fore.LIGHTGREEN_EX + f"\nYou explored The Bunker but found nothing.\n" + "\u001b[0m")
    else:
        parts_bunker -= 1
        parts +=1
        remaining_parts = max_parts - int(parts)    
        fasttext(Fore.LIGHTGREEN_EX + f"\nWell done, {name}! You found the mast that had fallen in the bunker. There are now {remaining_parts} boat parts left.\n" + "\u001b[0m")
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.LIGHTGREEN_EX + "\nYou see the overgrowth indicating you are nearing the start point.\n" + "\u001b[0m")
        overgrowth1()

def overgrowth1():
    global food_overgrowth
    global food
    medtext(Fore.LIGHTGREEN_EX + "\u001b[1m\nThe Overgrowth" + "\u001b[0m")
    print(Fore.LIGHTGREEN_EX + """
     __    __        __          __    __        __          __    __
         //    \\)    __(//   __    (//    \\)    __(//   __    (//    \\)  
       /"      / __  \\)"    \\)_  /"      / __  \\)"    \\)_  /"      / __
     '|-..__..-''\_''-.\__..-'' '|-..__..-''\_''-.\__..-''  '|-..__..-''|
     (\\  \_    _(\\      _/     (\\  \_    _(\\      _/     (\\  \_    //)
      ""  (\\  //)""     //)      ""  (\\  //)""     //)      ""  (\\   ""
           ""  ""        ""            ""  ""        ""            ""
    """) 
    if food_overgrowth == 0:
        fasttext(Fore.LIGHTGREEN_EX + f"\nYou explored The Overgrowth but found nothing.\n" + "\u001b[0m")
    else:
        food_overgrowth -= 1
        food +=1
        remaining_food = max_food - int(food)
        fasttext(Fore.LIGHTGREEN_EX + f"\nWithin the overgrowth, you found some edible honeysuckle and rose flowers. Good work, {name}! You only need {remaining_food} more items of food.\n" + "\u001b[0m")
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.LIGHTGREEN_EX + "\nYou have reached the starting point" + "\u001b[0m")
        start()

def overgrowth2():
    global food_overgrowth
    global food
    medtext(Fore.LIGHTGREEN_EX + "\u001b[1m\nThe Overgrowth" + "\u001b[0m")
    print(Fore.LIGHTGREEN_EX + """
         __    __        __          __    __        __          __    __
        //    \\)    __(//   __    (//    \\)    __(//   __    (//    \\)  
       /"      / __  \\)"    \\)_  /"      / __  \\)"    \\)_  /"      / __
     '|-..__..-''\_''-.\__..-'' '|-..__..-''\_''-.\__..-''  '|-..__..-''|
     (\\  \_    _(\\      _/     (\\  \_    _(\\      _/     (\\  \_    //)
      ""  (\\  //)""     //)      ""  (\\  //)""     //)      ""  (\\   ""
           ""  ""        ""            ""  ""        ""            ""
    """) 
    if food_overgrowth == 0:
        fasttext(Fore.LIGHTGREEN_EX + f"\nYou explored The Overgrowth but found nothing.\n" + "\u001b[0m")
    else:
        food_overgrowth -= 1
        food +=1
        remaining_food = max_food - int(food)
        fasttext(Fore.LIGHTGREEN_EX + f"\nWithin the overgrowth, you found some edible honeysuckle and rose flowers. Good work, {name}! You only need {remaining_food} more items of food.\n" + "\u001b[0m")
    bar_parts()
    bar_food()  
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.LIGHTGREEN_EX + "\nYou see a bunker nearby as well as a waterfall. Which way do you want to go?" + "\u001b[0m")
        fasttext(Fore.LIGHTGREEN_EX + "\n1. Bunker\n2. Waterfall\n" + "\u001b[0m")
        answer = input("> ")
        if answer == "2" or answer == "Waterfall" or answer == "waterfall" or answer == "WATERFALL":
            waterfall2()
        elif answer == "1" or answer == "Bunker" or answer == "bunker" or answer == "BUNKER":
            bunker2()
        else:   # Need to fix this so it lets you input a proper answer
            fasttext("Invalid Input, Try Again")
            overgrowth2()

def bunker2():
    global parts_bunker
    global parts
    medtext(Fore.LIGHTGREEN_EX + "\u001b[1m\nThe Bunker" + "\u001b[0m")
    print(Fore.LIGHTGREEN_EX + """
                  ___________
         ________/=====    ,.|`##
        /=====      _,yTi^Tr#####
      _|__,.,,:,&%7@o=;#$fH######
    """)
    if parts_bunker == 0:
        fasttext(Fore.LIGHTGREEN_EX + f"\nYou explored The Bunker but found nothing.\n" + "\u001b[0m")
    else:
        parts_bunker -= 1
        parts +=1
        remaining_parts = max_parts - int(parts)    
        fasttext(Fore.LIGHTGREEN_EX + f"\nWell done, {name}! You found the mast that had fallen in the bunker. There are now {remaining_parts} boat parts left.\n" + "\u001b[0m")
    bar_parts()
    bar_food()    
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.LIGHTGREEN_EX + "\nNot far away, you notice a waterfall. However, you also notice that in the trees ahead, something is caught in the branches. Which do you choose?" + "\u001b[0m")
        fasttext(Fore.LIGHTGREEN_EX + "\n1. Waterfall\n2. Trees\n" + "\u001b[0m")
        answer = input("> ")
        if answer == "2" or answer == "tree" or answer == "trees" or answer == "Tree" or answer == "Trees" or answer == "TREE" or answer == "TREES":
            trees2()
        elif answer == "1" or answer == "Waterfall" or answer == "waterfall" or answer == "WATERFALL":
            waterfall2()
        else:   # Need to fix this so it lets you input a proper answer
            fasttext("Invalid Input, Try Again")
            bunker2()  

def waterfall2():
    global food_waterfall
    global food
    medtext(Fore.LIGHTGREEN_EX + "\u001b[1m\nThe Waterfall" + "\u001b[0m")
    print(Fore.LIGHTGREEN_EX + """
       _________....-~___~-.______
    ~~~                            ~~~~-----...___________..--------
                                               |   |     |
                                               | |   |  ||
                                               |  |  |   |
                                               |'. .' .`.|
    ___________________________________________|0oOO0oO0o|____________
     -          -         -       -      -    / '  '. ` ` \    -    -
          --                  --       --   /    '  . `   ` \    --
    --            ---          ---       /  '                \ ---
         ----               ----        /       ' ' .    ` `    \  ----
    -----         -----         ----- /   '   '        `      `   \.
        .-~~-.          ------     /          '    . `     `    `  \.
    """)
    if food_waterfall == 0:
        fasttext(Fore.LIGHTGREEN_EX + f"\nYou explored The Waterfall but found nothing.\n" + "\u001b[0m")
    else:
        food_waterfall -= 1
        food +=1
        remaining_food = max_food - int(food)
        fasttext(Fore.LIGHTGREEN_EX + f"\nIn the stream leading to the waterfall, you found some wild salmon. Good work, {name}! You only need {remaining_food} more items of food.\n" + "\u001b[0m")
    bar_parts()
    bar_food() 
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.LIGHTGREEN_EX + "\nIn the trees ahead, something appears to be caught in the branches. You also notice a ditch in the distance. Which do you choose to explore?" + "\u001b[0m")
        fasttext(Fore.LIGHTGREEN_EX + "\n1. Trees\n2. Ditch\n" + "\u001b[0m")
        answer = input("> ")
        if answer == "2" or answer == "Ditch" or answer == "ditch" or answer == "DITCH":
            ditch2()
        elif answer == "1" or answer == "tree" or answer == "trees" or answer == "Tree" or answer == "Trees" or answer == "TREE" or answer == "TREES":
            trees2()
        else:   # Need to fix this so it lets you input a proper answer
            fasttext("Invalid Input, Try Again")
            waterfall2()     

def trees2():
    global food_trees
    global food
    global parts_trees
    global parts
    medtext(Fore.LIGHTGREEN_EX + "\u001b[1m\nThe Trees" + "\u001b[0m")
    print(Fore.LIGHTGREEN_EX + """
         oxoxoo  oxoxooxoo oxoxooooo xoox                           
       ooxoxo oo   oxoxoooxx ooxoxoxoox oxoxo                                
      oooo xxoxoo ooo oooxoooo xxoxoo ooo ooox                                  
      oxo o oxoxo  xoxxoxooxo oooxoxoox xoxxo                     
       oxo xooxooooooooxoxoxoxo xooxoooo oox                             
         ooo\oo\  /o/o\  \/ ooo\oo\  /o/o                                    
            \  \/ /   \    /   \  \/ /
             |   /     |  |     |   /              
             |  |      |  |     |  |                    
             |  |      | 0|     |  |                                 
             | o|      |  |     | D|                       
             |  |      |  |     |  |                     
      ______/____\____/   \____/____\____                            
    """)
    if food_trees == 0:
        fasttext(Fore.LIGHTGREEN_EX + f"\nYou explored The Trees but found nothing.\n" + "\u001b[0m")
    else:
        food_trees -= 1
        food +=1
        remaining_food = max_food - int(food)
        parts_trees -= 1
        parts += 1
        remaining_parts = max_parts - int(parts)
        fasttext(Fore.LIGHTGREEN_EX + f"\nWell done, {name}! You found the sail caught in the branches.  There are now {remaining_parts} boat parts left. You also found some bananas. You only need {remaining_food} more items of food.\n" + "\u001b[0m")
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.LIGHTGREEN_EX + "\nAfter exploring the Trees, you notice a ditch in the distance. You also see some flat plains just ahead. Which do you choose to explore?" + "\u001b[0m")
        fasttext(Fore.LIGHTGREEN_EX + "\n1. Ditch\n2. Flat Plains\n" + "\u001b[0m")
        answer = input("> ")
        if answer == "2" or answer == "plains" or answer == "flat plains" or answer == "Plains" or answer == "Flat Plains" or answer == "Flat plains" or answer == "PLAINS" or answer == "FLAT PLAINS":
            plains2()
        elif answer == "1" or answer == "Ditch" or answer == "ditch" or answer == "DITCH":
            ditch2()
        else:   # Need to fix this so it lets you input a proper answer
            fasttext("Invalid Input, Try Again")
            trees2()    

def ditch2():
    medtext(Fore.LIGHTGREEN_EX + "\u001b[1m\nThe Ditch" + "\u001b[0m")
    print(Fore.LIGHTGREEN_EX + """
                         8a .
                               `.  _
    ___________  s,    _____     /_/   ______________
               .Jktbc._       _ ./
              xft#kTJ:   _.  (_)/)  -._
             cf8#6C. ,  (   ( ,-'      )
           ` `"P:'.     '-._\_\___.---'
    """)
    fasttext(Fore.LIGHTGREEN_EX + "\nYou explored the ditch but found nothing.\n" + "\u001b[0m")  
    bar_parts()
    bar_food()    
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.LIGHTGREEN_EX + "\nAs you continue through the jungle, you see some flat plains as well as ruins of an abandoned civilisation. Which would you like to explore?" + "\u001b[0m")
        fasttext(Fore.LIGHTGREEN_EX + "\n1. Flat Plains\n2. Ruins\n" + "\u001b[0m")
        answer = input("> ")
        if answer == "2" or answer == "Ruins" or answer == "ruins" or answer == "RUINS":
            ruins2()
        elif answer == "1" or answer == "plains" or answer == "flat plains" or answer == "Plains" or answer == "Flat Plains" or answer == "Flat plains" or answer == "PLAINS" or answer == "FLAT PLAINS":
            plains2()
        else:   # Need to fix this so it lets you input a proper answer
            fasttext("Invalid Input, Try Again")
            ditch2()    

def plains2():
    medtext(Fore.LIGHTGREEN_EX + "\u001b[1m\nThe Flat Plains" + "\u001b[0m")
    print(Fore.LIGHTGREEN_EX + """
                      _
                  _(_)_                          wWWWw   _
      @@@@       (_)@(_)   vVVVv     _     @@@@  (___) _(_)_
     @@()@@ wWWWw  (_)\    (___)   _(_)_  @@()@@   Y  (_)@(_)
      @@@@  (___)    `|/     Y    (_)@(_)  @@@@   \|/   (_)
       /      Y      \|     \|/    /(_)    \|      |/     |
    \ |     \ |/      | /  \ | /   \|/      |/    \|     \|/
    \\\|//   \\\|//   \\\\|//  \\\\|///  \\|///  \\\\|//  \\\|//  \\\|// 
    """)
    fasttext(Fore.LIGHTGREEN_EX + "\nYou explored the plains but found nothing.\n" + "\u001b[0m")    
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.LIGHTGREEN_EX + "\nJust ahead, you see the ruins of an abandoned civilisation as well as a dark cave which indicates you are nearing the start point. Where do you want to go?" + "\u001b[0m")    
        fasttext(Fore.LIGHTGREEN_EX + "\n1. Ruins\n2. Cave\n" + "\u001b[0m")
        answer = input("> ")
        if answer == "1" or answer == "Ruins" or answer == "ruins" or answer == "RUINS":
            ruins2()
        elif answer == "2" or answer == "Cave" or answer == "cave" or answer == "CAVE":
            cave2()
        else:   # Need to fix this so it lets you input a proper answer
            fasttext("Invalid Input, Try Again")
            plains2()  
    
def ruins2():
    global parts_ruins
    global parts
    medtext(Fore.LIGHTGREEN_EX + "\u001b[1m\nThe Ruins" + "\u001b[0m")
    print(Fore.LIGHTGREEN_EX + """
      / \               /| 
     /   \             / |  
    |_____|           |___\.
    |   |      _   _  |  /
    | O |_   _| |_| |_| O\.
    |-  | \_/      _  | -| 
    |   |   - _^_     |  \.
    |  _|    //|\\   - |   |
    |   |   ///|\\\    |  -|
    |-  |_  |||||||   ||||| 
    |   | \ |||||||   |||||  
    \ __|__||||||||___|___|   
    """)
    if parts_ruins == 0:
        fasttext(Fore.LIGHTGREEN_EX + f"\nYou explored The Ruins but found nothing.\n" + "\u001b[0m")
    else:
        parts_ruins -= 1
        parts +=1
        remaining_parts = max_parts - int(parts)    
        fasttext(Fore.LIGHTGREEN_EX + f"\nWell done, {name}! You found the hull within the ruins. There are now {remaining_parts} boat parts left.\n" + "\u001b[0m")
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.LIGHTGREEN_EX + "\nAhead, you see the cave indicating you are nearing the start point.\n" + "\u001b[0m")
        cave2()

def cave2():
    medtext(Fore.LIGHTGREEN_EX + "\u001b[1m\nThe Cave" + "\u001b[0m")
    print(Fore.LIGHTGREEN_EX + """
             _____________                  
            /             \___                 
              _ \          _  \                  
             /   \       _/m\  \                 
           _/    /      /MMmm\  \_                 
          /      \     |MMMMmm|   \__                   
         |        \   /MMMMMMm|      \             
         /        \  |MMMMMMmm\      \___                
        /           \|MMMMMMMMmm|____.'  /\_         
        |           /'___|  |______...,,'   \      
    """)
    fasttext(Fore.LIGHTGREEN_EX + "\nYou explored the cave but found nothing.\n" + "\u001b[0m")
    bar_parts()
    bar_food()
    if parts == 5.0 and food == 5.0:
        fasttext(Fore.RED + f"\u001b[1m\nCongratulations, {name}! You collected all the parts to reassemble your boat and enough food to make it back home. Bon voyage!\n" + "\u001b[0m")
        print("""
               ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----....._____
           \Ships & Giggles 2.0/
        ~^~^~^~^~^`~^~^`^~^~^`^~^~^
        ~^~^~`~~^~^`~^~^~`~~^~^~
        """)
    else:
        fasttext(Fore.LIGHTGREEN_EX + "\nYou have reached the starting point\n" + "\u001b[0m")
        start()

# Food
food_footprints = 1
food_palmtrees = 1
food_overgrowth = 1
food_trees = 1
food_waterfall = 1

# Boat Parts
parts_oasis = 1
parts_sand = 1
parts_ruins = 1
parts_trees = 1
parts_bunker = 1 

start()
