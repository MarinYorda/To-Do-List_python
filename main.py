# This is a simple To-Do-List program

import tkinter
import tkinter.messagebox
import pickle

# Creating a window to hold the list
root = tkinter.Tk()
root.title("To-Do Simple List")


# Functions to support the list
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")


def delete_task():
    #gets the index of the item you wish to delete
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Please select a task you wish to delete.")


def load_task():
    try:
        tasks = pickle.load(open("Tasks.data", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="There are no tasks to load.")


def save_task():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("Tasks.data", "wb"))


# Creating GUI
frame_tasks= tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=8, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Creating space for user to enter information
entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

# Creating different functionalities
# Add tasks
button_add_task = tkinter.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

# Delete tasks
button_delete_task = tkinter.Button(root, text="Delete Task", width=48, command=delete_task)
button_delete_task.pack()

# Load tasks
button_load_task = tkinter.Button(root, text="Load tasks", width=48, command=load_task)
button_load_task.pack()

# Save Tasks
button_save_task = tkinter.Button(root, text="Save Tasks", width=48, command=save_task)
button_save_task.pack()

root.mainloop()
if __name__ == '__main__':


