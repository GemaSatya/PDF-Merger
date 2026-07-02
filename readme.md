# PDF Merger

A simple Python program to merge multiple PDF files into one, with the merge order following the order in which the files are selected (uploaded) by the user.

## Features

- Select PDF files through an upload dialog (file explorer)
- Merge order follows the file selection order
- Displays the list of selected files before merging
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

2. A file explorer dialog will appear automatically.
3. Select the PDF files you want to merge. The order in which you click/select the files will determine the merge order in the final output file.
4. After the files are selected, the program will display the list of files along with their order in the terminal.
5. Enter the output file name when prompted (without the .pdf extension).
6. The merged file will be saved in the same folder as the script.

## Output Structure

The merged file will be named according to the user's input, for example:

```
hasil_gabungan.pdf
```

## Important Notes

The order of file selection in the upload dialog depends on the operating system being used. On most Windows systems, the click order will be preserved according to the selection order. However, if the order does not turn out as expected, it is recommended to use a method where files are selected one by one in sequence.

## License

Free to use and modify for personal or academic purposes.
