from django.shortcuts import render


class Todo:
    def __init__(self, num_task, created_date, deadline, owner):
        self.num_task = num_task
        self.created_date = created_date
        self.deadline = deadline
        self.owner = owner


list_todos = [
    Todo('Task 1', '10/09/2018', '12/09/2018', 'admin'),
    Todo('Task 2', '10/09/2018', '12/09/2018', 'admin'),
    Todo('Task 3', '10/09/2018', '12/09/2018', 'admin'),
    Todo('Task 4', '10/09/2018', '12/09/2018', 'admin'),
    Todo('Task 5', '10/09/2018', '12/09/2018', 'admin')
]

completed_list_todos = [
    Todo('Task 0', '10/09/2018', '12/09/2018', 'admin'),
]


def todo_list(request):
    context = {
        'todos': list_todos,
    }
    return render(request, 'todo_list.html', context=context)


def completed_todo_list(request):
    context = {
        'todos': completed_list_todos,
    }
    return render(request, 'completed_todo_list.html', context=context)

