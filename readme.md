# PDF Merger

A simple Python program to merge multiple PDF files into one, with the merge order following the order in which the user selects the files one by one.

## Features

- Select PDF files one at a time through an upload dialog (file explorer)
- Merge order strictly follows the order in which files are selected
- Option to keep adding files until you are done
- Confirmation step showing the final file order before merging
- Output is saved as a single new PDF file

## Requirements

- Python 3.7 or newer
- `pypdf` library

## Installation

Install the required library with the following command:

```
pip install pypdf
```

Note: the `tkinter` module is usually included in the standard Python installation. If it is not available (for example on some Linux distributions), install it with:

```
sudo apt-get install python3-tk
```

## How to Run

1. Run the script through terminal or command prompt:

```
python merge_pdf.py
```

2. A file explorer dialog will appear, asking you to select one PDF file at a time.
3. After selecting a file, you will be asked whether you want to add another file (`y`) or stop (`n`).
4. Repeat step 2-3 until all the PDF files you want to merge have been selected, in the exact order you want them merged.
5. The program will display the final order of the selected files for confirmation.
6. Enter the output file name when prompted (without the .pdf extension).
7. The merged file will be saved in the same folder as the script.

## Why Files Are Selected One by One

The standard file explorer dialog (`askopenfilenames`) does not always preserve the order in which files are clicked, it often returns files sorted by name or by the operating system's internal order instead. To guarantee that the merge order always matches the user's intended order, this program asks the user to select files one at a time instead of selecting multiple files at once.

## Output Structure

The merged file will be named according to the user's input, for example:

```
hasil_gabungan.pdf
```

## License

Free to use and modify for personal or academic purposes.
