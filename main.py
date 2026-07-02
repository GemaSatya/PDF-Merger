import os
from tkinter import Tk, filedialog
from pypdf import PdfWriter

def pilih_file_satu_per_satu():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)

    file_list = []
    nomor = 1

    while True:
        path = filedialog.askopenfilename(
            title=f"Pilih file PDF ke-{nomor}",
            filetypes=[("PDF files", "*.pdf")]
        )

        if not path:
            # Kalau user tekan cancel, tanya apakah mau berhenti
            if file_list:
                break
            else:
                print("Tidak ada file yang dipilih. Program berhenti.")
                root.destroy()
                return []

        file_list.append(path)
        print(f"{nomor}. {os.path.basename(path)} ditambahkan.")
        nomor += 1

        lanjut = input("Tambah file PDF lagi? (y/n): ").strip().lower()
        if lanjut != 'y':
            break

    root.destroy()
    return file_list

def gabungkan_pdf(list_file, output_path):
    merger = PdfWriter()

    for path in list_file:
        merger.append(path)
        print(f"Menambahkan: {os.path.basename(path)}")

    with open(output_path, "wb") as f_out:
        merger.write(f_out)

    merger.close()
    print(f"\nBerhasil digabungkan menjadi: {output_path}")

def main():
    print("Silakan pilih file PDF satu per satu sesuai urutan yang diinginkan.\n")

    file_list = pilih_file_satu_per_satu()

    if not file_list:
        return

    print(f"\nUrutan file yang akan digabungkan:")
    for i, f in enumerate(file_list, start=1):
        print(f"{i}. {os.path.basename(f)}")

    konfirmasi = input("\nLanjutkan penggabungan dengan urutan di atas? (y/n): ").strip().lower()
    if konfirmasi != 'y':
        print("Program dibatalkan.")
        return

    output_name = input("Masukkan nama file output (tanpa .pdf): ").strip()
    if not output_name:
        output_name = "hasil_gabungan"

    output_path = os.path.join(os.getcwd(), f"{output_name}.pdf")

    gabungkan_pdf(file_list, output_path)

if __name__ == "__main__":
    main()