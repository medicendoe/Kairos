from csv import DictReader
from ..sets import Task, TaskList, Coin

def task_load(csv_path: str) -> TaskList:
    """
    Load tasks from a CSV file into a TaskList.

    Args:
        csv_path (str): The path to the CSV file containing task data.

    Returns:
        TaskList: A TaskList object containing the loaded tasks.
    """
    task_list = TaskList()
    with open(csv_path, 'r') as csv_file:
        reader = DictReader(csv_file)
        for row in reader:
            task = Task(
                name=row['name'],
                type=row['type'],
                duration=int(row['duration']),
                required=row['required'].lower() == 'true',
                cost=Coin(
                    mental=int(row['costo mental']),
                    physical=int(row['costo fisico'])
                ),
                fixed=row['fixed'].lower() == 'true',
                start=int(row['start'])
            )
            task_list.append(task)
    return task_list