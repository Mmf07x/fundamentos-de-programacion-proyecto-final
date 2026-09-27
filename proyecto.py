existe_en_inventario = False
Inventario = []
Ventas = []
while True:
  try:
    opcion = int(input(
        "\n1. Agregar producto"
        "\n2. Consultar inventario"
        "\n3. Buscar producto"
        "\n4. Reporte de bajo stock"
        "\n5. Ver ventas del dia"
        "\n6. Vender producto"
        "\n7. Ver total vendido en el dia"
        "\n8. Salir"
        "\n\nSeleccione una opcion: "))
  except ValueError:
    print("Por favor, ingrese un numero valido.")
    continue

  if opcion == 1:
      nombre = input("Ingrese el nombre del producto: ")

      if nombre == "":
        print("El nombre del producto no puede estar vacio.")
        continue

      existe_en_inventario = False
      for producto in Inventario:
        if producto["nombre"] == nombre:
          print("El producto ya existe en el inventario.")
          existe_en_inventario = True

      if existe_en_inventario:
        print("El producto ya existe en el inventario.")
        continue
    try:
      cantidad = int(input("Ingrese la cantidad del producto: "))
      if cantidad < 0:
        print("La cantidad no puede ser menor que 0.")
        continue

      precio = float(input("Ingrese el precio del producto: "))
      if precio <= 0:
        print("El precio si o si tiene que ser mayor a 0")
        continue
    except ValueError:
      print("ingrese un numero valido.")
      continue  
      Inventario.append({
        "nombre": nombre, 
        "cantidad": cantidad, 
        "precio": precio
        })
      print(f"Producto {nombre} agregado al inventario con exito. ")
      print(f"Cantidad: {cantidad}")
      print(f"Precio: {precio}")

      

    elif opcion == 2:
      if len(Inventario) == 0:
        print("El inventario esta vacio.")
      else:
          print("\n---Inventario------")
      for producto in Inventario:
        print(f"Producto: {producto['nombre']}")
        print(f"Cantidad: {producto['cantidad']}")
        print(f"Precio: {producto['precio']}")

    elif opcion == 3:
        nombre = input("Ingrese el nombre del producto a buscar: ")
        producto_encontrado = False
  
        for producto in Inventario:
            if producto["nombre"] == nombre:
                print("\nProducto encontrado:")
                print(f"Producto: {producto['nombre']}")
                print(f"Cantidad: {producto['cantidad']}")
                print(f"Precio: {producto['precio']}")
                producto_encontrado = True
        if not producto_encontrado:
            print("Producto no encontrado.")

    elif opcion == 4:
      producto_encontrado = False
      print("\n---Productos de bajo stock------")
      for producto in Inventario:
        if producto["cantidad"] <= 5:
          print(f"Producto: {producto['nombre']}")
          print(f"Cantidad: {producto['cantidad']}")
          producto_encontrado = True
      if not producto_encontrado:
        print("No hay productos de bajo stock.")

  elif opcion == 5:
    for venta in Ventas:
      print(venta)

  elif opcion == 6:
    nombre = input("Ingrese el nombre del producto a vender: ")
    cantidad = int(input("Ingrese la cantidad a vender: "))
    for producto in Inventario:
      if producto["nombre"] == nombre:
        if producto["cantidad"] >= cantidad:
          producto["cantidad"] -= cantidad
          venta = {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": producto["precio"],
            "total": cantidad * producto["precio"]
            }
          Ventas.append(venta)
          print("Venta realizada con exito.")
  elif opcion == 7:
    total_vendido = 0
    for venta in Ventas:
      total_vendido += venta["total"]
    print(f"El total vendido en el dia es: {total_vendido}")

  elif opcion == 8:
    print("Gracias por usar el sistema")
    print("Saliendo del sistema")
    break

  else:
      print("Opcion no valida")