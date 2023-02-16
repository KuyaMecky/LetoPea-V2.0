import sys
import time
import speech_recognition as sr
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QDialog, QProgressBar
import pyqtgraph as pg
from scipy.fft import fft
import numpy as np

class SpeechRecognitionThread(QThread):
    update_progress = pyqtSignal(int)
    win.setGeometry( 500,500)
    def __init__(self):
        super().__init__()

    def run(self):
        # Call the function that performs speech recognition
        self.recognize_speech()

    def recognize_speech(self):
        # Initialize the speech recognition engine
        r = sr.Recognizer()

        # Initialize the pyqtgraph window for the spectrogram display
        win = pg.GraphicsLayoutWidget(show=True)
        win.setWindowTitle('Spectrogram')
        p1 = win.addPlot(title='Spectrogram')
        p1.setRange(yRange=[0, 10000])
        img = pg.ImageItem()
        p1.addItem(img)
        spec_array = np.zeros((512, 512))
        img.setImage(spec_array)

        # Open the microphone and start listening for speech
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)

            # Emit signals to update the progress bar with a bouncing animation
            for i in range(100):
                if i % 10 == 0:
                    self.update_progress.emit(i)
                elif i % 10 == 5:
                    self.update_progress.emit(10 - (i % 10))
                else:
                    self.update_progress.emit(i % 10)

            stream = r.listen(source, timeout=5, phrase_time_limit=5)

            # Calculate and display the frequency spectrum in real time using pyqtgraph
            while True:
                data = stream._audio_data
                data = np.frombuffer(data, dtype=np.int16)
                if len(data) > 0:
                    spectrum = np.abs(fft(data, 512))
                    spec_array[:-1] = spec_array[1:]
                    spec_array[-1] = spectrum
                    img.setImage(spec_array)
                    QApplication.processEvents()

        # Perform speech recognition on the audio
        try:
            text = r.recognize_google(audio)
        except sr.UnknownValueError:
            text = "Speech recognition could not understand audio"
        except sr.RequestError as e:
            text = "Speech recognition service error: {0}".format(e)

        # Emit signals to update the progress bar with a bouncing animation
        for i in range(100, 0, -1):
            if i % 10 == 0:
                self.update_progress.emit(i)
            elif i % 10 == 5:
                self.update_progress.emit(10 - (i % 10))
            else:
                self.update_progress.emit(i % 10)

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Create a progress bar widget
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)

        # Create a SpeechRecognitionThread object
        self.speech_recognition_thread = SpeechRecognitionThread()
        self.speech_recognition_thread.update_progress.connect(self.update_progress_bar)

        # Start the thread
        self.speech_recognition_thread.start()

    def update_progress_bar(self, value):
        # Update the value of the progress bar
        self.progress_bar.setValue(value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec())
