from os import SEEK_END, path
from datetime import datetime

DATEPATH = "date.txt"


def get_date():
    """
    Gets the stored date from txt file
    """
    date_exists = True
    try:
        if path.getsize(DATEPATH) == 0:
            date_exists = False
            set_date()
        with open(DATEPATH) as file:
            date_str = file.read().strip()
        return (datetime.strptime(date_str, "%Y-%m-%d").date(), date_exists)
    except FileNotFoundError:
        date_exists = False
        set_date()
        with open(DATEPATH) as file:
            date_str = file.read().strip()
        return (datetime.strptime(date_str, "%Y-%m-%d").date(), date_exists)


def set_date():
    """
    Sets the current date in txt file
    """
    with open(DATEPATH, "w") as file:
        file.write(f"{datetime.now().date()}")


def get_tasks(filepath):
    """
    Read a text file and returns the list of tasks
    """
    try:
        with open(filepath) as file:
            tasks = file.readlines()
        return tasks
    except FileNotFoundError:
        with open(filepath, "w+") as file:
            tasks = file.readlines()
        return tasks


def add_task(task, filepath):
    """
    Adds a task to the text file which contains all tasks
    """
    with open(filepath, "a") as file:
        file.seek(0, SEEK_END)
        file.writelines(task.strip() + "\n")


def update_tasks(tasks, filepath):
    """
    Updates new tasks into the text file
    """
    with open(filepath, "w") as file:
        file.writelines(tasks)
