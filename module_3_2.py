a = 0


def send_email(message, recipient, sender='university.help@gmail.com'):
    if '@' not in sender and '@' not in recipient:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    if '.net' in sender or '.ru' in sender or '.com' in sender:
        pass
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    if '.net' in recipient or '.ru' in recipient or '.com' in recipient:
        pass
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    if sender == recipient:
        print(f'Нельзя отправить письмо самому себе!')
        return
    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
        return



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


