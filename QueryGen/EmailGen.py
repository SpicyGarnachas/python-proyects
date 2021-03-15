import random
emails = {
    1: "@gmail.com",
    2: "@protonmail.com",
    3: "@outlook.com",
    4: "@hotmail.com",
    5: "@yahoo.com",
    6: "@icloud.com",
}

def gen_mail():
    rand_num = random.randint(1, 6)
    return str(emails[rand_num])
