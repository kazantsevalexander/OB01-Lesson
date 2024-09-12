import tkinter as tk

# Списки задач (Python-списки для хранения объектов Task)
tasks_incomplete = []
tasks_complete = []

class Task():
    def __init__(self, description, data, status=False):
        self.description = description
        self.data = data
        self.status = status

    def __str__(self):
        return f"Задача: {self.description}. Дата: {self.data}"

    def newTask(self):
        tasks_incomplete.append(self)

    def makeTask(self):
        self.status = True
        tasks_complete.append(self)
        tasks_incomplete.remove(self)

def add_task():
    task_new = task_free.get()
    data_new = task_data_free.get()

    if task_new and data_new:  # Проверяем, что поля не пустые
        task = Task(task_new, data_new)
        task.newTask()

        # Добавляем задачу в Listbox для отображения
        listbox_incomplete.insert(0, str(task))

        # Очищаем поля ввода
        task_free.delete(0, tk.END)
        task_data_free.delete(0, tk.END)

def move_task_doing():
    selected_index = listbox_incomplete.curselection()
    if selected_index:  # Проверяем, что что-то выбрано
        # Получаем индекс выбранной задачи
        index = selected_index[0]
        task = tasks_incomplete[index]

        # Перемещаем задачу в выполненные
        task.makeTask()

        # Обновляем виджеты Listbox
        listbox_incomplete.delete(index)
        listbox_complete.insert(0, str(task))

root = tk.Tk()
root.title("Мой менеджер задач")
root.config(bg="AntiqueWhite2")
root.geometry("1000x600")

label_free = tk.Label(root, text="Задача:", bg="AntiqueWhite2", font="Arial 16")
label_free.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

label_data_free = tk.Label(root, text="Дата:", bg="AntiqueWhite2", font="Arial 16")
label_data_free.grid(row=1, column=0, sticky="ew", padx=10, pady=0)

task_free = tk.Entry(root, width=80)
task_free.grid(row=0, column=2, sticky="ew", columnspan=2, pady=0)

task_data_free = tk.Entry(root, width=40)
task_data_free.grid(row=1, column=2, sticky="ew", columnspan=2, pady=0)

# Кнопка для добавления задачи
btn_add = tk.Button(root, text="В список дел", font="Arial 14", bg="lightblue", fg="black", height=2, command=add_task)
btn_add.grid(row=0, column=4, rowspan=2, sticky="ns")

# Метка для невыполненных задач
label_todo = tk.Label(root, text="Список дел", bg="AntiqueWhite2", width=14, font="Arial 14")
label_todo.grid(row=2, column=2, sticky="ew")

# Listbox для невыполненных задач
listbox_incomplete = tk.Listbox(root, width=35, height=20, bg="AntiqueWhite3", bd=2, relief="sunken")
listbox_incomplete.grid(row=3, column=2, padx=25)

# Метка для выполненных задач
label_done = tk.Label(root, text="Сделано", bg="AntiqueWhite2", width=14, font="Arial 14")
label_done.grid(row=2, column=3, sticky="ew")

# Listbox для выполненных задач
listbox_complete = tk.Listbox(root, width=35, height=20, bg="AntiqueWhite3", bd=2, relief="sunken")
listbox_complete.grid(row=3, column=3, padx=25)

# Кнопка для перемещения задач в "В работе"
btn_move = tk.Button(root, text="Выполнить", bg="LightCyan2", font="Arial 14", command=move_task_doing)
btn_move.grid(row=4, column=2, pady=20, ipadx=10, ipady=4)

root.mainloop()
