from pyomo.environ import Constraint
# R1: Tareas obligatorias se asignan una vez
def assignment_rule(model, t):
    if model.R[t]:
        return sum(model.x[t, b] for b in model.B) == 1
    else:
        return Constraint.Skip

def no_overlap_rule(model, b):
    # Sumar 1 por cada tarea 't' que esté activa durante el slot 's'
    active_tasks_in_block = []
    for t in model.T:
        task_partial = []
        for start_b in range(max(0,b-model.D[t]), b + 1):
            task_partial.append(model.x[t, start_b])
        
        if task_partial:
            active_tasks_in_block.append(sum(task_partial))

    return sum(active_tasks_in_block) <= 1

# R3: Forzar inicio del sueño
# Asegurar que el par (tarea_sueno, sleep_start_slot) es un inicio válido
def fixed_time_tasks(model, t):
    if model.F[t]:
        return model.x[t, model.I[t]] == 1
    else:
        return Constraint.Skip


# (R4: Horizonte temporal ya se maneja al definir ValidStarts)
def horizon_rule(model, t):
    task_horizon_limit = lambda t: len(model.B) - model.D[t]
    return sum(model.x[t, start_b] for start_b in range(task_horizon_limit(t), len(model.B))) == 0