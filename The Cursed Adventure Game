hp_pts = 3
name = (input("Enter your name: "))
print(f"Hello {name}, Welcome to This adventurous game!\n")
print("-------------------------------")
direction =(input("You are in a jungle and were going on a straight path but suddenly a giant spider came out of trees who is now about to chase you,\nHowever there is a left path and a right path,\nWhich one would you choose to run?:\n (type left or right):  "))
#============================================================Scene 1 (path selection)
if direction == "right":
    print("you choosed to go right, there are a bunch of bushes in that path\n")
elif direction == "left":
    print("you choosed to go left, there is a river you have swim through it\n")
else:
    print("invalid answer, the spider caught you\n =============YOU DIED============\n better luck next time!\n              ========ENDING: 1======= ")


#===========================================================Scene 2 (make your way)
if direction == "right":
    Q = input('''Quickly tap "Q" to cut your way through the bushes!: \n''')
    if Q == "Q":
        print("Yes! you managed to make your way through the bushes! and you noticed that the spider is nowhere to be seen\n")
    else:
        print("invalid button, the spider caught you with its web!\n =============YOU DIED============\n better luck next time!\n              ========ENDING: 2=======")
    
elif direction == "left":
    E = input('''Quickly tap "E" to swim faster through the river!: \n''')
    if E == "E":
        print("Yes! The spider has skill issues of not swimming, you managed to escape from the spider!\n")
    else:
        print("invalid button, the spider caught you with its web!\n =============YOU DIED============\n better luck next time!\n              ========ENDING: 2=======")
#==========================================================Scene 3 ("right" path exclusive: the monkeys)
if "right" in direction:
    print('''But suddenly lots of monkeys out of nowhere comes out of tree and started laughing\n You asked them why they are laughing and then\n suddenly an Ape came from A very big tree in the middle\n the ape looked like it was the king of these monkeys,\n He quickly throws his sword towards you\n  ''')
    C = input('''Quickly tap "C" to catch the sword!: \n''')
    if C == "C":
        print("You managed to catch it!\n ")
    else:
        print("You failed to tap on the right button!, the sword impaled you\n ==========YOU DIED============\n better luck next time!\n              ========ENDING: 3=======")
    if C == "C":
        print("It seems like the monkey king is impressed by how you escaped the spider and now he wants to challenge you to a duel!\n")
        print("The monkey king attacks with his weapon which is a giant tree log!\n")
        A = input("Tap A to crouch and dodge it!\n")
        if A == "A":
            print("Yes! you dodged it!, the king seems more excited now!\n the whole crowed of monkeys are cheering you!\n")
        else:
            print(f"You failed to click the right button!, the tree log hits on your face!\n")
            hp_pts = 2
            print (f"{hp_pts} hp left")
        print("the monkey king now furiously sweep his wood log and about to hit your legs!\n")
        F = input("Tap F to jump and dodge!\n")
        if F == "F":
            print("Great! you dodged it!,\n now the monkey king seems to have run out of stamina!\n its your chance attack him! \n")
        else:
            print("The log hits on your legs! your legs are now seriously injured!\n")
            if hp_pts == 2:
                hp_pts = 0
                print(f"{hp_pts}  hp left, you died\n ======Game over======\n              ========ENDING: 4=======")
            else:
                hp_pts = 1
                print(f"{hp_pts} hp left\n")
                print("Great! you dodged it!,\n now the monkey king seems to have run out of stamina!\n its your chance attack him! \n")
                
        if hp_pts >= 1:
            B = input("Tap B to defeat the monkey king!\n")
            if B == "B":
                print(f"you drawed your sword on monkey king and now he is on his knees and surrendered\n he then suddenly lifted you and cheered you!\n   it seems like you are their leader now!\n ======= Good Ending!=====")
            else:
                print(f"You did nothing and now monkey king quickly attacked you and throws you in the valley\n =======You DIED========\n            ========ENDING: 5=========")
        #=========================================================================== "left" path exclusive: the rangers
if "left" in direction:
    print('''Now you noticed that a group of sharks started surrounding you!!, \n But suddenly a group of rangers came in a boat to rescue you. ''' )
    R = input('''They threw a rope towards you\n. press "R" to Grab the rope!!\n''')
    if R == "R":
        print ("Yes now you climbed the boat and it seems like you are safe\n The rangers then ask you what you were doing swimming in that dangerous river\n Then you explained them everything that has happened up until now\n Ranger 1: damn that is such a brave thing to do!\n Ranger 2: I think he is bluffing haha! no one has ever survived the giant spider in this area!")
        print ("\n then you showed them the scars you got while running and they finally believed you\n Ranger 1: Look i dont know how you got here since this jungle has been sealed from weeks!\n Then suddenly you also realised that you also dont have any idea how you got here in the first place, you suddenly got a flashback of reading a book\n BAAAAAAAAAAAAAAAAM!!\n Ranger 1: The heck was that sound! it seems like we crashed into something!\n  ")
        print ("Ranger 2: I dont know that was that i didn't see anything while driving the boat!\n Ranger 1: It looks like something must have crashed into our boat from under the water\n SHEEEEEEEEEWWWWW!!\n Suddenly a strange looking Monster came out of the river!\n Ranger 1: Its THE KRAKEN!\n The KRAKEN threw a big rock towards the ship!\n")
        H = input('''Quickly Press "H" crouch down to dodge!''')
        if H == "H":
            print("YES you dodged it!\n")
            print("The Rangers are impressed by your skills of dodging!\n")
            print("Ranger 1: here take this gun i think you can handle this while i distract this monster\n")
            print("Ranger 2: Get yourself ready! i will speed up this boat make sure to stay firm!\n")
            print("Ranger 1: Aggh, i am slipping!\n")
            print("You noticed that the monster might get distracted if you let the ranger slip and you would get an opening to shoot the monster!")
            T = input('''Save the ranger? Press "T" or Dont save the ranger? Press "Y" \n''')
            if T == "T":
                print(f"You saved him!\n Ranger 1: Thanks a lot! man, i owe you, god that was embarassing!\n Ranger 2: Damn {name} you have the skills to become one of us haha\n ")
                print(f"Ranger 2: Look i got a plan, i will speed up my boat towards that monster and try to crash it, when that monster will try to look down and come closer to us {name} will shoot on its eyes, i know its very risky but this is the best we got!\n  ")
                Z = input("Ranger 2: Alright lets do this!,\n The boat is now in high speed!\n Ranger 2: Noww! the monster seems to look down its your chance shoot him!\n Press Z to shoot!\n")
                if Z == Z:
                    print("Dishhkiooow! Bulls eye! you shot the monster on his eyes and he fell down in the river like it died!\n Ranger 1: Yes we did it YESS!\n Ranger 2: Good shot! man i want you to join our organization! haha\n suddenly you started feeling dizzy...\n???: DAD wake up! DAD!\n What? you are now in your daughter's room,\n Stacey (your 6 years old daughter): Dad you said you would tell me a story about a jungle adventure! come on\n i want to listen to it now! then you can go back to sleep.\n You started remember everything! the whole thing that happend now was nothing but just some evil illusion caused by\n that strange jungle adventure book you found on your way to home, you were reading that book but it seems like it curses\n the reader into becoming the protagonist of the book\n god knows how many times you were in the loop but now you have to end it,\n its your only chance!\n  ")
                    P = input('''Burn the cursed book and end it all? Press "P"\n OR Dont Press P to not burn it?\n  ''')
                    if P == "P":
                        print("You choosed to burn the book, you told your whole family about your story,\n of course not everyone believed in you,\n but only You know what really happened\n          ========ENDING: 6=======")
                    else:
                        print("You choosed to not burn the book, after all you had a lot of fun in that illusion so why let all the fun go away?.... =========Ending: 7=======")
            if "Y" in T:
                print("You let him slipped into the river!, Ranger 2: NOOOOO!,\n the monster now quickly crouched down to grab the ranger you then shot the monster on its face\n The monster fell into the river like it died but the ranger was also in its hands so both the monster and ranger drowned,\n Ranger 2: YOU, WHY DIDNT YOU SAVE HIM!?, You tried reason with him but he is very angry,\n Ranger 2: GET OFF! JUST GET OFF!\n you have no choice but to leave the boat now you are alone on your own again\n suddenly you started feeling dizzy...\n???: DAD wake up! DAD!\n What? you are now in your daughter's room,\n Stacey (your 6 years old daughter): Dad you said you would tell me a story about a jungle adventure! come on i want to listen to it now!\n then you can go back to sleep!.\n You started to remember everything! the whole thing that happend now was nothing but just some evil illusion\n caused by that strange jungle adventure book you found on your way to home, you were reading that book\n but it seems like it curses the reader into becoming the protagonist of the book\n god knows how many times you were in the loop but now you have to end it,\n its your only chance!\n  ")
                P = input('''Burn the cursed book and end it all? Press "P"\n OR Dont Press P to not burn it?\n  ''')
                if P == "P":
                    print("You choosed to burn the book, you told your whole family about your story,\n of course not everyone believed in you,\n but only You know what really happened\n              ========ENDING: 6=======")
                else:
                    print("You choosed to not burn the book, after all you had a lot of fun in that illusion so why let all the fun go away?.... =========Ending 7=======")    
        else:   
            print(f'''The rock hits you!\n''')
            print("The rangers seems dissapointed in your dodging skills\n")
            print("Ranger 2: I dont think you have any skills of using a gun also, so make yourself useful and distract that monster while we try to get a shot on it\n")
            print("Ranger 2: Alright lets do this!,\n The boat is now in high speed!\n Ranger 1: Alright I am about to shoot!.\n Dishkiooooow, Ranger shot on his arm accedently The monster does not seems to be hurt at all\n Ranger 2: Shit, we should have made a plan!\n The monster is now about to attack! you dont have any choice ")
            V = input("Press V to sacrifice both rangers while you run away with boat, or Dont press V to sacrifice yourself\n")
            if V == "V":
                print("You Pushed both the rangers into the river,\n Ranger 2: What are you doing!,\n  Ranger 1: I thought we could trust you!\n The monster suddenly grabbed both the rangers and ate them while you escaped while speeding the boat.\n suddenly you started having flashbacks of your family and your boat crashed into a Rock!, And the monster suddenly jumped on your boat\n ===========YOU DIED============\n Sometimes its hard to make choices... \n              ========ENDING: 8======= ")
            else:
                print(f"You were too scared to push the rangers instead you saved them and sacrificed yourself,\n Ranger 1: NOOO! {name}!!\n   Ranger 2: Shit {name} you have my respect man!, sorry but we dont have any choice but to run away!\n You were a true hero!\n ===========YOU DIED============\n Like a hero!  \n              ========ENDING: 9=======")
    else:
        print("You failed to catch the rope! the sharks got you\n ===========YOU DIED============\n better luck next time!")
print('''======Thanks a lot for playing!=====\n I hope you like this game, i know it might be boring but this is my first ever big game project\n i have worked on this game with much critical thinking and hard work!\n I hope you all enjoyed playing this mini game\nCredits: Programmed by: (NINJA)\n Plot and Story by: (NINJA)\n                As you might have guessed there are 2 different paths in this game so besure to try both and give your review!\n                And remember! Every choices have consequences. (This game has a total of 9 different endings)   ''')    
