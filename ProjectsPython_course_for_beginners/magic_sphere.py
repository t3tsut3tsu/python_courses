import random
import time
def choice(question):
    answer = ['Undoubtedly', 'Predetermined', 'No doubt', 'Definitely yes', 'You can be sure of it', 'It seems to me - yes', 'Most likely', 'Good prospects', 'Signs say - yes', 'Yes', 'It is not clear yet, try again', 'Ask later', "It's better not to tell", "It's impossible to predict now", 'Concentrate and ask again', "Don't even think", 'My answer is no', 'According to my data - no', 'Prospects are not very good', 'Very doubtful']
    choosen = random.randint(0, len(answer) - 1)
    return answer[choosen]
print("Hello World, I'm a magic ball, and I know the answer to any question you have.\nWhat's your name?")
name = input()
print(f'Hello, {name}')
again = 'y'
while again.lower() == 'y':
    print("What's your question?")
    user_question = input()
    print('\nMagic sphere is thinking...\n')
    time.sleep(1)
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print(f'Okay, your answer is: {choice(user_question)}')
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n')
    print(f'Want to ask magic sphere again, {name}? (y or n)')
    again = input()
    if again.lower() == 'n':
        print("Thanks for coming. We'll see you again...")
        break