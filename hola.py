print("---CALCULADORA MEJORADA---")

print("Hola, elija la opcion")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. Division")
print("5. Modulo")
print("6. Exponente")

salir: bool = False
error = False

while not salir:

    seleccion = int(input("Teclee una numero y pulse Enter:\n"))


    match seleccion:
        case 1:
            print("Ha elegido la opcion suma")
        case 2:
            print("Ha elegido la opcion resta")
        case 3:
            print("Ha elegido la opcion multiplicacion")
        case 4:
            print("Ha elegido la opcion division")
        case 5:
            print("Ha elegido la opcion modulo")
        case 6:
            print("Ha elegido la opcion exponente")
        case 7:
            print("Salir")
            break
        case _:
            print("Opcion invalida")
            error = True

    if not error:
        numero1 = float(input("ingrese numero1: "))
        numero2 = float(input("ingrese numero2: "))

        match seleccion:
            case 1:
                resultado = round(numero1 + numero2, 2)
                print(f"La SUMA de {numero1} + {numero2} = {resultado}")
            case 2:
                resultado = round(numero1 - numero2, 2)
                print(f"La RESTA de {numero1} - {numero2} = {resultado}")
            case 3:
                resultado = round(numero1 * numero2, 2)
                print(f"La MULTIPLICACION de {numero1} * {numero2} = {resultado}")
            case 4:
                resultado = round(numero1 / numero2, 2)
                print(f"La DIVISION de {numero1} / {numero2} = {resultado}")
            case 5:
                resultado = round(numero1 % numero2, 2)
                print(f"El MODULO de {numero1} % {numero2} = {resultado}")
            case 6:
                resultado = round(numero1 ** numero2, 2)
                print(f"El EXPONENTE de {numero1} ** {numero2} = {resultado}")
