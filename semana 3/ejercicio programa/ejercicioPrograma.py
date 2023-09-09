print("--------------------------------")
print("********** PROGRAM ***********")
print("--------------------------------")

print("\n Choice an option:")
opc = input(" 1 - START\n 0 - CLOSE\n")
int_opc = int(opc)

while (int_opc != 0 and int_opc == 1):
  print("--------------------------------")
  print("********** MAIN MENU ***********")
  print("--------------------------------")

  print("\n Choice an option:")
  menuOpc = input(" 1 - Sing in\n 2 - Login\n 0 - Exit\n")
  int_menuOpc = int(menuOpc)

  if int_menuOpc == 1:
    print("------------------------------")
    print("********** SIGN UP ***********")
    print("------------------------------")

    user_name = input("Ingresa nombre: ")
    user_email = input("Ingresa email: ")
    user_phone = input("Ingresa número de teléfono: ")
    user_password = input("Ingresa contraseña: ")

  elif int_menuOpc == 2:
    print("------------------------------")
    print("*********** LOGIN ************")
    print("------------------------------")

    captcha = 25

    user_validation = input("Ingrese email o número de telefono: ")
    password_validation = input("Ingrese contraseña: ")
    captcha_validation = input("CAPTCHA - Resuelva la siguiente ecuación: 5*5 = ?")
    int_captcha = int(captcha_validation)

    if user_email == user_validation or user_phone == user_validation:
        if password_validation == user_password:
          if int_captcha == captcha:
            login = True
            print("Bienvenido" , user_name)

            while (login == True):
                print("--------------------------------")
                print("********** USER MENU ***********")
                print("--------------------------------")

                print("\n Choice an option:")
                menuOpc2 = input(" 1 - Game\n 2 - CreditCard\n 0 - Back\n")
                int_menuOpc2 = int(menuOpc2)

                if int_menuOpc2 == 1:
                  print("--------------------------------")
                  print("********** LIVE GAME ***********")
                  print("--------------------------------")

                  import random
                  vidas = 3
                  puntos = 0

                  while(vidas != 0):
                      num = random.randint(0, 9)
                      if num == 0:
                          vidas -=1
                          print ("vidas: ", vidas)
                      else:
                          puntos +=1
                          print ("puntos: ", puntos)

                elif int_menuOpc2 == 2:
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

                elif int_menuOpc2 == 0:
                  break


    else:
      print("usuario o contraseña inválidos")





print("GRACIAS!")