"""
Tugas Modul 3 - Rekayasa Perangkat Lunak
Program Biodata Sederhana
"""

def tampilkan_biodata():
    print("=== Biodata Mahasiswa ===")
    nama = "Stevalia Bindi Rahmania"
    nim = "F 521 25 20 040"
    kelas = "A"
    prodi = "S1 Sistem Informasi"
    fakultas = "Teknik"
    universitas = "Universitas Tadulako"

    print(f"Nama       : {nama}")
    print(f"NIM        : {nim}")
    print(f"Kelas      : {kelas}")
    print(f"Prodi      : {prodi}")
    print(f"Fakultas   : {fakultas}")
    print(f"Universitas: {universitas}")
    print("Status: Setup Berhasil!")


if __name__ == "__main__":
    tampilkan_biodata()