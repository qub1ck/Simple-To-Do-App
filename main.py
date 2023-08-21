if __name__ == '__main__':
    import functions as f
    import interface as i

    app = f.widgets.QApplication(f.sys.argv)
    main_window = i.MainWindow()
    main_window.show()

    f.sys.exit(app.exec())