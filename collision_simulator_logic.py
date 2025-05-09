from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from gui import *

class CollisionSimulator(QMainWindow, Ui_CollisionSimulator):
    def __init__(self) -> None:
        """
        Sets the default instance variables and initializes input 
	fields, labels, and error labels.
        """
        super().__init__()
        self.setupUi(self)
        self.start_pushButton.clicked.connect(self.start)
        self.restart_pushButton.clicked.connect(self.restart)
        self.objects_inputs_list = [self.object_mass_input_1, self.object_mass_input_2, self.object_velocity_input_1, self.object_velocity_input_2,]
        self.mass_inputs = [self.object_mass_input_1, self.object_mass_input_2]
        self.velocity_inputs = [self.object_velocity_input_1, self.object_velocity_input_2]
        self.error_message_label_1.setStyleSheet("color: red;")
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.timer = QTimer()
        self.timer.timeout.connect(self.objects_collision_logic)
        self.object_movement_1 = 1
        self.object_movement_2 = -1

    def error_handling(self) -> bool:
        """
        Handles input validation errors by checking each input field for correctness.
        Displays specific error messages based on the type of error and clears the incorrect input
        and sets focus on the corresponding field so the user can fix the error.
        """
        self.error_message_label_1.clear()
        for i in self.objects_inputs_list:
            inputs = i.text().strip()
            if not inputs:
                self.error_message_label_1.setText("Error: Cannot leave any box empty!")
                i.clear()
                i.setFocus()
                return False
            try:
                inputs_converted = float(inputs)
                if i in self.mass_inputs and not 1 <= inputs_converted <= 100:
                    self.error_message_label_1.setText("Error: Mass must be between 1 and 100!")
                    i.clear()
                    i.setFocus()
                    return False
                if i in self.velocity_inputs and not 1 <= inputs_converted <= 20:
                    self.error_message_label_1.setText("Error: Velocity must be between 1 and 20!")
                    i.clear()
                    i.setFocus()
                    return False
            except ValueError:
                self.error_message_label_1.setText("Error: Enter numbers only!")
                i.clear()
                i.setFocus()
                return False
        return  True

    def objects_collision_logic(self) -> None:
        """
        Handles both object movement and collision logic. Objects move based on the user's entered
        velocities and masses. When a collision is detected, the velocities are updated according to
        the principles of elastic collisions, accounting for both mass and velocity.
        (This project was based on an existing project [https://www.youtube.com/watch?v=3mRvCF4qyTA&t=193s, 2:58], and the
        logic was developed with the help of web dictionaries and AI by asking key questions, such as 'How does
        QGraphicsView work?' etc.)
        """
        y1 = self.object_1.y()
        y2 = self.object_2.y()
        x1 = self.object_1.x() + self.object_velocity_1 * self.object_movement_1
        x2 = self.object_2.x() + self.object_velocity_2 * self.object_movement_2
        if x1 + self.object_1.rect().width() >= self.scene.width():
            x1 = self.scene.width() - self.object_1.rect().width()
            self.object_movement_1 *= -1
        elif x1 <= 0:
            x1 = 0
            self.object_movement_1 *= -1
        if x2 >= 0:
            x2 = 0
            self.object_movement_2 *= -1
        elif x2 + self.object_2.rect().width() >= self.scene.width():
            x2 = self.scene.width() - self.object_2.rect().width()
            self.object_movement_2 *= -1
        self.object_1.setPos(x1, y1)
        self.object_2.setPos(x2, y2)
        if self.object_1.collidesWithItem(self.object_2):
            m1 = float(self.object_mass_input_1.text().strip())
            m2 = float(self.object_mass_input_2.text().strip())
            v1 = self.object_velocity_1 * self.object_movement_1
            v2 = self.object_velocity_2 * self.object_movement_2
            new_v1 = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
            new_v2 = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
            self.object_velocity_1 = abs(new_v1)
            self.object_velocity_2 = abs(new_v2)
            self.object_movement_1 = 1 if new_v1 >= 0 else -1
            self.object_movement_2 = 1 if new_v2 >= 0 else -1

    def start(self) -> None:
        """
        Starts the simulation by checking for input errors using self.error_handling().
        If all inputs are valid, it sets up the scene and creates two square objects:
        a blue one on the left and a red one on the right, both vertically centered.
        Then it starts the animation loop at 60 FPS (1000 ms ÷ 16 ≈ 60).
        """
        if not self.error_handling():
            return
        self.scene.clear()
        view_width = self.graphicsView.viewport().width()
        view_height = self.graphicsView.viewport().height()
        self.scene.setSceneRect(0, 0, view_width, view_height)
        object_mass_1 = float(self.object_mass_input_1.text().strip())
        self.object_velocity_1 = float(self.object_velocity_input_1.text().strip())
        x_pos_object_1 = 0
        y_pos_object_1 = (view_height - object_mass_1) / 2
        self.object_1 = QGraphicsRectItem(x_pos_object_1, y_pos_object_1, object_mass_1, object_mass_1)
        self.object_1.setBrush(QBrush(QColor("blue")))
        self.scene.addItem(self.object_1)
        object_mass_2 = float(self.object_mass_input_2.text().strip())
        self.object_velocity_2 = float(self.object_velocity_input_2.text().strip())
        x_pos_object_2 = view_width - object_mass_2
        y_pos_object_2 = (view_height - object_mass_2) / 2
        self.object_2 = QGraphicsRectItem(x_pos_object_2, y_pos_object_2, object_mass_2, object_mass_2)
        self.object_2.setBrush(QBrush(QColor("red")))
        self.scene.addItem(self.object_2)
        self.timer.start(16)

    def restart(self) -> None:
        """
        Resets the window by clearing the animation, input boxes, and error label.
        Stops the QTimer and sets focus to the first velocity input, ready for new input.
        """
        for i in self.objects_inputs_list:
            i.clear()
        self.error_message_label_1.clear()
        self.scene.clear()
        self.object_velocity_input_1.setFocus()
        self.timer.stop()





