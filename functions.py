import sys
from PyQt6 import QtWidgets as widgets, QtCore as core, QtGui as gui


def showDate():
    current_date = core.QDate.currentDate()
    date = current_date.toString("dddd dd, MMMM yyyy")
    return date


def showTime():
    current_time = core.QTime.currentTime()
    time = current_time.toString("hh:mm:ss")
    return time


def showList():
    temp = open("tasks.txt", 'r')
    if len(temp.read()) > 1:
        temp.close()
        with open("tasks.txt", 'r') as f:
            file = f.read()
            f.close()
            file = file.split('\n')

            tasks = []
            for item in file:
                tasks.append(item)
            tasks.remove('')

            return tasks
    else:
        f = open("tasks.txt", 'a')
        f.close()
        tasks = ["No tasks!"]

        return tasks


def add(new_text):
    file = showList()
    if "No tasks!" in file:
        f = open("tasks.txt", 'w')
    else:
        f = open("tasks.txt", 'a')

    f.write(f"{new_text}\n")
    f.close()


def edit(selected_item):
    global ind
    edited_text, ok = widgets.QInputDialog.getText(None, "Edit Item", "Enter new text:",
                                                   text=selected_item)

    temp = showList()
    print(temp)
    for item in showList():
        if item == selected_item:
            ind = temp.index(item)
    temp[ind] = edited_text

    f = open("tasks.txt", 'w')
    for item in temp:
        f.write(f"{item}\n")

    return edited_text, ok


def remove(selected_item):
    task_list = showList()
    task_list.reverse()

    task_list.remove(selected_item)
    task_list.reverse()

    f = open("tasks.txt", 'w')
    for item in task_list:
        f.write(f"{item}\n")
