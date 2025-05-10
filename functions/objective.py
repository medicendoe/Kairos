from itertools import product

def objective(m):
    # Sumar la Adecuacion precalculada para cada tarea que inicia
    return sum(m.x[t, b] * m.S[t, b] for (t, b) in product(m.T, m.B))