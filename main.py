import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the user interface from the .ui file
        loader = QUiLoader()
        ui_file = QFile("IHM.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file)
        ui_file.close()

        # Set up the user interface
        self.setCentralWidget(self.ui.centralwidget)
        self.ui.pushButton.clicked.connect(self.handle_button_click)

    def handle_button_click(self):
        print("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())