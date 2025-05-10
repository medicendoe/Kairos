from sets.Block import Block
from sets.Task import Task, TaskType


def S_Precaulus(task: Task, block: Block) -> float:

    if not isinstance(task, Task):
        raise TypeError("El argumento 'tarea' debe ser un objeto de la clase Task")
    if not isinstance(block, Block):
        raise TypeError("El argumento 'block' debe ser un objeto de la clase Block")

    type = task.type
    mental_demand = task.cost.mental
    physical_demand = task.cost.physical
    mental_energy = block.energy.mental
    fisica_energy = block.energy.physical

    mental_suitability = 0
    physical_suitability = 0

    # Adecuación mental: alta energía es buena para alta demanda
    if mental_demand >= 4: # Tareas de alta demanda mental
        mental_suitability = energia_mental * 2 # Escala 2-10
    elif mental_demand <= 2: # Tareas de baja demanda mental
        mental_suitability = (6 - energia_mental) # Premiar energía baja/media, Escala 1-5
    else: # Demanda media
        mental_suitability = 5 # Valor constante o más complejo

    # Adecuación física: alta energía es buena para alta demanda
    if physical_demand >= 4: # Tareas de alta demanda física (Deporte)
        physical_suitability = energia_fisica * 2 # Escala 2-10
    elif physical_demand <= 2: # Tareas de baja demanda física (Estudio, Trabajo)
        # Quizás preferir energía física moderada, no agotado ni hiperactivo
        physical_suitability = 5 - abs(energia_fisica - 3) # Pico en 3, rango 3-5
    else: # Demanda media
        physical_suitability = 5

    # Ponderar según el tipo de tarea
    peso_mental = 0.0
    peso_fisico = 0.0

    if tipo == TaskType.HIGHSTUDY or tipo == TaskType.HIGHWORK:
        peso_mental = 0.8
        peso_fisico = 0.2
    elif tipo == TaskType.HIGHSPORT or tipo == TaskType.LOWSPORT:
        peso_mental = 0.1
        peso_fisico = 0.9
    elif tipo == TaskType.LOWSTUDY or tipo == TaskType.LOWWORK or tipo == TaskType.PERSONAL:
        peso_mental = 0.5 # Flexible
        peso_fisico = 0.5

    adecuacion_total = (peso_mental * mental_suitability) + (peso_fisico * physical_suitability)

    return round(adecuacion_total, 2) # Devolver un número