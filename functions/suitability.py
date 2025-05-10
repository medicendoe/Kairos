from sets.Block import Block
from sets.Task import Task, TaskType


def S_Precalculus(task: Task, block: Block) -> float:

    if not isinstance(task, Task):
        raise TypeError("El argumento 'tarea' debe ser un objeto de la clase Task")
    if not isinstance(block, Block):
        raise TypeError("El argumento 'block' debe ser un objeto de la clase Block")

    type = task.T
    mental_demand = task.D_M_F.M
    physical_demand = task.D_M_F.F
    mental_energy = block.E_M_F.M
    physical_energy = block.E_M_F.F

    mental_suitability = 0
    physical_suitability = 0

    # Adecuación mental: alta energía es buena para alta demanda
    if mental_demand >= 4: # Tareas de alta demanda mental
        mental_suitability = mental_energy * 2 # Escala 2-10
    elif mental_demand <= 2: # Tareas de baja demanda mental
        mental_suitability = (6 - mental_energy) # Premiar energía baja/media, Escala 1-5
    else: # Demanda media
        mental_suitability = 5 # Valor constante o más complejo

    # Adecuación física: alta energía es buena para alta demanda
    if physical_demand >= 4: # Tareas de alta demanda física (Deporte)
        physical_suitability = physical_energy * 2 # Escala 2-10
    elif physical_demand <= 2: # Tareas de baja demanda física (Estudio, Trabajo)
        # Quizás preferir energía física moderada, no agotado ni hiperactivo
        physical_suitability = 5 - abs(physical_energy - 3) # Pico en 3, rango 3-5
    else: # Demanda media
        physical_suitability = 5

    # Ponderar según el tipo de tarea
    peso_mental = 0.0
    peso_fisico = 0.0

    if type == TaskType.HIGHSTUDY or type == TaskType.HIGHWORK:
        peso_mental = 0.8
        peso_fisico = 0.2
    elif type == TaskType.HIGHSPORT or type == TaskType.LOWSPORT:
        peso_mental = 0.1
        peso_fisico = 0.9
    elif type == TaskType.LOWSTUDY or type == TaskType.LOWWORK or type == TaskType.PERSONAL:
        peso_mental = 0.5 # Flexible
        peso_fisico = 0.5

    adecuacion_total = (peso_mental * mental_suitability) + (peso_fisico * physical_suitability)

    return round(adecuacion_total, 2) # Devolver un número