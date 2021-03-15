import random

# 65-90
def upper_cas():
    return chr(random.randint(65, 90))

# 97-122
def lower_cas():
    return chr(random.randint(97, 122))

# 48-57
def numbers():
    return chr(random.randint(48, 57))

# 33-47
def symbols():
    return chr(random.randint(33, 47))

def generate_pass(lenght_pass):
    password = ""
    count_gen = 0

    while lenght_pass > count_gen:
        selector = random.randint(0, 3)
        if selector == 0:
            password = password + upper_cas()
        elif selector == 1:
            password = password + lower_cas()
        elif selector == 2:
            password = password + numbers()
        else:
            password = password + symbols()
        count_gen += 1
    return password
