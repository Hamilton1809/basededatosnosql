
from pez import Pez
from perro import Perro
from gato import Gato


mi_pez = Pez(0.5)
mi_perro = Perro(12.5)
mi_gato = Gato(4.0)


print("--- Acciones individuales ---")
mi_pez.nadar()
mi_perro.ladrar()
mi_gato.maullar()

print("\n--- Acción heredada (Respirar) ---")
mi_pez.respirar()
mi_perro.respirar()
mi_gato.respirar()