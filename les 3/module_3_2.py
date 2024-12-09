def check(adress_string):
    pos_first = adress_string.find(sobaka)
    if pos_first == -1:
        return False

    pos_last = adress_string.rfind(sobaka)
    if pos_first != pos_last:
        return False

    pos_dot = adress_string.rfind(".")

    if pos_dot == -1:
        return False

    domain = adress_string[pos_dot + 1:]
    if not domain in domains:
        return False

    return True




def send_email(message, recipient, *, sender="university.help@gmail.com"):

    if not (check(recipient) and check(sender)):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return


    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return


    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        return
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
        return





sobaka = "@"
domains = "com", "ru", "net"

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')