name = input('Type your name here: ')
print('Welcome', name, 'to this adventure!')

answer = input('You are on a dirt road, it has come to an end. You can go left or right. Which way would you like to go? ').lower()

if answer == 'left':
    answer = input('You have arrived at a river. You can either walk around it or swim across it. Type walk or swim to decide which you would like to do: ').lower()

    if answer == 'swim':
        print('You swam halfway across before being eaten by a shark!')
    elif answer == 'walk':
        print('You walked for too long and died of dehydration!')
    else:
        print('not a valid option, you lost!')

elif answer == 'right':
    answer = input('You have arrived at a bridge. Would you like to cross or turn back? Type cross or back: ').lower()

    if answer == 'cross':
        answer = input('You crossed the bridge and saw a stranger. Would you like to speak to them? Type yes or no: ').lower()
        if answer == 'yes':
            answer = input('You talk to the stranger and they give you some gold, do you accept the gold? Type yes or no: ').lower()
            if answer == 'yes':
                print('Congratulations, you have won the game!')
            elif answer == 'no':
                print('You did not take the gold and lost the game!')
            else:
                print('not a valid option, you lost!')

        elif answer == 'no':
            print('You decide not to talk to the stranger and lose the game.')
        else:
            print('not a valid option, you lost!')
            
    elif answer == 'back':
        print('You go back and lose!')
    else:
        print('not a valid option, you lost!')

else:
    print('not a valid option, you lost!')