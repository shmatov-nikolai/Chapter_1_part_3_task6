'''
6. Напишите программу, которая генерирует случайные пароли. Имейте ввиду, что хорошие
пароли сочетают в себе строчные и прописные буквы, а так же числа и символы. Пароль
должен генерироваться каждый раз, когда пользователь просит об этом
Дополнительно:

Пользователь должен выбрать на сколько сильным должен быть его пароль.
'''
import random

def password_gen(key):
    if key == 1:
        len_pass = 10
        i = 0
        rand_pass = []
        while i < len_pass:
            rand_pass.append(str(random.randint(0, 9)))
            i += 1
            if i == len_pass:
                pass_for_user = ''.join(rand_pass)
                verify_pass = input(f'''Ваш сгенерированный пароль: {pass_for_user} 
если Вас устраивает данный пароль, введите: 'y' 
если нет, то: 'n'
: ''')
                if verify_pass == 'y':
                    break
                elif verify_pass == 'n':
                    i = 0
                    rand_pass = []
        return pass_for_user
    if key == 2:
        len_pass = 16
        i = 0
        rand_pass = []
        list_pass = ['a','A','b','B','c','C','d','D','e','E','f','F',
                     '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','*','#','$','!','@','$','&']
        while i < len_pass:
            rand_pass.append(list_pass[random.randint(0, len(list_pass)-1)])
            i += 1
            if i == len_pass:
                pass_for_user = ''.join(rand_pass)
                verify_pass = input(f'''Ваш сгенерированный пароль: {pass_for_user} 
если Вас устраивает данный пароль, введите: 'y' 
если нет, то: 'n'
: ''')
                if verify_pass == 'y':
                    break
                elif verify_pass == 'n':
                    i = 0
                    rand_pass = []
        return pass_for_user

vibor_key = int(input('''
Выберите сложность генерации пароля:
1. Простой пароль (длина пароля: 10 символов, только цифры)
2. Хороший пароль (длина пароля: 16 символов, содержит строчные и 
                   заглавные буквы, а так же числа и символы)
Ваш выбор:'''))

password_user = password_gen(vibor_key)
print(f"Вот Ваш сгенерированный пароль: {password_user}")
