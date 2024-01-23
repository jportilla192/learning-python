def calculator(num1, num2, opcion):
    if opcion == 1:
        return num1 + num2
    elif opcion == 2:
        return num1 - num2
    elif opcion == 3:
        return num1 * num2
    elif opcion == 4:
        if num2 == 0:
            print('No se puede dividir entre 0')
        else:
            return num1 / num2
    elif opcion == 5:
        print('Gracias por usar la calculadora')
    else:
        print('Opcion invalida')
    opcion = menu()



def menu():
    print('Bienvenido a la calculadora')
    print('Ingrese dos numeros')
    num1 = float(input('Ingrese el primer numero: '))
    num2 = float(input('Ingrese el segundo numero: '))
    print('1. Sumar')
    print('2. Restar')
    print('3. Multiplicar')
    print('4. Dividir')
    print('5. Salir')
    opcion = int(input('Ingrese una opcion: '))
    print("El resultado de la operacion es: ", calculator(num1, num2, opcion))


menu()