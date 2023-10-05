a = 'gato'
b = "O gato subiu no telhado"
c = "telhado"

print(a == b[2:6])
print(a == b)
print(a > c)
print(a > b)
print(a != c)
print(c == b[16:])
print(c == b[15:])
print(a == b[2:5])


def fazAlgo(string):
    pos = len(string) - 1
    string = string.upper()
    while pos >= 0:
        print(string[pos], end="")
        pos = pos - 1


fazAlgo('paralelepipedo')

print()

def fazAlgo2(string):
    pos = 0
    string1 = ""
    string = string.lower()
    stringMA = string.upper()

    while pos < len(string):
        if pos % 2 == 0:
            string1 = string1 + stringMA[pos]
        else:
            string1 = string1 + string[pos]
        pos = pos + 1
    return string1


print(fazAlgo2("paralelepipedo"))

print()
def fazAlgo3(string):
    pos = 0
    string1 = ""

    while pos < len(string):
        if string[pos] != " ":
            string1 = string1+string[pos]
        pos = pos + 1

    string1 = string1.capitalize()
    return string1


print(fazAlgo3("É UM TESTE"))