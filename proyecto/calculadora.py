print("=== CALCULADORA BÁSICA ===")

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

print("\nSeleccione una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Ingrese una opción: ")

if opcion == "1":
    resultado = numero1 + numero2
    print("El resultado es:", resultado)

elif opcion == "2":
    resultado = numero1 - numero2
    print("El resultado es:", resultado)

elif opcion == "3":
    resultado = numero1 * numero2
    print("El resultado es:", resultado)

elif opcion == "4":
    if numero2 != 0:
        resultado = numero1 / numero2
        print("El resultado es:", resultado)
    else:
        print("No se puede dividir entre cero.")

else:
    print("Opción no válida.")
