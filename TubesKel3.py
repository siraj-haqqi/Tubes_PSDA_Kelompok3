# TubesKel3.py
# Struktur Data: Doubly Linked List untuk Playlist Musik

class Node:
    def __init__(self, judul, penyanyi, durasi, genre):
        self.judul    = judul
        self.penyanyi = penyanyi
        self.durasi   = durasi
        self.genre    = genre
        self.prev     = None
        self.next     = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # ──────────────────────────────────────────────
    # INSERT — Tambah lagu ke akhir list
    # ──────────────────────────────────────────────
    def insert(self, judul, penyanyi, durasi, genre):
        node_baru = Node(judul, penyanyi, durasi, genre)
        if self.head is None:
            self.head = node_baru
            self.tail = node_baru
        else:
            node_baru.prev = self.tail
            self.tail.next = node_baru
            self.tail = node_baru
        self.size += 1

    # ──────────────────────────────────────────────
    # DELETE — Hapus lagu berdasarkan judul
    # ──────────────────────────────────────────────
    def delete(self, judul):
        current = self.head
        while current:
            if current.judul.lower() == judul.lower():
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                self.size -= 1
                return True  # berhasil dihapus
            current = current.next
        return False  # tidak ditemukan

    # ──────────────────────────────────────────────
    # DELETE BY INDEX — Hapus lagu berdasarkan index
    # ──────────────────────────────────────────────
    def delete_by_index(self, index):
        if index < 0 or index >= self.size:
            return False
        current = self.head
        for _ in range(index):
            current = current.next
        return self.delete(current.judul)

    # ──────────────────────────────────────────────
    # SEARCH — Cari lagu berdasarkan judul/penyanyi
    # ──────────────────────────────────────────────
    def search(self, keyword):
        hasil = []
        current = self.head
        keyword = keyword.lower()
        while current:
            if (keyword in current.judul.lower() or
                keyword in current.penyanyi.lower() or
                keyword in current.genre.lower()):
                hasil.append(current)
            current = current.next
        return hasil

    # ──────────────────────────────────────────────
    # SORT — Urutkan dengan Bubble Sort
    # ──────────────────────────────────────────────
    def sort(self, key="judul"):
        if self.head is None:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current and current.next:
                val_a = getattr(current, key).lower()
                val_b = getattr(current.next, key).lower()
                if val_a > val_b:
                    # Tukar data (bukan pointer)
                    current.judul,    current.next.judul    = current.next.judul,    current.judul
                    current.penyanyi, current.next.penyanyi = current.next.penyanyi, current.penyanyi
                    current.durasi,   current.next.durasi   = current.next.durasi,   current.durasi
                    current.genre,    current.next.genre    = current.next.genre,    current.genre
                    swapped = True
                current = current.next

    # ──────────────────────────────────────────────
    # DISPLAY — Kembalikan semua lagu sebagai list
    # ──────────────────────────────────────────────
    def display(self):
        hasil = []
        current = self.head
        while current:
            hasil.append({
                "judul":    current.judul,
                "penyanyi": current.penyanyi,
                "durasi":   current.durasi,
                "genre":    current.genre,
            })
            current = current.next
        return hasil

    # ──────────────────────────────────────────────
    # Helper: ambil node ke-index (untuk navigasi)
    # ──────────────────────────────────────────────
    def get_by_index(self, index):
        if index < 0 or index >= self.size:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
