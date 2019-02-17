# Programa que conta dias, horas, minutos e segundos

segundos = input("Quantos segundos você deseja converter? ")

dias = int(segundos) // 86400
segundosrestantes1 = int(segundos) % 86400
horas = segundosrestantes1 // 3600
segundosrestantes2 = segundosrestantes1 % 3600
minutos = segundosrestantes2 // 60
segundosrestantesfinal = segundosrestantes2 % 60

print(str(dias) + " dia(s), " + str(horas) + " hora(s), " + str(minutos) + " minuto(s) e " + str(segundosrestantesfinal) + " segundo(s).")
