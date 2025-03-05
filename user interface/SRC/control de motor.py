welcome_message = """
    BIENVENIDO AL SISTEMA MOTOR CONTROL
    Para comenzar, debes introducir una velocidad deseada y el sentido de giro:
"""
print(welcome_message)


while True:
    user_velocity = input("Introduce una velocidad en el rango válido (0-225 rpm) o escribe STOP para detener el motor: ").strip()

    if user_velocity.upper() == "STOP":
        print({"sentido": "Ninguno", "velocidad": 0})
        print("El motor se ha detenido.")  
        break

    try:
        user_velocity = int(user_velocity)
    except ValueError:
        print("Error: Debes ingresar un valor numérico. Intenta de nuevo.")
        continue 

    if 0 <= user_velocity <= 225:
        if user_velocity == 0:
            print({"sentido": "Ninguno", "velocidad": 0})
            print("El motor está detenido (0 RPM).")
        else:
            sentido_giro = input("Introduce el sentido de giro (cw/ccw): ").strip().lower()
            
            if sentido_giro not in ["cw", "ccw"]:
                print("Error: Sentido de giro no válido. Introduce 'horario' o 'antihorario'.")
                continue

            estado_motor = {"sentido": sentido_giro, "velocidad": user_velocity}
            print(estado_motor)
    else:
        print("Error: La velocidad no está en el rango (0 a 225). Intenta de nuevo.")
