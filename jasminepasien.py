print("=== DATA PASIEN RUMAH SAKIT ===")

nama = input("Nama pasien: ")

print("\nPilih jenis penyakit:")
print("1. Demam Berdarah (DBD)")
print("2. Tifus")
print("3. Pneumonia")
print("4. Stroke")
print("5. Muntaber / Diare Parah")
print("6. Diabetes")
print("7. Malaria Berat")
print("8. Tumor Otak")
print("9. Tuberkulosis (TBC)")
print("10. Apendisitis")

pilihan = int(input("Masukkan pilihan: "))

if pilihan == 1:
    penyakit = "Demam Berdarah (DBD)"
elif pilihan == 2:
    penyakit = "Tifus"
elif pilihan == 3:
    penyakit = "Pneumonia"
elif pilihan == 4:
    penyakit = "Stroke"
elif pilihan == 5:
    penyakit = "Muntaber / Diare Parah"
elif pilihan == 6:
    penyakit = "Diabetes"
elif pilihan == 7:
    penyakit = "Malaria Berat"
elif pilihan == 8:
    penyakit = "Tumor Otak"
elif pilihan == 9:
    penyakit = "Tuberkulosis (TBC)"
elif pilihan == 10:
    penyakit = "Apendisitis"
else:
    penyakit = "Tidak ditemukan"

if pilihan >= 1 and pilihan <= 10:
    hari = int(input("Lama menginap (hari): "))

    biaya = hari * 350000
    makanan = "Makanan khusus sesuai kebutuhan nutrisi pasien" if hari > 3 else "Makanan biasa rumah sakit"

    print("\n=== HASIL DATA PASIEN ===")
    print("Nama pasien:", nama)
    print("Penyakit:", penyakit)
    print("Status: Pasien opname")
    print("Fasilitas: Kamar, tempat tidur, dokter, perawat, dan obat-obatan")
    print("Makanan:", makanan)
    print("Kunjungan: Pukul 10.00-12.00 dan 16.00-18.00")
    print("Lama menginap:", hari, "hari")
    print("Total biaya: Rp", biaya)
else:
    print("Pilihan penyakit tidak tersedia")

print("\n=== TERIMA KASIH ===")