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
        nombre=input('Ingrese el nombre del producto: '),
        precio=float(input('Ingrese el precio del producto: '))
    )

    if resultado:
        print('Producto agregado exitosamente!')

elif opcion == 3:
    id = input('Ingrese el ID del producto: ')
    producto = productoCRUD.existe(id)
    if producto:
        nombre = input(f'Ingrese el nuevo nombre ({producto[1]}): ')
        precio = input(f'Ingrese el nuevo precio ({producto[2]}): ')

        if len(nombre) == 0:
            nombre = producto[1]
        if len(precio) == 0:
            precio = producto[2]

        resultado = productoCRUD.actualizar(id, nombre, precio)
        if resultado:
            print('Producto actualizado exitosamente!')
    else:
        print('El ID del producto no existe')
elif opcion == 4:
    id = input('Ingrese el ID del producto: ')
    resultado = productoCRUD.eliminar(id)
    if resultado:
        print('Producto eliminado exitosamente!')
elif opcion == 5:
    id = input('Ingrese el ID del producto: ')
    producto = productoCRUD.existe(id)
    if producto:
        print(f'Id: {producto[0]}\nNombre: {producto[1]}\nPrecio: {producto[2]}')
    else:
        print('El ID del producto no existe')
elif opcion == 0:
    break

else:
    print('Opción incorrecta')
