class Coin:
    def __init__(self, mental: int, physical: int):
        if not isinstance(mental, int) or not 1 <= mental <= 5:
            raise ValueError("El atributo 'mental' debe ser un entero entre 1 y 5")
        if not isinstance(physical, int) or not 1 <= physical <= 5:
            raise ValueError("El atributo 'physical' debe ser un entero entre 1 y 5")

        self.M = mental
        self.F = physical
        
    def __str__(self): return f"Coin(mental={self.M}, physical={self.F})"