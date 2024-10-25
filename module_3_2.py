

def send_email(message, recipient, sender):
    sender_non = (input("Адрес отправителя: "))
    if '@' in recipient and sender and sender_non:
        if '.com' or '.net' or '.ru' in recipient and sender and sender_non:
            if sender_non == recipient:
                print("Нельзя отправить самому себе!")
            elif sender_non == sender:
                print(f"Письмо успешно отправлено с адреса {sender_non} на адрес {recipient}.")
            else:
                print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!"
                      f"Письмо успешно отправлено с адреса {sender_non} на адрес {recipient}.")
        else:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    else:
        print("Это не e-mail адрес!")


recipient = (input("Получатель сообщения: "))
message = (input("Введите текст сообщения: "))
sender = "university.help@gmail.com"

send_email(message, recipient, sender)
