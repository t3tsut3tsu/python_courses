import random
def is_valid(n):
    if n.isdigit() and 1 <= int(n) <= m:
        return True
    else:
        return False
def num_guessing(n):
    counter = 0
    while True:
        if is_valid(n) == False:
            print(f'But maybe we should still enter an integer from 1 to {m}?')
            n = input()
            continue
        else:
            n = int(n)
            if n > number:
                print('Your number is higher than the one you have guessed, try again')
                print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
                counter += 1
                n = input()
                continue
            elif n < number:
                print('Your number is less than the one you thought of, try again')
                print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
                counter += 1
                n = input()
                continue
            elif n == number:
                print(f'You guessed it, congratulations! You guessed the number in {counter} attempts')
                break
while True:
    print('Do you want to play the number guessing game?')
    answer = input()
    if answer.lower() == 'да' or answer.lower() == 'д' or answer.lower() == 'y' or answer.lower() == 'yes':
        print('Welcome to the number guessing game')
        print('Enter the right border of the range')
        m = int(input())
        number = random.randint(1, m)
        print(f'Enter a number from 1 to {m}')
        n = input()
        num_guessing(n)
        continue
    elif answer.lower() == 'нет' or answer.lower() == 'н' or answer.lower() == 'n' or answer.lower() == 'no':
        print("Thanks for coming. See you!")
        break
    else:
        print("Try to write 'yes' or 'no'")
        continue