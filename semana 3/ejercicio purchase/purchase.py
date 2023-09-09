print("------------------------------")
print("********* PURCHASE ***********")
print("------------------------------")

compra = input("Ingresa Valor de la Compra: ")
int_compra = int(compra)
cuotas = input("Ingresa el Número Cuotas: ")
int_cuotas = int(cuotas)
pagar = input("Desea inicar los pagos, ingrese 1 para SI / 2 para NO ")
int_pagar = int(pagar)

montoCuota = int_compra / int_cuotas

print("------------------------------")
print("********* PAIDMENT ***********")
print("------------------------------")

while (pagar != 2):
    if int_cuotas == 0:
      print ("Su compra ya ha sido pagada!")
      break
    else:
      int_cuotas -=1
      int_compra -= montoCuota
      print ("cuotas restante: ", int_cuotas)
      print ("monto restante: ", int_compra)

print ("GRACIAS")