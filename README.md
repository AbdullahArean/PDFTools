# PDF Contrast and Brightness Adjuster

This Python script adjusts the contrast and brightness of each page in a PDF file and outputs a modified PDF.

## Features
- Adjust the **contrast** of PDF pages.
- Adjust the **brightness** of PDF pages.
- Save the modified PDF as a new file.

## Requirements

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

## Usage

To run the script, use the following format:

```bash
python pdf_contrast_brightness.py <contrast> <brightness> -i <input_file> -o <output_file>
```

### Example Command

```bash
python pdf_contrast_brightness.py 1.5 1.2 -i input.pdf -o output.pdf
```

### Parameters:
- `<contrast>`: The contrast multiplier (a float). `1` means no change, `2` doubles the contrast, `0.5` halves it.
- `<brightness>`: The brightness multiplier (a float). `1` means no change, `2` doubles the brightness, `0.5` halves it.
- `-i <input_file>`: The path to the input PDF file.
- `-o <output_file>`: The path to save the output PDF file.

### Output

The script processes each page of the input PDF, applies the specified contrast and brightness adjustments, and saves a new PDF with the modified pages.

## Example

```bash
python pdf_contrast_brightness.py 1.5 1.2 -i my_document.pdf -o adjusted_document.pdf
```

This command adjusts the contrast to 1.5x and the brightness to 1.2x for each page of `my_document.pdf`, and saves the result as `adjusted_document.pdf`.

## License

This project is licensed under the MIT License. Feel free to use and modify it!
