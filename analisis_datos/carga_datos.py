

import random


def generar_lista_compras():
    canasta_básica = {
      'Arroz' : 1800,
        'Azúcar' : 2200,
        'Harina' : 1200,
        'Tomate' : 2500,
        'Frijoles' : 1400,
        'Papas' : 3000,
        'Lecha': 1000,
        'Cerveza' : 1000,
        'Cafe' : 5000,
        'Fideos': 800,
        'Jabón' : 1500,
        'Huevos' : 3500,
        'Naranjas' : 2500,
        'Sal': 800  
    }
    #Aquí voy a seleccionar aleatoriamente 5 productos de la canasta básica
    selección = random.sample(list(canasta_básica.items()),k=6)
    return selección    