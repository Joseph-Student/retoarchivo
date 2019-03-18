from archivo import ListaArticulo


def menu():
    print("Estas son las oparaciones que se pueden realizar: ")
    print("1- Agregar articulo.")
    print("2- Listar articulos.")
    print("3- Buscar articulo.")
    print("4- Eliminar articulo.")
    print("5- Mostrar menu.")
    print("6- Salir.")


def mostrar_archivo():
    print("Bienvenido a la lista de compra.\n")
    menu()
    lista_compra = ListaArticulo(nombre='lista_compra')
    while True:
        try:
            resp = int(input("Escriba su opcion: "))
            print()
        except ValueError:
            print("Por favor introduzca un numero.")
            mostrar_archivo()
        else:
            if resp is 1:
                lista_compra.agregar_articulo(input(
                    "Nombre del articulo que desea agregar: \n").capitalize())
            elif resp is 2:
                lista_compra.ver_articulos()
            elif resp is 3:
                lista_compra.buscar_articulo()
            elif resp is 4:
                lista_compra.eliminar_articulo()
            elif resp is 5:
                menu()
                continue
            elif resp is 6:
                break
            else:
                print("Esta opcion no se encuentra disponible")


if __name__ == '__main__':
    mostrar_archivo()
    print()
    print("Gracias por usar nuestra aplicacion.")
