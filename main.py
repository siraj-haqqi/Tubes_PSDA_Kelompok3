import keyword
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTableWidgetItem, QMessageBox
)
from PySide6.QtCore import Qt
from main_ui import Ui_MainWindow       
from TubesKel3 import DoublyLinkedList  


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.playlist = DoublyLinkedList()
        self.current_index = 0  

        self.ui.btnInsertLagu.clicked.connect(self.insert_lagu)
        self.ui.btnDeleteGlobal.clicked.connect(self.delete_lagu)
        self.ui.btnSearch.clicked.connect(self.search_lagu)
        self.ui.btnSort.clicked.connect(self.sort_lagu)
        self.ui.btnDisplay.clicked.connect(self.display_lagu)
        self.ui.btnNext.clicked.connect(self.next_lagu)
        self.ui.btnPrevious.clicked.connect(self.previous_lagu)

    def insert_lagu(self):
        judul    = self.ui.inputJudul.text().strip()
        penyanyi = self.ui.inputPenyanyi.text().strip()
        durasi   = self.ui.inputDurasi.text().strip()
        genre    = self.ui.inputGenre.text().strip()

        if not judul:
            QMessageBox.warning(self, "Peringatan", "Judul lagu tidak boleh kosong!")
            return

        self.playlist.insert(judul, penyanyi, durasi, genre)

        self.ui.inputJudul.clear()
        self.ui.inputPenyanyi.clear()
        self.ui.inputDurasi.clear()
        self.ui.inputGenre.clear()

        self.display_lagu()
        self.ui.statusbar.showMessage(f"Lagu '{judul}' berhasil ditambahkan!", 3000)

    def delete_lagu(self):
        selected = self.ui.tablePlaylist.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih lagu yang ingin dihapus!")
            return

        judul_item = self.ui.tablePlaylist.item(selected, 1)
        if not judul_item:
            return

        judul = judul_item.text()
        konfirmasi = QMessageBox.question(
            self, "Konfirmasi",
            f"Hapus lagu '{judul}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if konfirmasi == QMessageBox.StandardButton.Yes:
            self.playlist.delete(judul)
            self.display_lagu()
            self.ui.statusbar.showMessage(f"Lagu '{judul}' berhasil dihapus!", 3000)

    def search_lagu(self):
        keyword = self.ui.inputSearch.text().strip()
        if not keyword:
             self.display_lagu()
             return

        hasil_node = self.playlist.search(keyword)
        hasil = [{"judul": n.judul, "penyanyi": n.penyanyi,
              "durasi": n.durasi, "genre": n.genre} for n in hasil_node]
        self.render_tabel(hasil)
        self.ui.statusbar.showMessage(f"Ditemukan {len(hasil)} lagu untuk '{keyword}'", 3000)

    def sort_lagu(self):
        index = self.ui.comboSort.currentIndex()
        key_map = {0: "judul", 1: "penyanyi", 2: "genre"}
        key = key_map.get(index, "judul")
        self.playlist.sort(key)
        self.display_lagu()
        self.ui.statusbar.showMessage(f"Playlist diurutkan berdasarkan {key.capitalize()}!", 3000)

    def display_lagu(self):
        semua = self.playlist.display()
        self.render_tabel(semua)
        self.ui.statusbar.showMessage(f"Menampilkan {len(semua)} lagu", 3000)

    def next_lagu(self):
        total = self.ui.tablePlaylist.rowCount()
        if total == 0:
            return
        self.current_index = min(self.current_index + 1, total - 1)
        self.ui.tablePlaylist.selectRow(self.current_index)

    def previous_lagu(self):
        total = self.ui.tablePlaylist.rowCount()
        if total == 0:
            return
        self.current_index = max(self.current_index - 1, 0)
        self.ui.tablePlaylist.selectRow(self.current_index)

    def render_tabel(self, data):
        self.ui.tablePlaylist.setRowCount(0)
        for i, lagu in enumerate(data):
            self.ui.tablePlaylist.insertRow(i)
            self.ui.tablePlaylist.setRowHeight(i, 36)

            self.ui.tablePlaylist.setItem(i, 0, QTableWidgetItem(str(i + 1)))
            self.ui.tablePlaylist.setItem(i, 1, QTableWidgetItem(lagu["judul"]))
            self.ui.tablePlaylist.setItem(i, 2, QTableWidgetItem(lagu["penyanyi"]))
            self.ui.tablePlaylist.setItem(i, 3, QTableWidgetItem(lagu["durasi"]))
            self.ui.tablePlaylist.setItem(i, 4, QTableWidgetItem(lagu["genre"]))
            self.ui.tablePlaylist.setItem(i, 5, QTableWidgetItem("—"))

            for col in [0, 3]:
                item = self.ui.tablePlaylist.item(i, col)
                if item:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
