import pymysql as mysql

# Configuración de variables de conexión
user = 'root'
password = 'root'
baseDatos = 'tienda_adso'
host = 'localhost'

# Establecer conexión y cursor
miconexion = mysql.connect(host=host, user=user, database=baseDatos, password=password)
cursor = miconexion.cursor()

def agregar():
    try:
        producto = ("15", "tv", 25000, "electrodomesticos")
        
        consulta = """
            INSERT INTO productos (procodigo, pronombre, proprecio, procategoria) 
            VALUES (%s, %s, %s, %s)
        """
        
        cursor.execute(consulta, producto)
        miconexion.commit()
        
        if cursor.rowcount == 1:
            print("Producto agregado correctamente")
            
    except mysql.Error as e:
        print(f"Error al agregar el producto: {e}")

def agregar_varios():
    try:
        productos = [
            ("21", "nevera", 12000.00, "electrodomesticos"),
            ("22", "lavadora", 9500.00, "electrodomesticos"),
            ("23", "audifonos", 8000.00, "tecnologia"),
            ("24", "camara", 3000.00, "tecnologia")
        ]
        
        consulta = """
            INSERT INTO productos (procodigo, pronombre, proprecio, procategoria) 
            VALUES (%s, %s, %s, %s)
        """
        
        cursor.executemany(consulta, productos)
        miconexion.commit()
        
        print(f"Se agregaron {cursor.rowcount} productos correctamente.")
        
    except mysql.Error as e:
        miconexion.rollback()
        print(f"Error al agregar varios productos: {e}")

def listar():
    try:
        consulta = "SELECT * FROM productos"
        cursor.execute(consulta)
        productos = cursor.fetchall()
        
        for producto in productos:
            print(f"id: {producto[0]}")
            print(f"codigo: {producto[1]}")
            print(f"nombre: {producto[2]}")
            print(f"precio: {producto[3]}")
            print(f"categoria: {producto[4]}")
            print("-" * 20)
                    
    except mysql.Error as e:
        print(f"Error al listar productos: {e}")

def consultarporcodigo():
    try:
        codigo = input("Ingrese el código de producto a buscar: ")
        codigoaconsultar = (codigo,)
        
        consulta = "SELECT * FROM productos WHERE procodigo=%s"
        cursor.execute(consulta, codigoaconsultar)
        producto = cursor.fetchone()
        
        if producto:
            print("\nProducto encontrado:")
            print(f"ID: {producto[0]} | Código: {producto[1]} | Nombre: {producto[2]} | Precio: {producto[3]} | Categoría: {producto[4]}")
        else:
            print("No existe ese producto")
            
    except mysql.Error as e:
        print(f"Error al consultar: {e}")

# --- NUEVA FUNCIÓN AÑADIDA AQUÍ ---
def consultarporcategoria():
    try:
        categoria = input("Ingrese la categoría a buscar: ")
        categoriaaconsultar = (categoria,)
        
        consulta = "SELECT * FROM productos WHERE procategoria=%s"
        cursor.execute(consulta, categoriaaconsultar)
        productos = cursor.fetchall()
        
        if productos:
            print(f"\n--- Productos en la categoría '{categoria}' ---")
            for producto in productos:
                print(f"ID: {producto[0]} | Código: {producto[1]} | Nombre: {producto[2]} | Precio: {producto[3]}")
            print("-" * 20)
        else:
            print("No se encontraron productos en esa categoría")
            
    except mysql.Error as e:
        print(f"Error al consultar por categoría: {e}")
# -----------------------------------

def actualizar():
    try:
        datosactualizar = ("televisor", 1)
        
        consulta = "UPDATE productos SET pronombre=%s WHERE idproducto=%s"
        cursor.execute(consulta, datosactualizar)
        miconexion.commit()
        
        if cursor.rowcount == 1:
            print("Producto actualizado correctamente")
        else:
            print("No existe el producto con esa ID")
            
    except mysql.Error as e:
        miconexion.rollback()
        print(f"Error al actualizar: {e}")

def eliminar():
    try:
        productoeliminar = (3,)
        
        consulta = "DELETE FROM productos WHERE idproducto=%s"
        cursor.execute(consulta, productoeliminar)
        miconexion.commit()
        
        if cursor.rowcount == 1:
            print("Producto eliminado correctamente")
        else:
            print("No existe un producto con esa ID para eliminar")
            
    except mysql.Error as e:
        miconexion.rollback()
        print(f"Error al eliminar: {e}")

# Ejemplo de uso
# Nota: Si agregar_varios() te da error de duplicados, ponle un # al inicio para comentarla
agregar_varios()
listar()
consultarporcategoria()