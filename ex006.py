import random as rnd

prpDic={0:'Snake',1:'Water',2:'Gun'}
matrix=[['D','W','L'],['L','D','W'],['W','L','D']]

def SnkWtrGun():
    print('0.Snake \n1.Water\n2.Gun')
    plyrChoice=int(input('Enter your choice \n'))
    if plyrChoice<0 and plyrChoice>2:
        print('Invalid choice')
        SnkWtrGun()
        return
    print(f'Your Choice : {prpDic.get(plyrChoice)}')
    compChoice=rnd.randint(0, 2)
    print(f'Computer Choice : {prpDic.get(compChoice)}')
    reslt=matrix[plyrChoice][compChoice]
    match reslt:
        case 'D':
            print('It is draw, Try again !!!')
            SnkWtrGun()
            return
        case 'W':
            print('Congrats you won  !!!')
            return
        case 'L':
            print('Sorry you lost  !!!')
            return

SnkWtrGun()

