import random
n = random.randint (1,100)
try:
    a = -1
    guesses = 1
    while (a != n):
        a = int(input("Enter your guessed number:  "))
        if (a>n):
            print("Enter a lower number please!")
            guesses +=1
        elif (a<n):
            guesses +=1
            print("Enter a higher number please!")
        
    print(f'''Congratulations! you have guessed the number "{n}" in {guesses} attempt(s)''')
except:
    print("Error occured Please enter a 'number', as your punishment the game will have to restart!")
