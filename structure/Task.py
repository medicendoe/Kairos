from enum import Enum, auto

class TaskType(Enum):
    HIGHSTUDY = 0
    HIGHWORK = auto()
    HIGHSPORT = auto()
    LOWSTUDY = auto()
    LOWWORK = auto()
    LOWSPORT = auto()
    PERSONAL = auto()

class Task:
    def __init__(self, name: str,type: TaskType, duration: int, required: bool, cost: Coin):
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

        self.name = name
        self.type = type
        self.duration = duration
        self.required = required
        self.cost = cost

    def __str__(self):
        return f"Task(type={self.type.value}, duration={self.duration}, required={self.required}, cost={self.cost})"