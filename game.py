import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ClickerGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Накликай котиков')
        self.setGeometry(100, 100, 300, 400)

        self.click_count = 0
        self.image_index = 1
 
        self.image_folder = 'images'

        self.images = [os.path.join(self.image_folder, f'image_{i}.png') for i in range(1, 6)]

        if not os.path.exists(self.image_folder):
            print(f'Папка с котами "{self.image_folder}" не найдена.')
            sys.exit()

        self.layout = QVBoxLayout()

        self.label = QLabel(f'Кликай на кота, чтобы посмотреть следующего. Кликов уже: {self.click_count}', self)
        self.layout.addWidget(self.label)

        self.image_label = QLabel(self)
        self.pixmap = QPixmap(self.images[0])
        self.image_label.setPixmap(self.pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label)

        self.setLayout(self.layout)

        self.image_label.mousePressEvent = self.on_click

    def on_click(self, event):
        self.click_count += 1
        self.label.setText(f'Кликай на кота, чтобы посмотреть следующего. Кликов уже: {self.click_count}')

        if self.click_count % 50 == 0 and self.image_index < len(self.images):
            self.change_image()

    def change_image(self):
        self.pixmap = QPixmap(self.images[self.image_index])
        self.image_label.setPixmap(self.pixmap)
        self.image_index += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClickerGame()
    window.show()
    sys.exit(app.exec_())