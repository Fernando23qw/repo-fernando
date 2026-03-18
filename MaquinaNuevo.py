#def = Palabra clave utilizada para definir o crear funciones personalizadas.
#Ejemplo:
def maquina():
    print("¡Bienvenido a la máquina expendedora!")
def saludo(nombre2):    #aqui recibe el argumento que le pasamos al llamar a la función, en este caso "amigo"
    print(f"Hola {nombre2}!")   
    print("Bienvenido al comedor.")
while True:
    contrseña = int(input("Por favor, la contraseña para entrar al comedor: "))
    if contrseña == 12345:
        print("Contraseña correcta. Ahora ingresa tu nombre para saludarte.")
        break
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")

nombre = input("Por favor, ingresa tu nombre: ")
saludo(nombre)  #aqui se ejecuta la función saludo, y se muestra el mensaje en pantalla.

print("tenemos una maqueina expendedora, por favor elige una bebida")
print("[1]COCA COLA")       
print("[2]FANTA")
print("[3]PEPSI")
print("[4]SPRITE")
print("[5]NESTEA")
numero  = int (input("Ingrese el número de la bebida que desea comprar: "))
match numero:
        case 1:
            print("Has elegido COCA COLA")
            print("El precio de la COCA COLA es de 10 euros")  
            
        case 2: 
            print("Has elegido FANTA")
            print("El precio de la FANTA es de 10 euros")   
            
        case 3: 
            print("Has elegido PEPSI")
            print("El precio de la PEPSI es de 10 euros")
            
        case 4:
            print("Has elegido SPRITE")
            print("El precio de la SPRITE es de 10 euros")
            
        case 5:
            print("Has elegido NESTEA")
            print("El precio de la NESTEA es de 10 euros")
            
        case _:
            print("Opción no válida, por favor elija una bebida del menú.")
while True:
      bebida1 = input("Ingrese el dinero para comprar la bebida (10 euros): ")
      if bebida1 == "10 euros":
        print("¡Compra exitosa! Disfruta tu bebida.")
        break  
      else:
        print("Cantidad incorrecta. Por favor, ingrese exactamente 10 euros.")
