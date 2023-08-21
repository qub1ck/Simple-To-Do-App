import functions as f


class MainWindow(f.widgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = f.widgets.QVBoxLayout()
        self.setWindowTitle("To-Do App")
        self.setFixedSize(300, 500)

        self.setup_window()

        self.setLayout(self.layout)

    def setup_window(self):
        self.time_date()
        self.task_list()
        self.show_list()
        self.buttons()

    def time_date(self):
        self.date_label = f.widgets.QLabel()
        self.time_label = f.widgets.QLabel()

        self.layout.addWidget(self.date_label, alignment=f.core.Qt.AlignmentFlag.AlignTop.AlignHCenter)
        self.layout.addWidget(self.time_label, alignment=f.core.Qt.AlignmentFlag.AlignTop.AlignHCenter)

        timer_dt = f.core.QTimer(self)
        timer_dt.timeout.connect(self.update_date_time)
        timer_dt.start(1000)

        self.update_date_time()

    def update_date_time(self):
        self.date_label.setText(f.showDate())
        self.time_label.setText(f.showTime())

    def task_list(self):
        self.tasks_list = f.widgets.QListWidget()

        self.input_field = f.widgets.QLineEdit()
        self.input_field.setPlaceholderText("Type-in new task")

        self.layout.addWidget(self.tasks_list)
        self.layout.addWidget(self.input_field)

    def show_list(self):
        task_list = f.showList()
        self.tasks_list.clear()
        for item in task_list:
            item = f.widgets.QListWidgetItem(item)
            item.setTextAlignment(f.core.Qt.AlignmentFlag.AlignCenter)  # Align item text horizontally centered
            self.tasks_list.addItem(item)

    def buttons(self):
        self.add_button = f.widgets.QPushButton("Add")
        self.edit_button = f.widgets.QPushButton("Edit")
        self.remove_button = f.widgets.QPushButton("Remove")

        b_layout = f.widgets.QHBoxLayout()

        b_layout.addWidget(self.add_button)
        b_layout.addWidget(self.edit_button)
        b_layout.addWidget(self.remove_button)

        self.add_button.clicked.connect(self.add_button_action)
        self.add_button.clicked.connect(self.show_list)
        self.edit_button.clicked.connect(self.edit_button_action)
        self.edit_button.clicked.connect(self.show_list)
        self.remove_button.clicked.connect(self.remove_button_action)
        self.remove_button.clicked.connect(self.show_list)

        self.layout.addLayout(b_layout)

    def add_button_action(self):
        new_item = self.input_field.text()
        if new_item:
            f.add(new_item)
            self.tasks_list.addItem(new_item)
            self.input_field.clear()

    def edit_button_action(self):
        selected_item = self.tasks_list.currentItem()
        if selected_item:
            edited_text, ok = f.edit(selected_item.text())
            if ok:
                selected_item.setText(edited_text)

    def remove_button_action(self):
        selected_item = self.tasks_list.currentItem()
        if selected_item:
            row = self.tasks_list.row(selected_item)
            self.tasks_list.takeItem(row)
            f.remove(selected_item.text())