masa = float(input("indique aqui su peso en kg: "))
altura = float(input("indique aqui su altura en metros: "))

imc = masa/(altura**2)

round(imc,2)

print("tu indice de masa corporal es: ",imc)