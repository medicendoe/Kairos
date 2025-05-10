from itertools import product

def objective(m):
    # Sumar la Adecuacion precalculada para cada tarea que inicia
    acumulated_S = lambda t, b: sum(m.S[t, b_start] for b_start in range(b, min(b + m.D[t], len(m.B))))
    return sum(m.x[t, b] * acumulated_S(t, b) for (t, b) in product(m.T, m.B))