from csv import DictReader
from sets.Task import Task, TaskType
from sets.TaskList import TaskList
from sets.Coin import Coin

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
                type=TaskType(int(row['type'])),
                duration=int(row['duration']),
                required=row['required'].lower() == '1',
                cost=Coin(
                    mental=int(row['costo mental']),
                    physical=int(row['costo fisico'])
                ),
                fixed=row['fixed'].lower() == '1',
                start=int(row['start'])
            )
            task_list.append(task)
    return task_list