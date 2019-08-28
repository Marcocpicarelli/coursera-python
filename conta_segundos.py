# Função que conta horas, minutos e segundos

def conta_segundos1:

    segundos = input("Quantos segundos você deseja converter? ")

    horas = int(segundos) // 3600
    segundosrestantes = int(segundos) % 3600
    minutos = segundosrestantes // 60
    segundosrestantesfinal = segundosrestantes % 60

    print(str(horas) + " hora(s), " + str(minutos) + " minuto(s) e " + str(segundosrestantesfinal) + " segundo(s).")

# Função que conta dias, horas, minutos e segundos

def conta_segundos2:

    segundos = input("Quantos segundos você deseja converter? ")

    dias = int(segundos) // 86400
    segundosrestantes1 = int(segundos) % 86400
    horas = segundosrestantes1 // 3600
    segundosrestantes2 = segundosrestantes1 % 3600
    minutos = segundosrestantes2 // 60
    segundosrestantesfinal = segundosrestantes2 % 60

    print(str(dias) + " dia(s), " + str(horas) + " hora(s), " + str(minutos) + " minuto(s) e " + str(segundosrestantesfinal) + " segundo(s).")

# Função que conta semanas, dias, horas, minutos e segundos

def conta_segundos3:

    segundos = input("Quantos segundos você deseja converter? ")

    semanas = int(segundos) // 604800
    segundosrestantes1 = int(segundos) % 604800
    dias = segundosrestantes1 // 86400
    segundosrestantes2 = segundosrestantes1 % 86400
    horas = segundosrestantes2 // 3600
    segundosrestantes3 = segundosrestantes2 % 3600
    minutos = segundosrestantes3 // 60
    segundosrestantesfinal = segundosrestantes3 % 60

    print(str(semanas) + " semana(s), " + str(dias) + " dia(s), " + str(horas) + " hora(s), " + str(minutos) + " minuto(s) e " + str(segundosrestantesfinal) + " segundo(s).")
