import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
def carta_forbice_sasso():
    scelta = random.randint(0, 2)
    if scelta == 0:
        return "CARTA"
    elif scelta == 1:
        return "FORBICE"
    else:
        return"SASSO"