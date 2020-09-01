# https://www.youtube.com/playlist?list=PLzMcBGfZo4-lB8MZfHPLTEHO9zJDDLpYj

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

def window():
    # Initialising app - config to? OS
    app = QApplication(sys.argv)
    # Create Window
    win = QMainWindow()
    # Set window Size/Location
    win.setGeometry(1000, 200, 300, 300)
    # Set window Title
    win.setWindowTitle("Housing Project")

    # Create a Label - where? Window
    label = QtWidgets.QLabel(win)
    # Label Content
    label.setText("My first label")
    # Move label location
    label.move(50, 50)

    # Display Window
    win.show()
    # Clean Exist
    sys.exit(app.exec_())

# Call the function
window()