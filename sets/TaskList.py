from Task import Task

class TaskList():
    def __init__(self, *args):
        self._tasks = []
        for item in args:
            self._validate_and_append(item)

    def _validate_and_append(self, item):
        if not isinstance(item, Task):
            raise TypeError("Solo se pueden añadir objetos de la clase Task a TaskList")
        self._tasks.append(item)

    def append(self, item):
        self._validate_and_append(item)

    def extend(self, iterable):
        for item in iterable:
            self._validate_and_append(item)

    def insert(self, index, item):
        self._validate_and_append(item)
        self._tasks.insert(index, item)

    def __getitem__(self, index):
        return self._tasks[index]

    def __setitem__(self, index, item):
        self._validate_and_append(item)
        self._tasks[index] = item

    def __delitem__(self, index):
        del self._tasks[index]

    def __len__(self):
        return len(self._tasks)

    def __iter__(self):
        return iter(self._tasks)

    def __contains__(self, item):
        return item in self._tasks

    def __str__(self):
        return f"TaskList([{', '.join(str(task) for task in self._tasks)}])"

    def __repr__(self):
        return f"TaskList({repr(self._tasks)})"

    def clear(self):
        self._tasks.clear()

    def index(self, item, start=0, end=None):
        return self._tasks.index(item, start, end)

    def pop(self, index=-1):
        return self._tasks.pop(index)
    
    def get_params(self):

        duration_params = {}
        required_params = {}

        for task in self._tasks:
            duration_params[task.name] = task.duration
            required_params[task.name] = task.required

        return duration_params, required_params