
def buzz(numero):
    if numero % 5 == 0:
        return True
    else:
        return False


def fizz(numero):
    if numero % 3 == 0:
        return True
    else:
        return False


def fizzbuzz(numero):
    if buzz(numero) == True and fizz(numero) == True:
        return "FizzBuzz"
    elif buzz(numero) == False and fizz(numero) == True:
        return "Fizz"
    elif buzz(numero) == True and fizz(numero) == False:
        return "Buzz"
    else:
        return numero


