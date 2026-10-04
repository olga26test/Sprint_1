new_tasks = ["task_001", "task_011", "task_007", "task_015", "task_005"]
completed_tasks = ["task_002", "task_012", "task_006"]

completed_tasks.append(new_tasks.pop(4))  # переместили task_005 в выполненные

new_tasks.remove("task_007")  # удалили task_007 из списка задач

print(new_tasks[-1])  # вывели на экран последнюю задачу из списка задач

#в задании этого нет, но тоже вывела на экран для наглядности:
print(new_tasks) 
print(completed_tasks)