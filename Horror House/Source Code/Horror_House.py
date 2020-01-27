import sys
import os
import pygame
from gtts import gTTS
import time


pygame.mixer.init()
pygame.mixer.music.load("Backwave.wav")
door_unlock= pygame.mixer.Sound("door_unlock.wav")
door_open= pygame.mixer.Sound("door_open.wav")
door_shut= pygame.mixer.Sound("door_shut.wav")
door_knob= pygame.mixer.Sound("door_knob.wav")                                #Sound imported
scream= pygame.mixer.Sound("scream.wav")
women_crying= pygame.mixer.Sound("crying.wav")

def main():
    os.system("CLS")
    print("   _________________________________________________________ ")
    print("  |   (    (  (  ) )  )  )        /      /       \          |")
    print("  |    (   (        ) HOUSE OF HORRORS  /        / ---------|")
    print("  |      (  ( () ) )            /      ^        /          /|")
    print("  |                            /\     / \      /          / |")
    print("  |          \/\       ^      /  \   /   \    /          /  |")
    print("  |             \/\   /  \   / +  \ /  +  \  /          /   |")
    print("  |       ^           /  \  /_____ /_______\/__________/    |")   #main page
    print("  |      /  \         /  \  |       |        | _______ |    |")
    print("  |      /  \          ||   |  ___  |   __   | _______ |   /|")
    print("  |      /  \               | |___| |  |  |  | _______ |  / |")
    print("  |       ||               /|___    |  |_*|  | _______ | /  |")
    print("  |                       /_|_+_|___|__---___|_________|/   |")
    print("  |   ^        ^      ^      ^       ^ ---^   /       /     |")
    print("  |   |        |      |      |       |    |  /       /      |")
    print("  |---|--------|------|------|-------|----| BY Kefron Grant |")                                                   
    print("  |---|--------|------|------|-------|----|/       /        |")
    print("  |___|________|______|______|_______|____|_______/_________|")
    print("                        -----------") 
    print("                       |   START   |  1")
    print("                        -----------")
    print("                        -----------")
    print("                       |   EXIT    |  2")
    print("                        -----------")
    print("                        -----------")
    print("                       |   RULES   |  3")
    print("                        -----------")
    print("                        -----------")
    print("                       |   MUTE    |  4")
    print("                        -----------")
    button_Choice=input("Please Choose your options with the assigned number: ")
    if(button_Choice == "1"):
        Start()
    elif(button_Choice == "2"):
        music_Mute()
        Exit()
    elif(button_Choice == "3"):
        Rules_Pg_1()
    elif(button_Choice == "4"):
         music_Play_pause()
    else:
        main()
def music_Play_pause():
    button_Music=input("play music Y or N : ")
    if(button_Music == "y"):
        Music()
        main()
    elif(button_Music == "n"):
        music_Mute()
        main()
    else:
        print("Case Sensitive")
        main()
class Player:
    def __init__(self,name,HP):
        self.name = name
        self.HP = HP
name = Player("Alex",3)
def Start():
    os.system("CLS")


def Rules_Pg_1():
    os.system('CLS')
    print(" __________________________________________________________")
    print("|                                                          |")
    print("| RULES & How to Play & Game Info:                         |")
    print("| --------------------------------                         |")
    print("|  Making Choices:                                         |")
    print("|                  EX.                                     |")
    print("|   -----------                         -----------        |")
    print("|  | Main Menu | 1                     |   EXIT    |  2    |") #if main page option three
    print("|   -----------                         -----------        |")
    print("|                ^                                         |")
    print("|                |                                         |")
    print("|                                                          |")
    print("|       You will be asked to input an assigned             |")
    print("|       number, this assigned number is used for           |")
    print("|       the main window, and will take you                 |")
    print("|       to the main window. Any other inputs               |")
    print("|       will take you back to the initial screen.          |")
    print("|                                                     pg.1 |")
    print(" __________________________________________________________")
    print("      -----------       -----------       -----------")
    print("     | Main Menu |  1  |   More     |  2 |   EXIT     |  3")
    print("      -----------       -----------       -----------")
    button_Choice_rules_one=input("Please Choose your options with the assigned number: ")
    if(button_Choice_rules_one == "1"):
        main()
    elif(button_Choice_rules_one == "2"):
        Rules_Pg_2()
    elif(button_Choice_rules_one == "3"):
        music_Mute()
        Exit()
    else:
        Rules_Pg_1()
def Rules_Pg_2():
    print(" __________________________________________________________")
    print("|                                                          |")
    print("| RULES & How to Play & Game Info:                         |")
    print("| --------------------------------                         |")
    print("|  Name <-- Player's name                                  |")
    print("|  HP <-- Players Health Points                            |")
    print("|                                                          |")
    print("|                                                          |")   #Rules Page 2
    print("|                                                          |")
    print("|    In the game you will have to keep an eye              |")
    print("|    on player health points, Somthing just might          |")
    print("|    be out to get you.                                    |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                     pg.2 |")
    print(" __________________________________________________________")
    print("      -----------       -----------       -----------")
    print("     | Main Menu |  4  |   More     |  5 |   EXIT     |  6")
    print("      -----------       -----------       -----------")
    button_Choice_rules_two=input("Please Choose your options with the assigned number: ")
    if(button_Choice_rules_two == "4"):
        main()
    elif(button_Choice_rules_two == "5"):
        Rules_Pg_3()
    elif(button_Choice_rules_two == "6"):
        music_Mute()
        Exit()
    else:
        Rules_Pg_2()
def Rules_Pg_3():
    print(" __________________________________________________________")
    print("|                                                          |")
    print("| RULES & How to Play & Game Info:                         |")
    print("| --------------------------------                         |")
    print("|  Back Story:                                             |")
    print("|                                                          |")
    print("|   A group of friends and the new girl decide             |")
    print("|   to investigate a home where a family mysteriously went |")
    print("|   missing. You play Alex the new girl in town who is     |")
    print("|   just tagging along to fit in,she will soon regret that |")
    print("|   decision or will she, Thats up to you.                 |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                               P.S HAVE FUN =D            |")
    print("|                                                          |")
    print("|                                                     pg.3 |")
    print(" __________________________________________________________")
    print("      -----------      -----------        -----------")
    print("     | Main Menu |  7 |   Last    |  8   |   EXIT     |  9")
    print("      -----------      -----------        -----------")
    button_Choice_start_three=input("Please Choose your options with the assigned number: ")
    if(button_Choice_start_three == "7"):
        main()
    elif(button_Choice_start_three == "8"):
        Rules_Pg_4()
    elif(button_Choice_start_three == "9"):
        music_Mute()
        Exit()
    else:
        Rules_Pg_3()
def Rules_Pg_4():
    print(" __________________________________________________________")
    print("|                                                          |")
    print("| RULES & How to Play & Game Info:                         |")
    print("| --------------------------------                         |")
    print("|                                                          |")
    print("|           Game version 1.0                               |")
    print("|                                                          |")
    print("|      Extra Notes:                                        |")
    print("|       * Combat / survival and Health not yet implemented.|")
    print("|                                                          |")
    print("|       * Story will be much longer with many more choices.|")
    print("|                                                          |")
    print("|       * Updated version will have more with More with    |")
    print("|         basement and upstairs.                           |")
    print("|                                                          |")
    print("|       * Iteams will also be added to heal or to progress |")
    print("|         the story.                                       |")
    print("|                                                     pg.4 |")
    print(" __________________________________________________________")
    print("      -----------                         -----------")
    print("     | Main Menu | 10                    |   EXIT     |  11")
    print("      -----------                         -----------")
    button_Choice_rules_two=input("Please Choose your options with the assigned number: ")
    if(button_Choice_rules_two == "10"):
        main()
    elif(button_Choice_rules_two == "11"):
        music_Mute()
        Exit()
    else:
        Rules_Pg_4()
                    


def Start():
    print(" __________________________________________________________")
    print("|                                                          |")
    print("| Name:", name.name ,"                                              |")
    print("| Health:", name.HP ,"                                               |")
    print("|                                                          |")
    print("|    Its the first day of school and so chaotic            |")
    print("|    You over hear what the comotion is about              |")
    print("|    apparently a kid named Joe and his family             |") #if main page option one
    print("|    went missing a few days ago.                          |")
    print("|                                                          |")
    print("|    You begin making your way to class where you          |")
    print("|    unwillingly introduce your self, Hello my name is     |")
    print("|    Alex. You make it through your classes with no        |")
    print("|    issues on your way to the bus you are stopped by      |")
    print("|    Becky you recognize her from class. She introduces    |")
    print("|    her self and then begins to ask where your from       |")
    print("|    you say Washington, as the conversation goes on she   |")
    print("|    asks if you'd like to hang out with here and her      |")
    print("|    friends, she says that they where going to check out  |")
    print("|    the house where Joe and his family went missing.      |")
    print("|                                                          |")
    print(" __________________________________________________________")
    print("      -----------       -----------     ---------------------")
    print("     |  Agree     | 1  | Ask why   | 2 |  Say No and go Home | 3")
    print("      -----------       -----------     ---------------------")
    print("      -----------                         -----------")
    print("     | Main Menu | 4                     |   EXIT     | 5")
    print("      -----------                         -----------")
    button_Choice_start=input("Please Choose your options with the assigned number: ")
    if(button_Choice_start == "1"):
        ASS1()
    elif( button_Choice_start == "2"):
        BSS2()
    elif( button_Choice_start == "3"):
        CSS3()
    elif(button_Choice_start == "4"):
        main()
    elif(button_Choice_start == "5"):
        Exit()
    else:
        Start()
        


#ASS1 = A Start Sub 1
#BSS1 = B Start Sub 2
#CSS1 = C Start Sub 3

def ASS1():
    print(" __________________________________________________________")
    print("|                                                          |")
    print("| Name:", name.name ,"                                              |")      # because Name and health are inserted lines had to 
    print("| Health:", name.HP ,"                                               |")     # pushed back.
    print("|                                                          |")
    print("|     You head Home first before meeting back up with      |")
    print("|     Becky and her friends. You begin to head back out    |")
    print("|     and head back to the school where you meet Becky     |")
    print("|     and three others. You meet Tomas Becky's Camera guy. |") 
    print("|     A tall lanky guy, then there was Tina a shy girl     |")
    print("|     who helps Tomas with filming. The last person        |")
    print("|     Becky introduces is Josh who was there for no        |")
    print("|     other reason but to show off for Becky.              |")
    print("|                                                          |")
    print("|     The five of you set off to the house located on a    |")
    print("|     plot land with no other houses around it. It is      |")
    print("|     now around nine and it is dark enough for you guys   |")
    print("|     to try and get into the house.                       |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print(" __________________________________________________________")
    print("      -----------       ")
    print("     |   next    | 1   ")
    print("      -----------       ")
    print("      -----------                         -----------")
    print("     | Main Menu |  4                    |   EXIT     |  5")
    print("      -----------                         -----------")
    button_Choice_rules_one=input("Please Choose your options with the assigned number: ")
    if(button_Choice_rules_one == "1"):
        ASSS1()
    elif(button_Choice_rules_one == "4"):
       main()
    elif(button_Choice_rules_one == "5"):
        music_Mute()
        Exit()
    else:
        ASS1()
        
#ASSS1 = A Start Sub, Sub 1
#BSSS1 = B Start Sub, Sub 2
#CSSS1 = C Start Sub, Sub 3
def ASSS1():
    print(" __________________________________________________________")
    print("|                                                          |")
    print("| Name:", name.name ,"                                              |")
    print("| Health:", name.HP ,"                                               |")
    print("|                                                          |")
    print("|                                                          |")
    print("|     You and the group get to the house, it has           |")
    print("|     an ominous feel to it, we have to find a way         |")
    print("|     in where should we start looking Becky says.         |") 
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print(" __________________________________________________________")
    print("      -------------       --------------       -----------")
    print("     | Check front | 1   |check windows | 2   | Check back | 3")
    print("      -------------       --------------       -----------")
    print("      -----------                         -----------")
    print("     | Main Menu |  4                    |   EXIT     |  5")
    print("      -----------                         -----------")
    button_Choice_rules_one=input("Please Choose your options with the assigned number: ")
    if(button_Choice_rules_one == "1"):
        ASSS2()
    elif(button_Choice_rules_one == "2"):
        ASSS3()
    elif(button_Choice_rules_one == "3"):
        ASSS4()
    elif(button_Choice_rules_one == "4"):
       main()
    elif(button_Choice_rules_one == "5"):
        music_Mute()
        Exit()
    else:
        ASSS1()

        
def ASSS2():
    print(" __________________________________________________________")
    print("|                                                          |")
    print("| Name:", name.name ,"                                              |")
    print("| Health:", name.HP ,"                                               |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|          You try to open the front door which is taped   |")
    print("|          off with caution type and the door is locked.   |") 
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print(" __________________________________________________________")
    print("                        ---------------       -----------")
    print("                       | Check windows | 2   | Check back | 3")
    print("                        ---------------       -----------")
    print("      -----------                         -----------")
    print("     | Main Menu |  4                    |   EXIT     |  5")
    print("      -----------                         -----------")
    door_L()
    time.sleep(1)
    door_L()
    time.sleep(1)
    door_L()
    button_Choice_rules_one=input("Please Choose your options with the assigned number: ")
    if(button_Choice_rules_one == "2"):
        ASSS3()
    elif(button_Choice_rules_one == "3"):
        ASSS4()
    elif(button_Choice_rules_one == "4"):
       main()
    elif(button_Choice_rules_one == "5"):
        music_Mute()
        Exit()
    else:
        ASSS2()


def ASSS3():
    print(" __________________________________________________________")
    print("|                                                          |")
    print("| Name:", name.name ,"                                              |")
    print("| Health:", name.HP ,"                                               |")
    print("|                                                          |")
    print("|                                                          |")
    print("|       You all split up to check and see if there         |")
    print("|       are any open windows but all of them are sealed    |")
    print("|       shut.                                              |") 
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print(" __________________________________________________________")
    print("      -------------                         -----------")
    print("     | Check front | 1                     | Check back | 3")
    print("      -------------                         -----------")
    print("      -----------                         -----------")
    print("     | Main Menu |  4                    |   EXIT     |  5")
    print("      -----------                         -----------")
    button_Choice_rules_one=input("Please Choose your options with the assigned number: ")
    if(button_Choice_rules_one == "1"):
        ASSS2()
    elif(button_Choice_rules_one == "3"):
        ASSS4()
    elif(button_Choice_rules_one == "4"):
       main()
    elif(button_Choice_rules_one == "5"):
        music_Mute()
        Exit()
    else:
        ASSS3()

def ASSS4():
    print(" __________________________________________________________")
    print("|                                                          |")
    print("| Name:", name.name ,"                                              |")
    print("| Health:", name.HP ,"                                               |")
    print("|                                                          |")
    print("|                                                          |")
    print("|     You go around to the back and there is a hole in     |")
    print("|     back doors window. Josh manages to unlock the back   |")
    print("|     by sticking his hand throught the window's hole.     |") 
    print("|                                                          |")
    print("|                                                          |")
    print("|     When you guys get inside Becky suggests that you guys|")
    print("|     split up. because there is an odd number Becky and   |")
    print("|     Josh head up stairs to look around while you         |")
    print("|     Tomas and Tina search around down stairs.            |")
    print("|     Tomas hands you a flashlight and asks what room you  |")
    print("|     want to search, the living room or the kitchen or the|")
    print("|     Bed room.                                            |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print(" __________________________________________________________")
    print("      -------------       -----------       -----------")
    print("     | Living room | 1   | Bed room  | 2   |  Kitchen  | 3")
    print("      -------------       -----------       -----------")
    print("      -----------                         -----------")
    print("     | Main Menu |  4                    |   EXIT     |  5")
    print("      -----------                         -----------")
    door_U()
    door_O()    
    button_Choice_rules_one=input("Please Choose your options with the assigned number: ")
    if(button_Choice_rules_one == "1"):
        ASSS6()
    elif(button_Choice_rules_one == "2"):
        ASSS8()    
    elif(button_Choice_rules_one == "3"):
        ASSS7()
    elif(button_Choice_rules_one == "4"):
       main()
    elif(button_Choice_rules_one == "5"):
        music_Mute()
        Exit()
    else:
        ASSS4()

def ASSS6():
    print(" __________________________________________________________")
    print("|                                                          |")
    print("| Name:", name.name ,"                                              |")
    print("| Health:", name.HP ,"                                               |")
    print("|                                                          |")
    print("|                                                          |")
    print("|     You pick living room. on your way to living room     |")
    print("|     you pass the basement where you hear it.             |")
    print("|     A woman crying.                                      |") 
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|     You make it to the living room you look around and   |")
    print("|     notice the claw like marks, like someone was being   |")
    print("|     pulled from the front door. Other than that you dont |")
    print("|     note anything else.                                  |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print(" __________________________________________________________")
    print("                        ----------------       ------------")
    print("                       | Go to bed room | 2   |  Go kitchen | 3")
    print("                        ----------------       ------------")
    print("      -----------                         -----------")
    print("     | Main Menu |  4                    |   EXIT     |  5")
    print("      -----------                         -----------")
    crying()
    button_Choice_rules_one=input("Please Choose your options with the assigned number: ")
    if(button_Choice_rules_one == "2"):
        ASSS8()
    elif(button_Choice_rules_one == "3"):
        ASSS7()
    elif(button_Choice_rules_one == "4"):
       main()
    elif(button_Choice_rules_one == "5"):
        music_Mute()
        Exit()
    else:
        ASSS6()
    
def ASSS7():
    print(" __________________________________________________________")
    print("|                                                          |")
    print("| Name:", name.name ,"                                              |")
    print("| Health:", name.HP ,"                                               |")
    print("|                                                          |")
    print("|                                                          |")
    print("|   You head towards the kitchen and same as the livig     |")
    print("|   room you find nothing just a regular kitchen, but      |")
    print("|   as you get ready to head out of the kitchen you        |") 
    print("|   notice a dark figure in the back yard, you double      |")
    print("|   take when you look back agian it's gone.               |")
    print("|                                                          |")
    print("|                                                          |")
    print("|    Then you hear a scream you rush out and check         |")
    print("|    you run into Tomas and Tina.                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print(" __________________________________________________________")
    print("      -----------------            ")
    print("     | Check on scream | 1      ")
    print("      -----------------            ")
    print("      -----------                         -----------")
    print("     | Main Menu |  4                    |   EXIT     |  5")
    print("      -----------                         -----------")
    scream_S()
    button_Choice_rules_one=input("Please Choose your options with the assigned number: ")
    if(button_Choice_rules_one == "1"):
        ASSS9()
    elif(button_Choice_rules_one == "4"):
       main()
    elif(button_Choice_rules_one == "5"):
        music_Mute()
        Exit()
    else:
        ASSS7()
    scream()

def ASSS8():
    print(" __________________________________________________________")
    print("|                                                          |")
    print("| Name:", name.name ,"                                              |")
    print("| Health:", name.HP ,"                                               |")
    print("|                                                          |")
    print("|                                                          |")
    print("|     You head to the bed room and again like the other    |")
    print("|     rooms you find nothing out of the ordinary but notice|")
    print("|     its strange how the bed and everything else in the   |") 
    print("|     house is untouched like no one has ever lived there  |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print(" __________________________________________________________")
    print("     -------------                       ---------------")
    print("    | Living room | 1                   | Go to Kitchen | 3")
    print("     -------------                       ---------------")
    print("      -----------                         -----------")
    print("     | Main Menu |  4                    |   EXIT     |  5")
    print("      -----------                         -----------")
    button_Choice_rules_one=input("Please Choose your options with the assigned number: ")
    if(button_Choice_rules_one == "1"):
        ASSS6()
    if(button_Choice_rules_one == "3"):
        ASSS7()
    elif(button_Choice_rules_one == "4"):
       main()
    elif(button_Choice_rules_one == "5"):
        music_Mute()
        Exit()
    else:
        ASSS3()

def ASSS9():
    print(" __________________________________________________________")
    print("|                                                          |")
    print("| Name:", name.name ,"                                              |")
    print("| Health:", name.HP ,"                                               |")
    print("|                                                          |")
    print("|                                                          |")
    print("|       You Tomas and Tina rush up stairs to where         |")
    print("|       the scream came from you find Becky and            |")
    print("|       look around for Josh but no sign you ask Becky     |") 
    print("|       who is silently on the ground looking at the       |")
    print("|       ceiling that when you notice Josh he was levitating|")
    print("|       on the ceiling.                                    |")
    print("|                                                          |")
    print("|       The room begins shake and you hear a loud get out! |")
    print("|                                                          |")
    print("|       Then Josh drops to the floor and you all scramble  |")
    print("|       to get Becky and Josh up.                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print(" __________________________________________________________")
    print("      ------------------------       -----------------------       ")
    print("     | Head to the front door | 1   | Head to the back door | 2")
    print("      ------------------------       -----------------------      ")
    print("      -----------                         -----------")
    print("     | Main Menu |  4                    |   EXIT     |  5")
    print("      -----------                         -----------")
    button_Choice_rules_one=input("Please Choose your options with the assigned number: ")
    if(button_Choice_rules_one == "1"):
        ASSS11()
    elif(button_Choice_rules_one == "2"):
        ASSS10()
    elif(button_Choice_rules_one == "4"):
       main()
    elif(button_Choice_rules_one == "5"):
        music_Mute()
        Exit()
    else:
        ASSS9()

def ASSS10():
    print(" __________________________________________________________")
    print("|                                                          |")
    print("| Name:", name.name ,"                                              |")
    print("| Health:", name.HP ,"                                               |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|      You all rush to the back of the house where         |") 
    print("|      you guys entered but all of sudden the door slams   |")
    print("|      shut.                                               |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print(" __________________________________________________________")
    print("      -------------------       ----------------------      ")
    print("     | Head to the front | 1   | Try to open the door  | 2   ")
    print("      -------------------       ----------------------      ")
    print("      -----------                         -----------")
    print("     | Main Menu |  4                    |   EXIT     |  5")
    print("      -----------                         -----------")
    door_S2()
    
    button_Choice_rules_one=input("Please Choose your options with the assigned number: ")
    if(button_Choice_rules_one == "1"):
        ASSS11()
    elif(button_Choice_rules_one == "2"):
        ASSS13()
    elif(button_Choice_rules_one == "4"):
       main()
    elif(button_Choice_rules_one == "5"):
        music_Mute()
        Exit()
    else:
        ASSS10()
    
def ASSS11():
    print(" __________________________________________________________")
    print("|                                                          |")
    print("| Name:", name.name ,"                                              |")
    print("| Name:", name.HP ,"                                                 |")
    print("|                                                          |")
    print("|                                                          |")
    print("|    You make it out of the front door with the door       |")
    print("|    slamming behind you all. you all head back to the     |")
    print("|    school where you met up. before leaving you guys      |") 
    print("|    agree to not speak of what happened for fear of       |")
    print("|    being labled crazy.                                   |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print(" __________________________________________________________")
    print("      ----------- ")
    print("     |   Next    | 1")
    print("      ----------- ")
    print("      -----------                         -----------")
    print("     | Main Menu |  4                    |   EXIT     |  5")
    print("      -----------                         -----------")
    door_S()
    button_Choice_rules_one=input("Please Choose your options with the assigned number: ")
    if(button_Choice_rules_one == "1"):
        ASSS12()
    elif(button_Choice_rules_one == "4"):
       main()
    elif(button_Choice_rules_one == "5"):
        music_Mute()
        Exit()
    else:
        ASSS11()

def ASSS12():
    print(" __________________________________________________________")
    print("|                                                          |")
    print("| Name:", name.name ,"                                              |")
    print("| Health:", name.HP ,"                                               |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |") 
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                   Thank You For Playing                  |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print(" __________________________________________________________")
    print("      -----------                         -----------")
    print("     | Main Menu |  4                    |   EXIT     |  5")
    print("      -----------                         -----------")
    button_Choice_rules_one=input("Please Choose your options with the assigned number: ")
    if(button_Choice_rules_one == "4"):
       main()
    elif(button_Choice_rules_one == "5"):
        music_Mute()
        Exit()
    else:
        ASSS12()
def ASSS13():
    print(" __________________________________________________________")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|     You try to pull on door but it wont budge            |") #if main start page option branch option 2 sub branch 2
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print(" __________________________________________________________")
    print("      ----------------       ")
    print("     | Head to front  | 1   ")
    print("      ----------------      ")
    print("      -----------                         -----------")
    print("     | Main Menu |  4                    |   EXIT     |  5")
    print("      -----------                         -----------")
    door_L()
    time.sleep(1)
    door_L()
    time.sleep(1)
    door_L()
    button_Choice_rules_one=input("Please Choose your options with the assigned number: ")
    if(button_Choice_rules_one == "1"):
        ASSS11()
    elif(button_Choice_rules_one == "4"):
       main()
    elif(button_Choice_rules_one == "5"):
        music_Mute()
        Exit()
    else:
        ASSS13()

def BSS2():
    print(" __________________________________________________________")
    print("|                                                          |")
    print("| Name:", name.name ,"                                              |")
    print("| Health:", name.HP ,"                                               |")
    print("|                                                          |")
    print("|                                                          |")
    print("|       You ask Becky why you the new girl, Becky says     |")
    print("|       they needed more hands to help out with getting    |")
    print("|       the scoop on whats really happening at the house.  |") 
    print("|       As well as no one else wants to go because         |")
    print("|       there are rummors that the house nicknamed the     |")
    print("|       house of horrors is haunted.                       |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print(" __________________________________________________________")
    print("      ------------       -----------     -------------------- ")
    print("     | Agree to go | 1  | Ask more  | 2 | Say No and go Home | 3")
    print("      ------------       -----------      -------------------")
    print("      -----------                         -----------")
    print("     | Main Menu |  4                    |   EXIT     |  5")
    print("      -----------                         -----------")
    button_Choice_rules_one=input("Please Choose your options with the assigned number: ")
    if(button_Choice_rules_one == "1"):
        ASS1()
    elif(button_Choice_rules_one == "2"):
        BSSS1()
    elif(button_Choice_rules_one == "3"):
        CSS3()
    elif(button_Choice_rules_one == "4"):
       main()
    elif(button_Choice_rules_one == "5"):
        music_Mute()
        Exit()
    else:
        BSS2()
    
def BSSS1():
    print(" __________________________________________________________")
    print("|                                                          |")
    print("| Name:", name.name ,"                                              |")
    print("| Health:", name.HP ,"                                               |")
    print("|                                                          |")
    print("|                                                          |")
    print("|     You ask more about the house being haunted           |")
    print("|     Becky begins to talk about how the house used to be  |")
    print("|     A Hostel where several women went missing.           |") 
    print("|     And after being closed for some years it was         |")
    print("|     bought out by  Joes family when they moved           |")
    print("|     to town. Before Joe went missing he was going        |")
    print("|     on about how there was a woman crying but no         |")
    print("|     one there.                                           |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print(" __________________________________________________________")
    print("      ------------                         --------------------")
    print("     | Agree to go | 1                    |  Say No and go Home | 2")
    print("      ------------                         --------------------")
    print("      -----------                         -----------")
    print("     | Main Menu | 3                     |   EXIT     |  4")
    print("      -----------                         -----------")
    button_Choice_rules_one=input("Please Choose your options with the assigned number: ")
    if(button_Choice_rules_one == "1"):
        ASS1()
    elif(button_Choice_rules_one == "2"):
        CSS3()
    elif(button_Choice_rules_one == "3"):
        main()
    elif(button_Choice_rules_one == "4"):
        music_Mute()
        Exit()
    else:
        BSSS1()


def CSS3():
    print(" __________________________________________________________")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|   You decicede its not worth it and go home              |")
    print("|   later that day you see on the news teens gone missing. |")
    print("|   You are relieved but feel guilty becasue maybe if you  |")
    print("|   where there you could have change something but....    |")
    print("|   there is no use in you dwelling on it and decide to    |")  
    print("|   keep what happened to yourself and take your seceret   |")
    print("|   to the grave with you.                                 |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                  THE END                 |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                                          |")
    print("|                                   thank you for playing  |")
    print(" __________________________________________________________")
    print("      -----------                         -----------")
    print("     | Main Menu |  1                    |   EXIT     |  2")
    print("      -----------                         -----------")
    button_Choice_rules_one=input("Please Choose your options with the assigned number: ")
    if(button_Choice_rules_one == "1"):
          main()
    elif(button_Choice_rules_one == "2"):
          music_Mute()
          Exit()
    else:
        CSS3()

        
def Exit():
    sys.exit()          
def Music():
    pygame.mixer.music.load("Backwave.wav")
    pygame.mixer.music.play(-1)
def music_Mute():
    pygame.mixer.music.stop()
def door_U():
    time.sleep(2)
    pygame.mixer.Sound.play(door_unlock)
def door_O():
    time.sleep(2)
    pygame.mixer.Sound.play(door_open)
def door_L():
    pygame.mixer.Sound.play(door_knob)
    
def door_S():
    time.sleep(2)
    pygame.mixer.Sound.play(door_shut)
def door_S2():
    time.sleep(1)
    pygame.mixer.Sound.play(door_shut)
def scream_S():
    time.sleep(2)
    pygame.mixer.Sound.play(scream)  
def crying():
    pygame.mixer.Sound.play(women_crying)

    
    
    
    


Music()    
main()
