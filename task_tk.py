import tkinter as tk

def add_task(): #функция добавления задачи
    task = task_free.get()
    if task:
        list_todo.insert(0, task)
        task_free.delete(0, tk.END)

def del_task(): #удаление выбранной задачи
    task_status = [list_todo, list_doing, list_done]
    for task_list in task_status:
        selected_task = task_list.curselection()
        if selected_task:
            task_list.delete(selected_task)
            break

def move_task_doing():
    selected_index_todo = list_todo.curselection()
    selected_index_done = list_done.curselection()
    if selected_index_todo:
        selected_task_todo = list_todo.get(selected_index_todo)
        list_todo.delete(selected_index_todo)
        list_doing.insert(0, selected_task_todo)
    elif selected_index_done:
        selected_task_done = list_done.get(selected_index_done)
        list_done.delete(selected_index_done)
        list_doing.insert(0, selected_task_done)

def move_task_done():
    selected_index_todo = list_todo.curselection()
    selected_index_doing = list_doing.curselection()
    if selected_index_todo:
        selected_task_todo = list_todo.get(selected_index_todo)
        list_todo.delete(selected_index_todo)
        list_done.insert(0, selected_task_todo)
    elif selected_index_doing:
        selected_task_doing = list_doing.get(selected_index_doing)
        list_doing.delete(selected_index_doing)
        list_done.insert(0, selected_task_doing)

root = tk.Tk()
root.title("Мой менеджер задач")
root.config(bg="AntiqueWhite2")

label_free = tk.Label(root, text="Задача:", bg="AntiqueWhite2", font="Arial 16")
label_free.grid(row=0, column=0, sticky="ew", padx=10, pady=30)

task_free = tk.Entry(root, width=40)
task_free.grid(row=0, column=2, sticky="ew", columnspan=2, pady=30)

btn_add = tk.Button(root, text="В список дел", font="Arial 14", bg="lightblue", fg="black", command=add_task)
btn_add.grid(row=0, column=4, sticky="w")

label_todo = tk.Label(root, text="Список дел", bg="AntiqueWhite2", width=14, font="Arial 14")
label_todo.grid(row=2, column=2, sticky="ew")

list_todo = tk.Listbox(root, width=15, height=10, bg="AntiqueWhite3", bd=2, relief="sunken")
list_todo.grid(row=3, column=2, padx=25)

label_doing = tk.Label(root, text="В работе", bg="AntiqueWhite2", width=14, font="Arial 14")
label_doing.grid(row=2, column=3, sticky="ew")

list_doing = tk.Listbox(root, width=15, height=10, bg="AntiqueWhite3", bd=2, relief="sunken")
list_doing.grid(row=3, column=3, padx=25)

label_done = tk.Label(root, text="Сделано", bg="AntiqueWhite2", width=14, font="Arial 14")
label_done.grid(row=2, column=4, sticky="ew")

list_done = tk.Listbox(root, width=15, height=10, bg="AntiqueWhite3", bd=2, relief="sunken")
list_done.grid(row=3, column=4, padx=25)

btn_todo = tk.Button(root, text="В работу", bg="LightCyan2", font="Arial 14", command=move_task_doing)
btn_todo.grid(row=4, column=2, pady=20, ipadx=10, ipady=4)

btn_todo = tk.Button(root, text="Сделано", bg="LightCyan2", font="Arial 14", command=move_task_done)
btn_todo.grid(row=4, column=3, pady=30, ipadx=10, ipady=4)

btn_todo = tk.Button(root, text="Удалить", bg="LightCyan2", font="Arial 14", command=del_task)
btn_todo.grid(row=4, column=4, pady=20, ipadx=10, ipady=4)

root.mainloop()