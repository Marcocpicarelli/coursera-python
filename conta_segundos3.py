# Programa que conta semanas, dias, horas, minutos e segundos

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
