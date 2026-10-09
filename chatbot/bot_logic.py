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
    
def mt():
    temp = random.randint(1 , 32)
    if temp <= 0:
        return("Fa molto freddo, mettiti una giacca e un cappello")
    elif temp <= 12:
        return("Fa freddo, mettiti una giacca")
    elif temp <= 25:
        return("E' caldo, divertiti all'aperto!")
    elif temp <= 32:
        return("Fa troppo caldo, mettiti un berretto")
    elif temp > 32:
        return("fatti un bagno a mare!")
        
