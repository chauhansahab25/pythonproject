import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
comp =print("comp turn: Snake(s) Water(w) Gun(g)?")
randNo=random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
you=input("your turn: Snake(s) Water(w) Gun(g)?")
gameWin(comp, you)

print(f'computer choose:{comp}')
print(f'You choose:{you}')

if gameWin(comp, you)==None:
    print('This gameis tie!')
elif gameWin(comp, you)==True:
    print('You win!')
else:
    print('you lose!')