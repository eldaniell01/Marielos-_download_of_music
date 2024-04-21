import sys
import youtube_dl
import os
from pytube import YouTube
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QPropertyAnimation, QRect, QEasingCurve, QByteArray


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main = uic.loadUi('views/home.ui')
        self.main.show()
        pixmap = QPixmap('images/mari.png')
        pixmap2 = QPixmap('images/flor.png')
        self.main.label_2.setPixmap(pixmap)
        self.main.label.setPixmap(pixmap2)
        self.main.btnDownload.clicked.connect(self.downloadMusic)
        
    def downloadMusic(self):
        yt = YouTube(self.main.textUrl.text())
        stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
        nombre_archivo = stream.default_filename.replace('.mp4', '.mp3')
        ruta_completa = os.path.join('Downloads', nombre_archivo)
        stream.download(output_path='Downloads')
        os.rename(os.path.join('Downloads', stream.default_filename), ruta_completa)
        return ruta_completa