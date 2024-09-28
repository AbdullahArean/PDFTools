# PDF Tools

This repository contains Python scripts for modifying PDFs, including adjusting contrast and brightness and compressing PDFs by reducing image quality and DPI.

## Table of Contents
1. [PDF Contrast and Brightness Adjuster](#pdf-contrast-and-brightness-adjuster)
   - [Features](#features)
   - [Requirements](#requirements)
   - [Usage](#usage)
   - [Example](#example)
2. [PDF Compressor](#pdf-compressor)
   - [Features](#features-1)
   - [Requirements](#requirements-1)
   - [Usage](#usage-1)
   - [Example](#example-1)

---

## PDF Contrast and Brightness Adjuster

This Python script adjusts the contrast and brightness of each page in a PDF file and outputs a modified PDF.

### Features
- Adjust the **contrast** of PDF pages.
- Adjust the **brightness** of PDF pages.
- Save the modified PDF as a new file.

### Requirements

To use this script, you'll need the following Python packages:

- `Pillow`
- `img2pdf`
- `pdf2image`
- `tqdm`

You can install them using pip:

```bash
pip install pillow img2pdf pdf2image tqdm
```

You will also need `poppler` installed on your system for `pdf2image` to work. You can install it as follows:

- On Ubuntu:

  ```bash
  sudo apt install poppler-utils
  ```

- On macOS using Homebrew:

  ```bash
  brew install poppler
  ```

### Usage

To run the script, use the following format:

```bash
python pdf_contrast.py <contrast> <brightness> -i <input_file> -o <output_file>
```

### Example Command

```bash
python pdf_contrast.py 1.5 1.2 -i input.pdf -o output.pdf
```

#### Parameters:
- `<contrast>`: The contrast multiplier (a float). `1` means no change, `2` doubles the contrast, `0.5` halves it.
- `<brightness>`: The brightness multiplier (a float). `1` means no change, `2` doubles the brightness, `0.5` halves it.
- `-i <input_file>`: The path to the input PDF file.
- `-o <output_file>`: The path to save the output PDF file.

### Example

```bash
python pdf_contrast.py 1.5 1.2 -i my_document.pdf -o adjusted_document.pdf
```

This command adjusts the contrast to 1.5x and the brightness to 1.2x for each page of `my_document.pdf`, and saves the result as `adjusted_document.pdf`.

---

## PDF Compressor

The `pdf_compressor.py` script reduces the size of a PDF by lowering the quality and resolution of its images.

### Features
- Compress a PDF by adjusting image quality and DPI.
- Output a smaller, compressed PDF file.

### Requirements

You’ll need the following Python packages:

- `Pillow`
- `img2pdf`
- `pdf2image`
- `tqdm`

Install them using pip:

```bash
pip install pillow img2pdf pdf2image tqdm
```

### Usage

To run the script, use the following format:

```bash
python pdf_compressor.py -i <input_file> -o <output_file> -q <quality> --dpi <dpi>
```

### Example Command

```bash
python pdf_compressor.py -i input.pdf -o compressed_output.pdf -q 60 --dpi 80
```

#### Parameters:
- `-i <input_file>`: The path to the input PDF file.
- `-o <output_file>`: The path to save the compressed PDF file.
- `-q <quality>`: Quality of the compressed images (1-100). Lower values result in smaller file sizes. Default is 75.
- `--dpi <dpi>`: Dots per inch (DPI) for rendering the images from the PDF. Lower DPI results in smaller file sizes. Default is 100 DPI.

### Example

```bash
python pdf_compressor.py -i document.pdf -o compressed_document.pdf -q 50 --dpi 72
```

This command compresses the input `document.pdf` by reducing image quality to 50% and setting the DPI to 72, and saves the compressed PDF as `compressed_document.pdf`.

---

## License

This project is licensed under the MIT License. Feel free to use and modify it!
