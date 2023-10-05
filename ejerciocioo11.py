dinerocuenta =float(input("indique el dinero depositado en la cuenta: "))

año1 = dinerocuenta*1.04
año2 = dinerocuenta*(1.04)**2
año3 = dinerocuenta*(1.04)**3
año1 = round(año1,2)
año2 = round(año2,2)
año3 = round(año3,2)
print("el dinero tras el primer año es ",año1,"el dinero tras el segundo año es ",año2,"el dinero tras el tercer año es ",año3)