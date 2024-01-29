import os
import helpers

def start():

    while True:
        helpers.clean_screen() 

        print('''
        =======================================
            Bienvenido al Gestor de Clientes
        =======================================
        1. [1] Listar Clientes
        2. [2] Busca Cliente
        3. [3] Anadir Cliente
        4. [4] Modificar Cliente
        5. [5] Borrar Cliente
        0. [0] Exit
        =======================================    
        ''')

        option = input("Introduce una opcion: ")

        helpers.clean_screen()

        if option == "1":
            print("Listar Clientes")        
        elif option == "2":
            print("Buscar Cliente")
        elif option == "3":
            print("Anadir Cliente")
        elif option == "4":
            print("Modificar Cliente")
        elif option == "5":
            print("Borrar Cliente")
        elif option == "0":
            input("\nPulsa una tecla para continuar...")
            break
        else:
            print("Opcion no valida")
            
            continue

        input("\nPulsa una tecla para continuar...")



