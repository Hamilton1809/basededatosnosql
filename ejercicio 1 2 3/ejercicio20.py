class Vuelo:
    def __init__(self, numero_vuelo, fecha, origen, destino):
        self.numero_vuelo = numero_vuelo
        self.fecha = fecha
        self.origen = origen
        self.destino = destino
        
        self.pasajeros = [] 

    def registrar_pasajero(self, nombre):
        self.pasajeros.append(nombre)
        print(f"Pasajero '{nombre}' registrado con éxito en el vuelo {self.numero_vuelo}.")

    def listar_atributos(self):
        print(f"\n--- DETALLES DEL VUELO {self.numero_vuelo} ---")
        print(f"Fecha: {self.fecha}")
        print(f"Ruta: {self.origen} -> {self.destino}")
        print(f"Total de pasajeros: {len(self.pasajeros)}")
        print("Listado de pasajeros:")
        
       
        for i, pasajero in enumerate(self.pasajeros, 1):
            print(f"  {i}. {pasajero}")
        print("-----------------------------------")



mi_vuelo = Vuelo("XYZ-789", "29-Agosto-2026", "Popayán", "Bogotá")


print("--- REGISTRO DE PASAJEROS ---")
mi_vuelo.registrar_pasajero("Juan Pérez")
mi_vuelo.registrar_pasajero("Ana Gómez")
mi_vuelo.registrar_pasajero("Carlos Ruiz")


mi_vuelo.listar_atributos()