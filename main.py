import argparse
import os
import csv
from datetime import datetime
from pyomo.environ import ConcreteModel, Var, Objective, Constraint, NonNegativeIntegers, Binary, SolverFactory, Set, Param, NonNegativeReals, maximize
from itertools import product
from data.taskLoad import task_load
from data.blockLoad import block_load
from functions.suitability import S_Precalculus
from functions.restrictions import assignment_rule, no_overlap_rule, fixed_time_tasks, horizon_rule
from functions.objective import objective

def run_model(task_csv, block_csv):
    # Load data
    task_list = task_load(task_csv)
    block_list = block_load(block_csv)

    # Create model
    model = ConcreteModel()

    name, D, R, F, I = task_list.get_params()
    blocks, ids = block_list.get_params()
    S = {}
    
    for (t, b) in product(task_list, block_list):
        S[(t.name, b.id)] = S_Precalculus(t, b)
        
    # Creating the sets
    model.T = Set(initialize=name)
    model.B = Set(initialize=ids)

    # Creating the parameters
    model.D = Param(model.T, initialize=D, within=NonNegativeIntegers)  # Task durations
    model.R = Param(model.T, initialize=R, within=Binary)  # Required tasks
    model.F = Param(model.T, initialize=F, within=Binary)  # Fixed start times
    model.I = Param(model.T, initialize=I, within=NonNegativeIntegers)  # Fixed start times
    model.S = Param(model.T, model.B, initialize=S, within=NonNegativeReals)  # Suitability

    # Creating the variables
    model.x = Var(model.T, model.B, domain=Binary)  # Task assignment

    # Creating Constraints
    model.assingment = Constraint(model.T, rule=assignment_rule)
    model.no_overlap = Constraint(model.B, rule=no_overlap_rule)
    model.fixed_time = Constraint(model.T, rule=fixed_time_tasks)
    model.horizon = Constraint(model.T, rule=horizon_rule)

    # Creating the objective function
    model.obj = Objective(rule=objective, sense=maximize)  # Maximize suitability

    # Ensure out directory exists
    os.makedirs('out', exist_ok=True)

    # Generate timestamp for filenames
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    lp_filename = f"out/model_{timestamp}.lp"
    results_filename = f"out/results_{timestamp}.csv"

    model.write(lp_filename, io_options={'symbolic_solver_labels': True})

    solver = SolverFactory('glpk')
    result = solver.solve(model, tee=True)
    result.write()

    # Output results
    if result.solver.status == 'ok' and result.solver.termination_condition == 'optimal':
        print("Optimal solution found!")
        
        # Write results to CSV file
        with open(results_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Task', 'Block', 'Duration', 'Suitability'])
            
            # Store assignments for sorting
            assignments = []
            for t in model.T:
                for b in model.B:
                    if model.x[t, b].value == 1:
                        assignments.append((t, b, model.D[t], model.S[t, b]))
                        print(f"Task {t} assigned to Block {b}")
            
            # Sort by block/time and write to CSV
            for t, b, duration, suitability in sorted(assignments, key=lambda x: x[1]):
                writer.writerow([t, b, duration, suitability])
        
        print(f"Results exported to {results_filename}")
        print(f"LP model exported to {lp_filename}")
    else:
        print("No optimal solution found.")

# Example usage
if __name__ == "__main__":
    # Configurar argparse para leer argumentos desde la terminal
    parser = argparse.ArgumentParser(description="Run the scheduling optimization model.")
    parser.add_argument("task_csv", type=str, help="Path to the tasks CSV file.")
    parser.add_argument("block_csv", type=str, help="Path to the blocks CSV file.")
    args = parser.parse_args()

    # Pasar los argumentos a la función run_model
    run_model(args.task_csv, args.block_csv)