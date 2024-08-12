
import json
from datetime import datetime


def add_task(tasks, task):
    """
    Adds a new task to the task list.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task (dict): The task to be added.

    Returns:
    list of dict: Updated list of tasks.
    """
    if not isinstance(task, dict):
        raise ValueError("Task must be a dictionary.")

    required_keys = {'id', 'description', 'priority', 'deadline', 'completed'}
    if not required_keys.issubset(task.keys()):
        raise KeyError(f"Task must contain keys: {required_keys}")

    tasks.append(task)
    return tasks


def remove_task(tasks, task_id):
    """
    Removes a task by its ID.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be removed.

    Returns:
    list of dict: Updated list of tasks.
    """
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            del tasks[i]
            return tasks
    raise ValueError("Task with given ID not found.")


def update_task(tasks, task_id, updated_task):
    """
    Updates an existing task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    updated_task (dict): The updated task details.

    Returns:
    list of dict: Updated list of tasks.
    """
    for task in tasks:
        if task['id'] == task_id:
            task.update(updated_task)
            return tasks
    raise ValueError("Task with given ID not found.")


def get_task(tasks, task_id):
    """
    Retrieves a task by its ID.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be retrieved.

    Returns:
    dict: The task with the specified ID, or None if not found.
    """
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None


def set_task_priority(tasks, task_id, priority):
    """
    Sets the priority of a task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    priority (str): The new priority level.

    Returns:
    list of dict: Updated list of tasks.
    """
    valid_priorities = ['low', 'medium', 'high']
    if priority not in valid_priorities:
        raise ValueError(f"Priority must be one of {valid_priorities}")

    for task in tasks:
        if task['id'] == task_id:
            task['priority'] = priority
            return tasks
    raise ValueError("Task with given ID not found.")


def set_task_deadline(tasks, task_id, deadline):
    """
    Sets the deadline for a task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    deadline (str): The new deadline.

    Returns:
    list of dict: Updated list of tasks.
    """
    try:
        datetime.strptime(deadline, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Deadline must be in 'YYYY-MM-DD' format.")

    for task in tasks:
        if task['id'] == task_id:
            task['deadline'] = deadline
            return tasks
    raise ValueError("Task with given ID not found.")


def mark_task_as_completed(tasks, task_id):
    """
    Marks a task as completed.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be marked as completed.

    Returns:
    list of dict: Updated list of tasks.
    """
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            return tasks
    raise ValueError("Task with given ID not found.")


def set_task_description(tasks, task_id, description):
    """
    Sets the description for a task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    description (str): The new description.

    Returns:
    list of dict: Updated list of tasks.
    """
    if not isinstance(description, str):
        raise ValueError("Description must be a string.")

    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            return tasks
    raise ValueError("Task with given ID not found.")


def search_tasks_by_keyword(tasks, keyword):
    """
    Searches tasks by a keyword in the description.

    Parameters:
    tasks (list of dict): The current list of tasks.
    keyword (str): The keyword to search for.

    Returns:
    list of dict: Tasks that contain the keyword in their description.
    """
    if not isinstance(keyword, str):
        raise ValueError("Keyword must be a string.")

    return [task for task in tasks if keyword.lower() in task['description'].lower()]


def filter_tasks_by_priority(tasks, priority):
    """
    Filters tasks by priority.

    Parameters:
    tasks (list of dict): The current list of tasks.
    priority (str): The priority level to filter by.

    Returns:
    list of dict: Tasks with the specified priority.
    """
    valid_priorities = ['low', 'medium', 'high']
    if priority not in valid_priorities:
        raise ValueError(f"Priority must be one of {valid_priorities}")

    return [task for task in tasks if task['priority'] == priority]


def filter_tasks_by_status(tasks, status):
    """
    Filters tasks by their completion status.

    Parameters:
    tasks (list of dict): The current list of tasks.
    status (bool): The completion status to filter by.

    Returns:
    list of dict: Tasks with the specified completion status.
    """
    if not isinstance(status, bool):
        raise ValueError("Status must be a boolean value.")

    return [task for task in tasks if task['completed'] == status]


def filter_tasks_by_deadline(tasks, deadline):
    """
    Filters tasks by their deadline.

    Parameters:
    tasks (list of dict): The current list of tasks.
    deadline (str): The deadline to filter by.

    Returns:
    list of dict: Tasks with the specified deadline.
    """
    try:
        datetime.strptime(deadline, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Deadline must be in 'YYYY-MM-DD' format.")

    return [task for task in tasks if task['deadline'] == deadline]


def count_tasks(tasks):
    """
    Returns the total number of tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    int: The total number of tasks.
    """
    return len(tasks)


def count_completed_tasks(tasks):
    """
    Returns the number of completed tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    int: The number of completed tasks.
    """
    return sum(task['completed'] for task in tasks)


def count_pending_tasks(tasks):
    """
    Returns the number of pending tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    int: The number of pending tasks.
    """
    return len(tasks) - count_completed_tasks(tasks)


def generate_task_summary(tasks):
    """
    Generates a summary report of all tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    dict: A summary report containing total, completed, and pending tasks.
    """
    return {
        'total_tasks': count_tasks(tasks),
        'completed_tasks': count_completed_tasks(tasks),
        'pending_tasks': count_pending_tasks(tasks)
    }


def save_tasks_to_file(tasks, file_path):
    """
    Saves the task list to a file.

    Parameters:
    tasks (list of dict): The current list of tasks.
    file_path (str): The path to the file where tasks will be saved.

    Returns:
    None
    """
    if not isinstance(file_path, str):
        raise ValueError("File path must be a string.")

    with open(file_path, 'w') as file:
        json.dump(tasks, file)


def load_tasks_from_file(file_path):
    """
    Loads the task list from a file.

    Parameters:
    file_path (str): The path to the file where tasks are saved.

    Returns:
    list of dict: The loaded list of tasks.
    """
    if not isinstance(file_path, str):
        raise ValueError("File path must be a string.")

    with open(file_path, 'r') as file:
        return json.load(file)


def sort_tasks_by_deadline(tasks):
    """
    Sorts tasks by their deadline.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    list of dict: The sorted list of tasks.
    """
    return sorted(tasks, key=lambda task: datetime.strptime(task['deadline'], '%Y-%m-%d'))


def sort_tasks_by_priority(tasks):
    """
    Sorts tasks by their priority.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    list of dict: The sorted list of tasks.
    """
    priority_order = {'low': 0, 'medium': 1, 'high': 2}
    return sorted(tasks, key=lambda task: priority_order[task['priority']])


def user_menu():
    """
    Displays a menu for user interaction with the task manager.

    Returns:
    None
    """
    tasks = []
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. View Task")
        print("5. Set Task Priority")
        print("6. Set Task Deadline")
        print("7. Mark Task as Completed")
        print("8. Set Task Description")
        print("9. Search Tasks by Keyword")
        print("10. Filter Tasks by Priority")
        print("11. Filter Tasks by Status")
        print("12. Filter Tasks by Deadline")
        print("13. Count Tasks")
        print("14. Count Completed Tasks")
        print("15. Count Pending Tasks")
        print("16. Generate Task Summary")
        print("17. Save Tasks to File")
        print("18. Load Tasks from File")
        print("19. Sort Tasks by Deadline")
        print("20. Sort Tasks by Priority")
        print("21. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                task = {
                    'id': int(input("Enter task ID: ")),
                    'description': input("Enter description: "),
                    'priority': input("Enter priority (low, medium, high): "),
                    'deadline': input("Enter deadline (YYYY-MM-DD): "),
                    'completed': False
                }
                tasks = add_task(tasks, task)
                print("Task added.")

            elif choice == '2':
                task_id = int(input("Enter task ID to remove: "))
                tasks = remove_task(tasks, task_id)
                print("Task removed.")

            elif choice == '3':
                task_id = int(input("Enter task ID to update: "))
                updated_task = {
                    'description': input("Enter new description: "),
                    'priority': input("Enter new priority (low, medium, high): "),
                    'deadline': input("Enter new deadline (YYYY-MM-DD): ")
                }
                tasks = update_task(tasks, task_id, updated_task)
                print("Task updated.")

            elif choice == '4':
                task_id = int(input("Enter task ID to view: "))
                task = get_task(tasks, task_id)
                if task:
                    print(task)
                else:
                    print("Task not found.")

            elif choice == '5':
                task_id = int(input("Enter task ID to set priority: "))
                priority = input("Enter new priority (low, medium, high): ")
                tasks = set_task_priority(tasks, task_id, priority)
                print("Priority updated.")

            elif choice == '6':
                task_id = int(input("Enter task ID to set deadline: "))
                deadline = input("Enter new deadline (YYYY-MM-DD): ")
                tasks = set_task_deadline(tasks, task_id, deadline)
                print("Deadline updated.")

            elif choice == '7':
                task_id = int(input("Enter task ID to mark as completed: "))
                tasks = mark_task_as_completed(tasks, task_id)
                print("Task marked as completed.")

            elif choice == '8':
                task_id = int(input("Enter task ID to set description: "))
                description = input("Enter new description: ")
                tasks = set_task_description(tasks, task_id, description)
                print("Description updated.")

            elif choice == '9':
                keyword = input("Enter keyword to search: ")
                result = search_tasks_by_keyword(tasks, keyword)
                print("Tasks containing keyword:")
                for task in result:
                    print(task)

            elif choice == '10':
                priority = input("Enter priority to filter (low, medium, high): ")
                result = filter_tasks_by_priority(tasks, priority)
                print(f"Tasks with priority {priority}:")
                for task in result:
                    print(task)

            elif choice == '11':
                status = input("Enter status to filter (completed, pending): ").lower() == 'completed'
                result = filter_tasks_by_status(tasks, status)
                status_str = "completed" if status else "pending"
                print(f"Tasks that are {status_str}:")
                for task in result:
                    print(task)

            elif choice == '12':
                deadline = input("Enter deadline to filter (YYYY-MM-DD): ")
                result = filter_tasks_by_deadline(tasks, deadline)
                print(f"Tasks with deadline {deadline}:")
                for task in result:
                    print(task)

            elif choice == '13':
                total_tasks = count_tasks(tasks)
                print(f"Total tasks: {total_tasks}")

            elif choice == '14':
                completed_tasks = count_completed_tasks(tasks)
                print(f"Completed tasks: {completed_tasks}")

            elif choice == '15':
                pending_tasks = count_pending_tasks(tasks)
                print(f"Pending tasks: {pending_tasks}")

            elif choice == '16':
                summary = generate_task_summary(tasks)
                print("Task Summary:")
                print(f"Total tasks: {summary['total_tasks']}")
                print(f"Completed tasks: {summary['completed_tasks']}")
                print(f"Pending tasks: {summary['pending_tasks']}")

            elif choice == '17':
                file_path = input("Enter file path to save tasks: ")
                save_tasks_to_file(tasks, file_path)
                print("Tasks saved to file.")

            elif choice == '18':
                file_path = input("Enter file path to load tasks: ")
                tasks = load_tasks_from_file(file_path)
                print("Tasks loaded from file.")

            elif choice == '19':
                tasks = sort_tasks_by_deadline(tasks)
                print("Tasks sorted by deadline.")

            elif choice == '20':
                tasks = sort_tasks_by_priority(tasks)
                print("Tasks sorted by priority.")

            elif choice == '21':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 21.")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    user_menu()
