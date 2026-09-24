Inventario = []
Ventas = []
while True:
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
  if opcion == 1:
      nombre = input("Ingrese el nombre del producto: ")
      cantidad = int(input("Ingrese la cantidad del producto: "))
      precio = float(input("Ingrese el precio del producto: "))
      Inventario.append({"nombre": nombre, "cantidad": cantidad, "precio": precio})

  elif opcion == 2:
    for producto in Inventario:
      print(producto)

  elif opcion == 3:
    nombre = input("Ingrese el nombre del producto a buscar: ")
    for producto in Inventario:
       if producto["nombre"] == nombre:
        print(producto)

  elif opcion == 4:
    for producto in Inventario:
      if producto["cantidad"] < 10:
        print(producto)

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