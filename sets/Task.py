from enum import Enum, auto
from Coin import Coin

class TaskType(Enum):
    HIGHSTUDY = 0
    HIGHWORK = auto()
    HIGHSPORT = auto()
    LOWSTUDY = auto()
    LOWWORK = auto()
    LOWSPORT = auto()
    PERSONAL = auto()

class Task:
    def __init__(self, name: str,type: TaskType, duration: int, required: bool, cost: Coin, fixed: bool = False, start: int = -1):
        if not isinstance(name, str):
            raise ValueError("El atributo 'name' debe ser un string")
        if not isinstance(type, TaskType):
            raise ValueError("El atributo 'type' debe ser una instancia de TaskType")
        if not isinstance(duration, int) or duration <= 0:
            raise ValueError("El atributo 'duration' debe ser un entero positivo")
        if not isinstance(required, bool):
            raise ValueError("El atributo 'required' debe ser un booleano")
        if not isinstance(cost, Coin):
            raise ValueError("El atributo 'cost' debe ser una instancia de Coin")
        if not isinstance(fixed, bool):
            raise ValueError("El atributo 'fixed' debe ser un booleano")
        if not isinstance(fixed, int):
            raise ValueError("El atributo 'fixed' debe ser un entero")

        self.name = name
        self.T = type
        self.D = duration
        self.R = required
        self.D_M_F = cost
        self.F = fixed
        self.I = start

    def __str__(self):
        return f"Task(type={self.T.value}, duration={self.D}, required={self.R}, cost={self.D_M_F})"