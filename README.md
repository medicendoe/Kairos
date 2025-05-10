# Horario - Sistema de Optimización de Horarios

## Descripción del Proyecto

Horario es un sistema de optimización de programación de tareas que utiliza técnicas de investigación operativa para asignar tareas a bloques de tiempo específicos, considerando restricciones y maximizando la idoneidad de cada asignación según el tipo de tarea y los niveles de energía mental y física disponibles en cada bloque de tiempo.

## Tecnologías Utilizadas

- **Python 3.9**: Lenguaje principal de programación
- **Pyomo 6.4.2**: Framework de modelado para problemas de optimización
- **GLPK**: Solver de programación lineal
- **Docker**: Contenedorización para facilitar la ejecución

## Estructura del Proyecto

```
Horario/
├── sets/               # Clases del modelo de datos
├── functions/          # Lógica de optimización
├── data/               # Utilidades para carga de datos
├── in/                 # Datos de entrada (CSV)
├── out/                # Resultados de la optimización
├── docs/               # Documentación técnica detallada
├── main.py             # Punto de entrada principal
├── Dockerfile          # Configuración de Docker
├── docker-compose.yml  # Configuración de Docker Compose
└── requirements.txt    # Dependencias del proyecto
```

## Requisitos

### Para ejecución con Docker
- Docker y Docker Compose

### Para ejecución directa con Python
- Python 3.9 o superior
- Dependencias listadas en `requirements.txt`
- GLPK solver instalado en el sistema

## Ejecución

### Utilizando Docker (recomendado)

1. Asegúrate de tener Docker y Docker Compose instalados
2. Coloca tus archivos CSV de tareas y bloques en la carpeta `in/`
3. Ejecuta el siguiente comando:

```bash
docker-compose up
```

Los resultados se guardarán en la carpeta `out/`.

### Utilizando Python directamente

1. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

2. Instala el solver GLPK:
   - En Ubuntu/Debian: `sudo apt-get install glpk-utils`
   - En macOS (con Homebrew): `brew install glpk`
   - En Windows: Descarga desde http://winglpk.sourceforge.net/

3. Ejecuta el programa:

```bash
python main.py in/tasks.csv in/blocks.csv
```

## Datos de entrada

Los datos de entrada deben estar en formato CSV en la carpeta `in/`:

- `tasks.csv`: Definición de tareas con nombres, tipos, duración, requisitos y costos
- `blocks.csv`: Definición de bloques de tiempo con niveles de energía

## Documentación

Para información técnica más detallada sobre los algoritmos, modelos matemáticos y la implementación, consulta la documentación en la carpeta `docs/`.

## Licencia

Este proyecto es de código abierto y está disponible para uso educativo y personal.
