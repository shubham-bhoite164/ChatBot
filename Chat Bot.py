import random

var_1 = ['hi','hello']
var_2 = ['how are you','how are you doing','how is your health']
var_3 = ['what is your name','how do I call you','name','your name please']
var_4 = ['programming language','what should I learn']
var_5 = ['what are your hobbies','what do you do in your free time']

while True:
    user_input = input('user said to bot: ')

    if user_input.lower() in var_1:
        bot = ['hellow','hi']
        print('Bot replied to user: ' + random.choice(bot) + '\n')

    elif user_input.lower() in var_2:
        bot = ['I am good','I am doing good','finest ever']
        print('Bot replied to user: ' + random.choice(bot) + '\n')

    elif user_input.lower() in var_3:
        bot = ['My name is Friday','You can me as Friday', 'My name is Friday']
        print('Bot replied to user :' + random.choice(bot) + '\n')

    elif user_input.lower() in var_4:
        bot = ['Python','Python programming language']
        print('Bot replied to user :' + random.choice(bot) + '\n')

    elif user_input.lower() in var_5:
        bot = ['Learning programming language','coding']
        print('Bot replied to user :' + random.choice(bot) + '\n')

    else:
        print("Bot replied to user - Sorry I didn't understand")
