counter = 1

while counter <= 3:
    login = input("Введіть свій логін: ")
    password = input("Введіть пароль: ")
    if login == "admin" and password == "qwerty":
        print("Авторизацію успішно пройдено з", counter, "спроби")
        break
    if counter < 3:
        print("Дані не вірні. Спробуйте ще раз. У вас залишилось", 3 - counter, "спроб.")
    counter +=1
else:
    print("Ви ввели невірні дані 3 рази, ваш акаунт заблоковано")