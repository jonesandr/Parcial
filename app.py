from sqlite3 import apilevel
from modelo import ProductoCRUD
from unittest import result

productoCRUD = ProductoCRUD()

while True:
    print('....INVENTARIO....')
    print('1. Agregar')
    print('2. visualizar')
    print('3. Actualizar')
    print('4. Eliminar')
    print('5. Buscar')
    print('0. Salir')
    opcion = int(input('Opcion: '))

    if opcion == 2:
        productos = productoCRUD.mostrar()
        if len(productos) == 0:
            print('No hay productos')
        else:
            for i in productos:
                print('-' * 30)
                print(f'Id: {i[0]}\nNombre: {i[1]}\nPrecio: {i[2]}')

    elif opcion == 1:
        resultado = productoCRUD.agregar(
            nombre=input('Ingresar producto: '),
            precio=float(input('Ingresar precio: '))
        )

        if resultado:
            print('Producto agregado!')

    elif opcion == 3:
        id = input('Ingrese el id del producto: ')
        producto = productoCRUD.existe(id)
        if producto:
            nombre = input(f'Ingrese el nuevo nombre({producto[1]}): ')
            precio = input(f'Igrese el nuevo precio({producto[2]}): ')

            if len(nombre) == 0:
                nombre = producto[1]
            if len(precio) == 0:
                precio = producto[2]

            resultado = productoCRUD.actualizar(id, nombre, precio)
            if resultado:
                print('Producto actualizado')
        else:
            print('El id del producto no existe')
    elif opcion == 4:
        id = input('Ingresar id del producto: ')
        resultado = productoCRUD.eliminar(id)
        if resultado:
            print('Producto eliminado!')
    elif opcion == 5:
        id = input('Ingresar id del producto: ')
        producto = productoCRUD.existe(id)
        if producto:
            print(f'Id: {producto[0]}\nNombre: {producto[1]}\nPrecio: {producto[2]}')
        else:
            print('El id del producto no existe')
    elif opcion == 0:
        break

    else:
        print('Opcion incorrecta')