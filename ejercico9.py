inversion = float(input("indique el dinero que desea invertir: "))
interes= float(input("indique el interes anual (%): "))

interes = interes/100

años = int(input("indique el numero de años que desea mantener el dinero: "))

Capital = (inversion*((interes+1)**años))

print("el capital obtenido en ",años," años =",Capital)