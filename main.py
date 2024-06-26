#Функция проверки на палиндром
def is_palindrome(user_string):
    user_string = user_input.lower().replace(" ", "")
    return user_string == user_string[::-1]

#Получение строки от пользователя
user_input = input("Введите строку: ")
#Вызов функции и вывод
if is_palindrome(user_input):
    print(f'"{user_input}" является палиндромом')
else:
    print(f'"{user_input}" не является палиндромом')
