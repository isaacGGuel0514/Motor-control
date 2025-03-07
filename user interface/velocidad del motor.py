welcome_message=["""
BIENVENIDO AL SISTEMA MOTOR CONTROL
para comenzar, debes introducir una velocidad deseada:
Introduce la velocidad:"""]

while True:
    
     user_velocity=input(welcome_message)
    
     if user_velocity.isnumeric():
          user_velocity=int(user_velocity)
          if user_velocity<=300:
               print(user_velocity)
          else:
               print("el usuario no ingresó una velocidad valida")
     else:
          print("el usuario no ingresóuna velocidad valida")

    


