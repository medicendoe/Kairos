from sets.Coin import Coin

class Block:
    def __init__(self, id: int, energy: Coin):
        if not isinstance(energy, Coin):
            raise TypeError("El atributo 'energy' debe ser un objeto de la clase Coin")
        if not isinstance(id, int) or id < 0:
            raise ValueError("El atributo 'id' debe ser un entero positivo (incluyendo 0)")
        self.E_M_F = energy
        self.id = id

    def __lt__(self, other):
        if isinstance(other, Block):
            return self.id < other.id
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Block):
            return self.id == other.id
        return NotImplemented
        
    def __str__(self):
        return f"Block(energy={self.E_M_F}, id={self.id})"