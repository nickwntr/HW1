def send_mail(msg,recipient,sender = "university.help@gmail.ru"):
    dflt_sender = "university.help@gmail.ru"
    domains = [".ru",".com",".net"]
    recip_domain = False
    send_domain = False
    for domain in domains:
        if not recip_domain:
            if recipient.find(domain) > 0:
                recip_domain = True

        if not send_domain:
            if sender.find(domain) > 0:
                send_domain = True
    print()
    if recipient.find("@") < 0 or sender.find("@") < 0 or (not recip_domain and not send_domain):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return 0
    if sender == recipient:
        print("Невозможно отправить самому себе")
        return 0
    if sender != dflt_sender:
        print("Нестандартный отправитель".upper())
    print(f"Письмо отправлено с адреса {sender} на адрес {recipient}")
    return 1

send_mail("Good Morning", "upperlimit@ya.ru")
send_mail("Chain Mail", "fi-noReply.ru")
send_mail("ToMyself", "upperlimit@ya.ru", "upperlimit@ya.ru")
send_mail("FromAnother", "shagohod@jmail.com", "upperlimit@ya.ru")