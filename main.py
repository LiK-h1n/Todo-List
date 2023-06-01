from streamlit import title, checkbox, text_input, session_state, experimental_rerun, text, expander, subheader, \
    write, form, form_submit_button
from functions import get_tasks, add_task, update_tasks, get_date, set_date
from datetime import datetime

FILEPATH_1 = "incomplete_tasks.txt"
FILEPATH_2 = "complete_tasks.txt"
FILEPATH_3 = "daily_tasks.txt"


def add_task_():
    task = session_state["new task"]
    incomplete_tasks.append(task)
    add_task(task, FILEPATH_1)


def add_daily_task():
    task = session_state["new task"]
    add_task(task, FILEPATH_3)


incomplete_tasks = get_tasks(FILEPATH_1)
stored_date, did_exist = get_date()
if stored_date < datetime.now().date() or not did_exist:
    update_tasks([], FILEPATH_2)
    daily_tasks = get_tasks(FILEPATH_3)
    for daily_task in daily_tasks:
        if daily_task not in incomplete_tasks:
            add_task(daily_task, FILEPATH_1)
    incomplete_tasks = get_tasks(FILEPATH_1)
    set_date()
complete_tasks = get_tasks(FILEPATH_2)


title("To-do List App")
subheader("")
with expander("Incomplete Tasks", True):
    for index, task in enumerate(incomplete_tasks):
        check_box = checkbox(task, key=index)
        if check_box:
            completed_task = incomplete_tasks.pop(index)
            update_tasks(incomplete_tasks, FILEPATH_1)
            add_task(completed_task, FILEPATH_2)
            del session_state[index]
            experimental_rerun()
write("")
with expander("Completed Tasks"):
    for task in complete_tasks:
        text(task)
write("")


with form("My form", clear_on_submit=True):
    text_input("new task name", placeholder="Add a new task",
               key="new task",
               label_visibility="hidden")
    daily_task = checkbox("Daily Task", key="daily task")
    add_button = form_submit_button("Add", on_click=add_task_)
if daily_task:
    add_daily_task()
