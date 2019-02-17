def fizzbuzz(n):

    if n % 3 == 0 and n % 5 == 0:
        return("FizzBuzz")
    elif n % 3 != 0 and n % 5 != 0:
        return(str(n))
    elif n % 3 == 0:
        return("Fizz")
    elif n % 5 == 0:
        return("Buzz")

x = int(input("Digite um número: "))

print(fizzbuzz(x))
