def incomodam(n):
    if n < 1:
        return ""
    else:
        return "incomodam " + incomodam(n - 1)


def elefantes(n):
    if n < 1:
        return ""
    if n == 1:
        return "Um elefante incomoda muita gente\n"
    else:
        frase1 = str(n) + " elefantes " + incomodam(n) + "muito mais\n"
        frase2 = str(n) + " elefantes incomodam muita gente\n"
        return elefantes(n - 1) + frase1 + frase2


print(elefantes(4))
