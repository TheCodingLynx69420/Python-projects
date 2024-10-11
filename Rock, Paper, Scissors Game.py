import random

def Gamewin(comp, you):
    if comp==you:
        return None
    elif comp =='R':
        if you == 'S':
            return False
        elif you == 'P':
            return True
    elif comp == 'P':
        if you == 'R':
            return False
        elif you == 'S':
            return True
    elif comp == 'S':
        if you == 'P':
            return False
        elif you == 'R':
            return True

print("Comp turn: Will Choose; Rock(R), Paper(P), or Scissors(S)")
randomNo=random.randint(1,3)
if randomNo == 1:
    comp= 'R'
elif randomNo == 2:
    comp = 'P'
elif randomNo == 3:
    comp = 'S'

you = input("Your turn:Choose Rock(R), Paper(P), or Scissors(S):  ")
a = Gamewin(comp,you)

print(f"Computer Choosed:  {comp}")
print(f"You Choosed:  {you}")

if a==None:
    print ("The game is a tie!")
elif a:
    print("You win!!")
else:
    print("You lose!")
