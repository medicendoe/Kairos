# R1: Tareas obligatorias se asignan una vez
def assignment_rule(model, R_t):
    return sum(model.x[R_t, b] for b in model.B) == 1

# R2: No solapamiento de tareas en cada slot
def no_overlap_rule(model, b):
    # Sumar 1 por cada tarea 't' que esté activa durante el slot 's'
    is_active = lambda t: sum(model.x[t, start_b] for start_b in range(b-model.D[t],b))
    active_tasks_in_block = sum(is_active(t) for t in model.T)
    return active_tasks_in_block <= 1

# R3: Forzar inicio del sueño
# Asegurar que el par (tarea_sueno, sleep_start_slot) es un inicio válido
def fixed_time_tasks(model, F_t):
    return sum(model.x[t, model.I[t]] for t in F_t) == len(F_t)


# (R4: Horizonte temporal ya se maneja al definir ValidStarts)
def horizon_rule(model, t):
    task_horizon_limit = lambda t: len(model.B) - model.D[t]
    return sum(model.x[t, start_b] for start_b in range(task_horizon_limit(t), len(model.B) - 1)) == 0