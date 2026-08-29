from datetime import datetime

cuentas = {}
consecutivo = 1

while True:
    print("\nMENÚ BANCO ADSO 3229426")
    print("1. Crear Cuenta\n2. Consignar Cuenta\n3. Retirar Cuenta\n4. Consultar Cuenta Por Código")
    print("5. Consultar Cuenta por Identificación Cliente\n6. Listar Cuentas\n7. Salir")
    opcion = input("Ingrese Opción (1-7): ")

    if opcion == '1':
        anio = datetime.now().year
        codigo = f"{anio}-{consecutivo}"
        consecutivo += 1
        identificacion = input("Identificación: ")
        nombre = input("Nombre completo: ")
        correo = input("Correo electrónico: ")
        
        cuentas[codigo] = {
            "identificacion": identificacion, "nombre": nombre, "correo": correo,
            "fecha_creacion": datetime.now().strftime("%Y-%m-%d"), "saldo": 0.0
        }
        print(f"Cuenta creada exitosamente. Su código es: {codigo}")

    elif opcion == '2':
        codigo = input("Ingrese el código de la cuenta: ")
        if codigo in cuentas:
            monto = float(input("Valor a consignar: "))
            cuentas[codigo]["saldo"] += monto
            print("Consignación exitosa.")
        else: print("Cuenta no encontrada.")

    elif opcion == '3':
        codigo = input("Ingrese el código de la cuenta: ")
        if codigo in cuentas:
            monto = float(input("Valor a retirar: "))
            if cuentas[codigo]["saldo"] >= monto:
                cuentas[codigo]["saldo"] -= monto
                print("Retiro exitoso.")
            else: print("Saldo insuficiente.")
        else: print("Cuenta no encontrada.")

    elif opcion == '4':
        codigo = input("Ingrese el código de la cuenta: ")
        if codigo in cuentas: print(cuentas[codigo])
        else: print("Cuenta no encontrada.")

    elif opcion == '5':
        ident = input("Ingrese la identificación: ")
        encontradas = {cod: datos for cod, datos in cuentas.items() if datos["identificacion"] == ident}
        if encontradas:
            for c, d in encontradas.items(): print(f"Código: {c}, Datos: {d}")
        else: print("No se encontraron cuentas para esa identificación.")

    elif opcion == '6':
        for c, d in cuentas.items(): print(f"Código: {c}, Datos: {d}")

    elif opcion == '7':
        print("Saliendo del sistema.")
        break
    else:
        print("Opción inválida.")