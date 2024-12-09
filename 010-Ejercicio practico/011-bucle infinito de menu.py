"""
    Tienda de ropa
    (c) 2024 Jose Vicente Carratalá
"""
# Condiciones iniciales

productos = []

# Mensaje de bienvenida

print("######## Bienvenidos ########")
print("#### A la tienda de ropa ####")
print("# de Jose Vicente Carratalá #")
print("")

# Menú principal
while True:
    print("Menú:")
    print("1.-Insertar un producto")
    print("2.-Listar productos")
    print("3.-Actualizar un producto")
    print("4.-Eliminar un producto")
    print("")

    # Selección de opción

    opcion = input("Selecciona una opción(1-4):")
    print(f"Has escogido la opcion: {opcion}")

    # Comportamiento condicional

    if opcion == "1":
        print("Vamos a insertar un registro")
        nombre = input("Nombre:")
        descripcion = input("Descripcion:")
        precio = input("Precio:")
        productos.append(
                {
                    "nombre":nombre,
                    "descripcion":descripcion,
                    "precio":precio
                }
            )
    elif opcion == "2":
        print("Vamos a listar los registros")
    elif opcion == "3":
        print("Vamos a actualizar un registro")
    elif opcion == "4":
        print("Vamos a eliminar un registro")






