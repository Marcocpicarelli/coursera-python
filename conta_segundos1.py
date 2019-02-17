# Programa que conta horas, minutos e segundos

segundos = input("Quantos segundos você deseja converter? ")

horas = int(segundos) // 3600
segundosrestantes = int(segundos) % 3600
minutos = segundosrestantes // 60
segundosrestantesfinal = segundosrestantes % 60

print(str(horas) + " hora(s), " + str(minutos) + " minuto(s) e " + str(segundosrestantesfinal) + " segundo(s).")
