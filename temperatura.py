
def menu():
    loop = "True"
    while loop == "True":

        print("""Hola buenos días
            Acabas de entrar a la aplicación para convertir grados ya sea de farenheit a celsius o viseversa
            Para poder empezar necesitas elejir una opcion, esta la vas a elejir por medio de numeros dependiendo de que sea lo que quieres hacer
            1. Farenheit a Celsuis
            2. Celsius a Farenheit
            3. Cerrar el programa
            
    """)
        
        opcion=int(input("¿Qué opción quieres elejir?: "))

        if opcion == 1:
            print("""Elejiste la opcion de Farenheit a Celsius
En el caso de esta conversion tiene ciertos limites, el minimo es de -459.67° y maximo de 212°""")
            far=int(input("Ingresa la temperatura en grados Farenheit: "))
            if -456.67 <= far <= 212:
                conv = (far-32) * 5/9
                print(str(far) + " grados Farenheit son " + str(conv) + " en grados celsuis.\n")
            else:
                print("Este dato entra en el rango de no validos\n")

        elif opcion == 2:
            print("""Elejiste la opcion de Celsuis a Farenheit
En el caso de esta conversion teine ciertos limites, el minimos es de -273.15° y maximo de 100°""")
            cel = int(input("Ingrese la cantidad en grados Celsius: "))
            if -273.15 <= cel <= 100:
                conv = (cel * 9/5) + 32
                print(str(cel) + " grados Celsius son " + str(conv) + " grados Farenheit\n")
            else:
                print("Este dato entra en el rango de los no validos\n")

        elif opcion == 3:
            print("Gracias por usar este programa \n")
            loop = "False"
        
        else:
            print("Ingrese una opcion valida")




menu()
