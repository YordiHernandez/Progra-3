from arbol import Arbol

arbol = Arbol(10)
arbol.agregar(11)
arbol.agregar(12)
arbol.agregar(13)
arbol.agregar(14)
arbol.agregar(15)
arbol.agregar(9)
arbol.agregar(8)
arbol.agregar(7)
arbol.agregar(6)
arbol.preorden()
arbol.inorden()
arbol.postorden()

opc = input("Quiere buscar un numero (s/n): ")

if opc == 's':
    busqueda = int(input("Ingresa un número para buscar en el árbol: "))
    n = arbol.buscar(busqueda)
    if n is None:
        print(busqueda," no esta en el arbol")
    else:
        print(busqueda," si esta en el arbol")
elif opc == 'n':
    print("Finalizando busqueda")
else:
    print("Porfavor ingrese 's' o 'n'")