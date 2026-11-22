def mostrar_catalogo(catalogo):
    # Muestra todos los videojuegos y sus existencias.
    print("\nCATALOGO GAMEZONE")
    for producto in catalogo:
        print(
            producto["codigo"], "|",
            producto["nombre"], "|",
            "Precio: $" + str(round(producto["precio"], 2)), "|",
            "Existencia:", producto["existencia"]
        )


def buscar_producto(catalogo, codigo):
    # Regresa el producto encontrado o None si no existe.
    codigo = codigo.upper()
    for producto in catalogo:
        if producto["codigo"].upper() == codigo:
            return producto
    return None


def hay_existencia(existencia, cantidad):
    # Valida que la cantidad sea positiva y que haya existencias suficientes.
    if cantidad <= 0:
        return False
    if cantidad <= existencia:
        return True
    return False


def calcular_importe(precio, cantidad):
    # Calcula el importe de una linea de compra.
    importe = precio * cantidad
    return round(importe, 2)


def calcular_total(subtotal, descuento=0.0, impuesto=0.16):
    # Aplica el descuento y el impuesto al subtotal.
    total = subtotal * (1 - descuento)
    total = total * (1 + impuesto)
    return round(total, 2)


def actualizar_existencia(existencia, cantidad):
    # Calcula las unidades restantes despues de una venta valida.
    nueva_existencia = existencia - cantidad
    return nueva_existencia


def main():
    # Catalogo inicial almacenado en una lista de diccionarios.
    catalogo = [
        {"codigo": "G001", "nombre": "DOOM Eternal", "precio": 699.00, "existencia": 5},
        {"codigo": "G002", "nombre": "Minecraft", "precio": 499.00, "existencia": 8},
        {"codigo": "G003", "nombre": "The Legend of Zelda: Tears of the Kingdom", "precio": 1199.00, "existencia": 3},
        {"codigo": "G004", "nombre": "Super Mario Bros. Wonder", "precio": 999.00, "existencia": 4},
        {"codigo": "G005", "nombre": "Hollow Knight", "precio": 249.00, "existencia": 10},
    ]

    carrito = []

    print("BIENVENIDO A GAMEZONE")

    while True:
        mostrar_catalogo(catalogo)
        codigo = input("\nIngrese el codigo del videojuego (SALIR para finalizar): ")

        if codigo.upper() == "SALIR":
            break

        producto = buscar_producto(catalogo=catalogo, codigo=codigo)

        if producto == None:
            print("Codigo no encontrado. Intente nuevamente.")
            continue

        cantidad = int(input("Ingrese la cantidad: "))

        existe = hay_existencia(
            existencia=producto["existencia"],
            cantidad=cantidad
        )

        if existe == False:
            if cantidad <= 0:
                print("Cantidad no valida. Debe ser mayor que cero.")
            else:
                print(
                    "No hay suficiente existencia.",
                    "Disponible:",
                    producto["existencia"],
                    "unidad(es)."
                )
            continue

        importe = calcular_importe(
            precio=producto["precio"],
            cantidad=cantidad
        )

        linea = {
            "codigo": producto["codigo"],
            "nombre": producto["nombre"],
            "cantidad": cantidad,
            "importe": importe
        }
        carrito.append(linea)

        producto["existencia"] = actualizar_existencia(
            existencia=producto["existencia"],
            cantidad=cantidad
        )

        print("Agregado al carrito:", producto["nombre"], "- $", round(importe, 2))

    if len(carrito) == 0:
        print("\nNo se agregaron productos a la compra.")
    else:
        print("\nPRODUCTOS AGREGADOS")
        for linea in carrito:
            print(
                linea["codigo"], "|",
                linea["nombre"], "|",
                "Cantidad:", linea["cantidad"], "|",
                "Importe: $", round(linea["importe"], 2)
            )

        subtotal = 0
        for linea in carrito:
            subtotal = subtotal + linea["importe"]
        subtotal = round(subtotal, 2)

        descuento = 0.0
        if subtotal >= 1000:
            descuento = 0.10

        if descuento == 0.10:
            total = calcular_total(
                subtotal=subtotal,
                descuento=0.10,
                impuesto=0.16
            )
        else:
            total = calcular_total(subtotal=subtotal)

        monto_descuento = round(subtotal * descuento, 2)
        subtotal_con_descuento = round(subtotal - monto_descuento, 2)
        monto_impuesto = round(subtotal_con_descuento * 0.16, 2)

        print("\nRESUMEN DE COMPRA")
        print("Subtotal: $", round(subtotal, 2))
        print("Descuento: $", monto_descuento)
        print("Impuesto (16%): $", monto_impuesto)
        print("TOTAL A PAGAR: $", round(total, 2))

    print("\nINVENTARIO RESTANTE")
    for producto in catalogo:
        print(
            producto["codigo"], "|",
            producto["nombre"], "|",
            "Existencia:", producto["existencia"]
        )



