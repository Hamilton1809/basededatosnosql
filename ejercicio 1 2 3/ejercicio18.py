class Carro:
    def __init__(self, placa, marca, modelo, color):
        self.__placa = placa
        self.marca = marca
        self.__modelo = modelo
        self.color = color

    def getplaca(self):
        return self.__placa

    def getmodelo(self):
        return self.__modelo

    def setplaca(self, placa):
        self.__placa = placa

    def setmodelo(self, modelo):
        self.__modelo = modelo

class Libro:
    def __init__(self, titulo, autor, numeroPaginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__numeroPaginas = numeroPaginas

    def gettitulo(self): return self.__titulo
    def getautor(self): return self.__autor
    def getnumeroPaginas(self): return self.__numeroPaginas

    def settitulo(self, titulo): self.__titulo = titulo
    def setautor(self, autor): self.__autor = autor
    def setnumeroPaginas(self, numeroPaginas): self.__numeroPaginas = numeroPaginas


mi_carro = Carro("ABC-123", "Toyota", 2026, "Rojo")
mi_libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", 417)



mi_carro = Carro("ABC-123", "Toyota", 2026, "Rojo")
mi_libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", 417)



print("=== DATOS DEL CARRO ===")

print("Placa:", mi_carro.getplaca())
print("Modelo:", mi_carro.getmodelo())

print("Marca:", mi_carro.marca)
print("Color:", mi_carro.color)

print("\n=== DATOS DEL LIBRO ===")

print("Título:", mi_libro.gettitulo())
print("Autor:", mi_libro.getautor())
print("Páginas:", mi_libro.getnumeroPaginas())