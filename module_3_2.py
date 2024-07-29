def is_email(text_to_check: str) -> bool:
    suffixes = "ru", "net", "com"
    if ("." in text_to_check) and ("@" in text_to_check):
        text_to_check = text_to_check.split(".")
        return bool(any(suffix in text_to_check[-1] for suffix in suffixes))
    else:
        return False


def sender_and_recipient_is_email(sender: str,
                                  recipient: str,
                                  *args) -> bool:
    return is_email(sender) and is_email(recipient)


def email_is_not_equal(sender: str,
                       recipient: str,
                       *args) -> bool:
    return sender != recipient


def sender_is_standard(sender: str,
                       recipient: str,
                       standard_sender: str) -> bool:
    return sender == standard_sender


def send_email(message: str,
               recipient: str,
               sender: str = "university.help@gmail.com"):
    standard_sender = "university.help@gmail.com"
    logs = (f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}",
            "Нельзя отправить письмо самому себе!",
            f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.",
            f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    conditions = (sender_and_recipient_is_email,
                  email_is_not_equal,
                  sender_is_standard)
    for condition_number in range(len(conditions)):
        if not conditions[condition_number](sender, recipient, standard_sender):
            print(logs[condition_number])
            return
    else:
        print(logs[-1])
        return


if __name__ == "__main__":
    send_email("Hey, yo!", "golodrol@bk.ru", "university.help@gmail.com")
