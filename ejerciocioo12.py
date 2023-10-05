barrasdia =int(input("barras de pan que no son del dia: "))
print("el precio de una barra de pan es de 3.49")
descuento = 3.49*0.6
print("el descuento por no ser del dia es de",descuento)
preciobarra = (3.49-descuento)
ganancia = (barrasdia*preciobarra)
ganancia = round(ganancia,2)
print("la ganancia total es de ",ganancia," euros")