print("------------------------------")
print("********** SIGN UP ***********")
print("------------------------------")

user_name = input("Ingresa nombre: ")
user_email = input("Ingresa email: ")
user_phone = input("Ingresa número de teléfono: ")
user_password = input("Ingresa contraseña: ")

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
        print("Bienvenido" , user_name)
else:
  print("usuario o contraseña inválidos")