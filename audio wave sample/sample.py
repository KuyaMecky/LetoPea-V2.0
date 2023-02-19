import sys
import speech_recognition as sr
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

class SpeechRecognizer(QThread):
    recognized = pyqtSignal(str)

    def run(self):
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            recognized_text = recognizer.recognize_google(audio)
            self.recognized.emit(recognized_text)
        except sr.UnknownValueError:
            self.recognized.emit("Could not understand audio")
        except sr.RequestError as e:
            self.recognized.emit(f"Could not request results from Google Speech Recognition service; {e}")

class WaveWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.width = 500
        self.height = 100
        self.pen = QPen(QColor(255, 0, 0))
        self.samples = [0] * self.width

    def update_samples(self, samples):
        self.samples = samples

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(self.pen)

        y_offset = self.height / 2
        x_offset = 0
        for sample in self.samples:
            y = y_offset + (sample * self.height / 2)
            qp.drawLine(int(x_offset), int(y_offset), int(x_offset), int(y))
            x_offset += 1

        qp.end()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Speech Recognition Example")
        self.resize(600, 200)

        self.label = QLabel("Say something...")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.wave_widget = WaveWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.wave_widget)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        self.recognizer = SpeechRecognizer()
        self.recognizer.recognized.connect(self.recognized)

    def start_listening(self):
        self.recognizer.start()
        self.wave_widget.update_samples([0] * self.wave_widget.width)

    def recognized(self, text):
        self.label.setText(text)

    def update_wave(self, samples):
        self.wave_widget.update_samples(samples)
        self.wave_widget.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.start_listening()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
