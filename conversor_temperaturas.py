# Conversor de Kelvin para Fahrenheit
def kelvin_fahrenheit(k):
    c = k - 273
    f = ((9 * c) / 5) + 32
    return f

# Conversor de Kelvin para Celsius
def kelvin_celsius(k):
    c = k - 273
    return c

# Conversor de Fahrenheit para Kelvin
def fahrenheit_kelvin(f):
    c = ((f - 32) * 5) / 9
    k = c + 273
    return k

# Conversor de Fahrenheit para Celsius
def fahrenheit_celsius(f):
    c = ((f - 32) * 5) / 9
    return c

# Conversor de Celsius para Fahrenheit
def celsius_fahrenheit(c):
    f = ((9 * c) / 5) + 32
    return f
