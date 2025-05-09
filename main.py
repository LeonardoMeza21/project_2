from PyQt6.QtWidgets import QApplication
from collision_simulator_logic import CollisionSimulator


def main():
    application = QApplication([])
    window = CollisionSimulator()
    window.show()
    application.exec()

if __name__ == '__main__':
    main()