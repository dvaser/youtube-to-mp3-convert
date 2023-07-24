import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QListWidget, QWidget
from PyQt6.QtCore import QThread
from mp3_convert_ui import Ui_MainWindow
from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtGui import QIcon
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
import ssl
import sys

class ConvertThread(QThread):
    def __init__(self, video_urls, textbar):
        super().__init__()
        self.video_urls = video_urls
        self.textbar = textbar

    def run(self):
        # Müzik klasörünü oluştur
        music_folder = os.path.join(os.path.dirname(sys.argv[0]), "music")
        os.makedirs(music_folder, exist_ok=True)

        for url in self.video_urls:
            self.convert_to_mp3(url, music_folder)

    def convert_to_mp3(self, video_url, music_folder):
        try:
            # Youtube videosunu çeker
            yt = YouTube(video_url)
            title = yt.title

            # Videoyu en yüksek kalitede indirir
            audio_stream = yt.streams.get_audio_only()

            # Dosyayı indir
            audio_stream.download(output_path=music_folder, filename=f"{title}.mp3")

            def convert_message(text):
                self.textbar.setText(text)  # QLineEdit'ın içine mesajı yerleştir

            # İndirilen video dosyasının yolunu ayarlar
            audio_path = music_folder + audio_stream.default_filename
            
            print(audio_path)

            convert_message(text=f"MP3 dosyası '{title}.mp3' başarıyla oluşturuldu!")

        except Exception as e:
            print(f"Error: {str(e)}")

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.listMusic = []

        # Uygulama penceresinin arka plan rengini değiştirin
        self.setStyleSheet("background-color: lightgray;")  # İstediğiniz arka plan rengini buraya yazın
        # QLineEdit'in arka plan rengini beyaz yapın
        self.lineEdit.setStyleSheet("background-color: white;")
        # QListView'in arka plan rengini gri yapın
        self.listView.setStyleSheet("background-color: white;")
        # QPushButton'un arka plan rengini mavi yapın
        self.pushButton.setStyleSheet("background-color: white;")
        self.pushButton_2.setStyleSheet("background-color: white;")
        self.pushButton_3.setStyleSheet("background-color: white;")

        # Uygulama penceresinin boyutunu sınırlayın
        self.setMaximumSize(640, 421)  # Pencere en fazla 800x600 boyutunda olacak

        # Favicon'u ayarlayın
        self.set_favicon()

        self.pushButton.clicked.connect(self.add_url)
        self.pushButton_3.clicked.connect(self.delete_selected_urls)
        self.pushButton_2.clicked.connect(self.convert)

        self.model = QtGui.QStandardItemModel()
        self.listView.setModel(self.model)

        self.lineEdit_2.setDisabled(True)  # QLineEdit'ı devre dışı bırak

    def add_url(self):
        url = self.lineEdit.text()
        if url:
            try:
                # Bypass SSL certificate verification (sometimes required on Windows)
                ssl._create_default_https_context = ssl._create_default_https_context if hasattr(ssl, '_create_default_https_context') else ssl._create_default_https_context

                # Get video title using pytube
                yt = YouTube(url)
                title = yt.title
            except Exception as e:
                title = 'Untitled'

            item = QtGui.QStandardItem(url)
            item.setData(title, QtCore.Qt.ItemDataRole.DisplayRole)
            self.model.appendRow(item)
            self.listMusic.append(url)

    def delete_selected_urls(self):
        selected_indexes = self.listView.selectedIndexes()
        for index in selected_indexes:
            self.model.removeRow(index.row())
            self.listMusic.pop(index.row())

    def convert(self):
        if self.model.rowCount() > 0:
            self.convert_started()
            video_urls = self.listMusic
            self.convert_thread = ConvertThread(video_urls, self.lineEdit_2)
            self.convert_thread.finished.connect(self.convert_finished)
            self.convert_thread.start()

    def convert_started(self):
        self.lineEdit_2.setText("Dönüştürme işlemi başlatılıyor...")  # QLineEdit'ın içine mesajı yerleştir
        self.lineEdit_2.setStyleSheet("background-color: lightblue; color: black;")

    def convert_finished(self):
        self.lineEdit_2.setText("İşlem bitti.")  # QLineEdit'ın içine mesajı yerleştir
        self.lineEdit_2.setStyleSheet("background-color: lightgreen; color: black;")

    def set_favicon(self):
        # Favicon dosyanızın yolu ve adı
        favicon_path = "favicon.ico"  # favicon.ico dosyanızın yolu
        # Favicon dosyasını kontrol edin
        if os.path.exists(favicon_path):
            app_icon = QIcon(favicon_path)
            self.setWindowIcon(app_icon)
        else:
            print("Favicon dosyası bulunamadı!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())
