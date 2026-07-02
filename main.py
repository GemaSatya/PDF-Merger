import os
from tkinter import Tk, filedialog
from pypdf import PdfWriter

def pilih_file_pdf():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)

    file_paths = filedialog.askopenfilenames(
        title="Pilih file PDF (urutan pemilihan akan menentukan urutan penggabungan)",
        filetypes=[("PDF files", "*.pdf")]
    )

    root.destroy()
    return list(file_paths)

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
    print("Silakan pilih file PDF yang ingin digabungkan.")
    print("Urutan penggabungan mengikuti urutan Anda mengklik/memilih file di dialog.\n")

    file_list = pilih_file_pdf()

    if not file_list:
        print("Tidak ada file yang dipilih. Program berhenti.")
        return

    print(f"\nJumlah file terpilih: {len(file_list)}")
    for i, f in enumerate(file_list, start=1):
        print(f"{i}. {os.path.basename(f)}")

    output_name = input("\nMasukkan nama file output (tanpa .pdf): ").strip()
    if not output_name:
        output_name = "hasil_gabungan"

    output_path = os.path.join(os.getcwd(), f"{output_name}.pdf")

    gabungkan_pdf(file_list, output_path)

if __name__ == "__main__":
    main()