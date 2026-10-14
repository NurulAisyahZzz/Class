# ==========================================
# SISTEM PENGGAJIAN KARYAWAN
# Pemrograman Berorientasi Objek (OOP)
# ==========================================

# 1. SUPERCLASS: Karyawan
class Karyawan:
    def __init__(self, nama, id_karyawan, gaji_pokok):
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.__gaji_pokok = gaji_pokok

    # Getter untuk mengambil gaji pokok
    def get_gaji_pokok(self):
        return self.__gaji_pokok

    # Setter untuk mengubah gaji pokok
    def set_gaji_pokok(self, gaji_pokok):
        if gaji_pokok <= 0:
            print("Peringatan: Gaji pokok harus lebih dari 0!")
        else:
            self.__gaji_pokok = gaji_pokok
            print("Gaji pokok berhasil diperbarui.")

    # Method dasar
    def hitung_gaji_total(self):
        return self.__gaji_pokok

    def tampilkan_info(self):
        print(f"Nama        : {self.nama}")
        print(f"ID Karyawan : {self.id_karyawan}")
        print(f"Gaji Pokok  : Rp{self.get_gaji_pokok():,.0f}")


# 2. CHILD CLASS: Karyawan Tetap
class KaryawanTetap(Karyawan):
    def __init__(self, nama, id_karyawan, gaji_pokok, tunjangan):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.tunjangan = tunjangan

    # Overriding method hitung_gaji_total
    def hitung_gaji_total(self):
        return self.get_gaji_pokok() + self.tunjangan

    # Overriding method tampilkan_info
    def tampilkan_info(self):
        print("\n=== DATA KARYAWAN TETAP ===")
        super().tampilkan_info()
        print(f"Tunjangan   : Rp{self.tunjangan:,.0f}")
        print(f"Total Gaji  : Rp{self.hitung_gaji_total():,.0f}")


# 3. CHILD CLASS: Karyawan Kontrak
class KaryawanKontrak(Karyawan):
    def __init__(self, nama, id_karyawan, gaji_pokok,
                 jam_lembur, tarif_lembur):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.jam_lembur = jam_lembur
        self.tarif_lembur = tarif_lembur

    # Overriding method hitung_gaji_total
    def hitung_gaji_total(self):
        return (
            self.get_gaji_pokok()
            + (self.jam_lembur * self.tarif_lembur)
        )

    # Overriding method tampilkan_info
    def tampilkan_info(self):
        print("\n=== DATA KARYAWAN KONTRAK ===")
        super().tampilkan_info()
        print(f"Jam Lembur  : {self.jam_lembur} jam")
        print(f"Tarif/Jam   : Rp{self.tarif_lembur:,.0f}")
        print(
            f"Total Lembur: Rp"
            f"{self.jam_lembur * self.tarif_lembur:,.0f}"
        )
        print(f"Total Gaji  : Rp{self.hitung_gaji_total():,.0f}")


# 4. MAIN PROGRAM
karyawan1 = KaryawanTetap(
    "Nurul Aisyah Z", "K001", 5000000, 1000000
)

karyawan2 = KaryawanKontrak(
    "Dewi Andira", "K002", 3500000, 10, 50000
)

# Menyimpan objek ke dalam list
daftar_karyawan = [karyawan1, karyawan2]

# Demonstrasi polymorphism
print("===== DAFTAR PENGGAJIAN KARYAWAN =====")

for karyawan in daftar_karyawan:
    karyawan.tampilkan_info()

# Demonstrasi encapsulation
print("\n===== PENGUJIAN ENCAPSULATION =====")

print("\n1. Mengubah gaji dengan nilai tidak valid:")
karyawan1.set_gaji_pokok(-1000000)
karyawan2.set_gaji_pokok(-500000)

print("\n2. Mengubah gaji dengan nilai valid:")
karyawan1.set_gaji_pokok(6000000)
karyawan2.set_gaji_pokok(4000000)

print("\n3. Menampilkan ulang data karyawan:")
karyawan1.tampilkan_info()
karyawan2.tampilkan_info()
