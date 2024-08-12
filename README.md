# Task-Manager-System

![image](https://github.com/user-attachments/assets/533c395a-3c27-4710-9742-3b67dabe933e)

# Project Overview

The objective of this project is to develop a suite of Python functions for a basic task manager application and provide a user menu to interact with these functions that handle various tasks such as creating, updating, deleting, and managing tasks, as well as generating reports and performing searches.

# Features

    Task Management Operations: The program supports adding, removing, updating, and retrieving tasks.
    Task Filtering: It allows users to filter tasks by priority, status (completed or pending), and deadline.
    Task Sorting: Users can sort tasks by deadline and priority.
    Task Counting: Provides counts of total tasks, completed tasks, and pending tasks.
    Task Searching: Users can search tasks by keywords in the description.
    Task Summary Generation: A summary report of tasks can be generated.
    File Operations: The task list can be saved to or loaded from a file.
    Robust Error Handling: The application includes error handling for invalid inputs and file operations.
    Console Menu: A user-friendly menu guides users through the available options.

# Function Documentation


add_task

Adds a new task to the task list.

    Parameters:
        tasks (list of dict): The current list of tasks, where each task is a dictionary with keys 'id', 'description', 'priority', 'deadline', and 'completed'.
        task (dict): The task to be added, which should contain 'id', 'description', 'priority', 'deadline', and 'completed'.

    Returns:
        list of dict: Updated list of tasks, including the newly added task.

remove_task

Removes a task by its ID.

    Parameters:
        tasks (list of dict): The current list of tasks.
        task_id (int): The ID of the task to be removed.

    Returns:
        list of dict: Updated list of tasks, excluding the removed task.

update_task

Updates an existing task with new details.

    Parameters:
        tasks (list of dict): The current list of tasks.
        task_id (int): The ID of the task to be updated.
        updated_task (dict): The updated task details. Can include new 'description', 'priority', 'deadline', and/or 'completed' status.

    Returns:
        list of dict: Updated list of tasks with the modified task.

get_task

Retrieves a task by its ID.

    Parameters:
        tasks (list of dict): The current list of tasks.
        task_id (int): The ID of the task to be retrieved.

    Returns:
        dict or None: The task with the specified ID, or None if the task is not found.

set_task_priority

Sets the priority of a task.

    Parameters:
        tasks (list of dict): The current list of tasks.
        task_id (int): The ID of the task to be updated.
        priority (str): The new priority level ('low', 'medium', 'high').

    Returns:
        list of dict: Updated list of tasks with the modified task priority.

set_task_deadline

Sets the deadline for a task.

    Parameters:
        tasks (list of dict): The current list of tasks.
        task_id (int): The ID of the task to be updated.
        deadline (str): The new deadline in 'YYYY-MM-DD' format.

    Returns:
        list of dict: Updated list of tasks with the modified task deadline.

mark_task_as_completed

Marks a task as completed.

    Parameters:
        tasks (list of dict): The current list of tasks.
        task_id (int): The ID of the task to be marked as completed.

    Returns:
        list of dict: Updated list of tasks with the task marked as completed.

set_task_description

Sets the description for a task.

    Parameters:
        tasks (list of dict): The current list of tasks.
        task_id (int): The ID of the task to be updated.
        description (str): The new description.

    Returns:
        list of dict: Updated list of tasks with the modified task description.

search_tasks_by_keyword

Searches tasks by a keyword in the description.

    Parameters:
        tasks (list of dict): The current list of tasks.
        keyword (str): The keyword to search for.

    Returns:
        list of dict: Tasks that contain the keyword in their description.

filter_tasks_by_priority

Filters tasks by priority.

    Parameters:
        tasks (list of dict): The current list of tasks.
        priority (str): The priority level to filter by.

    Returns:
        list of dict: Tasks with the specified priority.

filter_tasks_by_status

Filters tasks by their completion status.

    Parameters:
        tasks (list of dict): The current list of tasks.
        status (bool): The completion status to filter by.

    Returns:
        list of dict: Tasks with the specified completion status.

filter_tasks_by_deadline

Filters tasks by their deadline.

    Parameters:
        tasks (list of dict): The current list of tasks.
        deadline (str): The deadline to filter by.

    Returns:
        list of dict: Tasks with the specified deadline.

count_tasks

Returns the total number of tasks.

    Parameters:
        tasks (list of dict): The current list of tasks.

    Returns:
        int: The total number of tasks.

count_completed_tasks

Returns the number of completed tasks.

    Parameters:
        tasks (list of dict): The current list of tasks.

    Returns:
        int: The number of completed tasks.

count_pending_tasks

Returns the number of pending tasks.

    Parameters:
        tasks (list of dict): The current list of tasks.

    Returns:
        int: The number of pending tasks.

generate_task_summary

Generates a summary report of all tasks.

    Parameters:
        tasks (list of dict): The current list of tasks.

    Returns:
        dict: A summary report containing total, completed, and pending tasks.

save_tasks_to_file

Saves the task list to a file.

    Parameters:
        tasks (list of dict): The current list of tasks.
        file_path (str): The path to the file where tasks will be saved.

    Returns:
        None

load_tasks_from_file

Loads the task list from a file.

    Parameters:
        file_path (str): The path to the file where tasks are saved.

    Returns:
        list of dict: The loaded list of tasks.

sort_tasks_by_deadline

Sorts tasks by their deadline.

    Parameters:
        tasks (list of dict): The current list of tasks.

    Returns:
        list of dict: The sorted list of tasks by deadline.

sort_tasks_by_priority

Sorts tasks by their priority.

    Parameters:
        tasks (list of dict): The current list of tasks.

    Returns:
        list of dict: The sorted list of tasks by priority.
