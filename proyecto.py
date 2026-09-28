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
    print("Error, tiene que ingresar un numero entero.")
    continue
    

  if opcion == 1:
      nombre = input("Ingrese el nombre del producto: ")      

      if nombre == "":
        print("El nombre del producto no puede estar vacio.")
        continue

      existe_en_inventario = False
      for producto in Inventario:
        if producto["nombre"] == nombre:
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
          print("Ingrese un numero valido.")
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
      print("No hay nada en el inventario.")
    else:
      print("\n---Inventario------")
      for producto in Inventario:
        print(f"Producto: {producto['nombre']}")
        print(f"Cantidad: {producto['cantidad']}")
        print(f"Precio: {producto['precio']}")
        print("--------------------")

 

      


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
        print("--------------------")
        producto_encontrado = True
    if not producto_encontrado:
      print("No hay productos de bajo stock.")

  elif opcion == 5:
    if len(Ventas) == 0:

      print("No han habido ventas en el dia.")

    else:
      print("\n---Ventas del dia------")

      for venta in Ventas:
        print(f"Producto: {venta['nombre']}")
        print(f"Cantidad: {venta['cantidad']}")
        print(f"Total: {venta['total']}")

  elif opcion == 6:
      
    nombre = input("Ingrese el nombre del producto a vender: ")
      
    try:
      cantidad = int(input("Ingrese la cantidad a vender: "))

      if cantidad <= 0:

        print("La cantidad a vender debe ser mayor a 0.")
        continue

    except ValueError:
        print("Error, la cantidad tiene que ser un numero entero.")
        continue
    
    existe_en_inventario = False

    for producto in Inventario:

      if producto["nombre"] == nombre:

        existe_en_inventario = True

        if producto["cantidad"] >= cantidad:

          producto["cantidad"] -= cantidad

          total = cantidad * producto["precio"]

          venta = {
            "nombre": producto["nombre"],
            "cantidad": cantidad,
            "precio": producto["precio"],
            "total": total
          }

          Ventas.append(venta)
          print("Venta realizada con exito.")
          print(f"Producto: {producto["nombre"]}")
          print(f"Cantidad: {cantidad}")
          print(f"Precio original: ${producto["precio"]}")
          print(f"Total de la venta: ${total}")

        else:
          print("No hay suficiente stock para realizar la venta.")
        
    if not existe_en_inventario:
      print("El producto no existe en el inventario.")

  elif opcion == 7:
    total_vendido = 0
  
    for venta in Ventas:
      total_vendido += venta["total"]
    print(f"/nEl total vendido en el dia es: ${total_vendido}")

  elif opcion == 8:
    print("Gracias por usar el sistema")
    print("Saliendo del sistema")
    break

  else:
    print("Opcion no valida tiene que ser del 1 al 8")