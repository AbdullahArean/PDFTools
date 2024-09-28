import PyPDF2
from argparse import ArgumentParser


def parse_page_ranges(page_ranges: str):
    """
    Parse a string of page ranges into a list of individual page numbers.
    For example, "1-2,4,6-8" will return [0, 1, 3, 5, 6, 7].

    `page_ranges`: A string representing page ranges.
    Returns a list of zero-indexed page numbers.
    """
    pages = set()
    ranges = page_ranges.split(',')

    for r in ranges:
        if '-' in r:
            start, end = r.split('-')
            pages.update(range(int(start) - 1, int(end)))  # Convert to zero-indexed
        else:
            pages.add(int(r) - 1)  # Convert to zero-indexed
    
    return sorted(pages)


def split_pdf(input_file: str, output_file: str, page_ranges: str):
    """
    Split a PDF based on specified page ranges and save it to an output file.

    `input_file`: Path to the input PDF file.
    `output_file`: Path to save the split PDF.
    `page_ranges`: Page ranges to extract (e.g., "1-2,4,6-8").
    """
    # Parse the page ranges string
    pages_to_extract = parse_page_ranges(page_ranges)

    # Read the input PDF
    reader = PyPDF2.PdfReader(input_file)
    writer = PyPDF2.PdfWriter()

    # Extract the specified pages
    for page_num in pages_to_extract:
        if 0 <= page_num < len(reader.pages):
            writer.add_page(reader.pages[page_num])
        else:
            print(f"Page {page_num + 1} is out of range.")

    # Write the new PDF
    with open(output_file, 'wb') as out_pdf:
        writer.write(out_pdf)

    print(f'Saved split PDF to {output_file}')


if __name__ == "__main__":
    parser = ArgumentParser(description="Split a PDF by page ranges")
    parser.add_argument('-i', '--input', help="Input PDF filename", required=True)
    parser.add_argument('-o', '--output', help="Output PDF filename", required=True)
    parser.add_argument('ranges', help="Page ranges to extract (e.g., 1-2,4,6-8)")

    args = parser.parse_args()
    
    split_pdf(args.input, args.output, args.ranges)
