from argparse import ArgumentParser
import io
from PIL import Image
import img2pdf
import pdf2image
from tqdm import tqdm

def compress_pdf(input_file: str, output_file: str, quality: int, dpi: int):
    """
    Compresses a PDF by reducing the image quality and DPI.
    
    `input_file`: name of the input PDF file
    `output_file`: name of the output compressed PDF file
    `quality`: quality of the output images (1-100). Lower is more compressed.
    `dpi`: DPI for rendering the PDF images. Lower DPI results in more compression.
    """
    print(f'Loading PDF {input_file}')
    input_images = pdf2image.convert_from_path(input_file, dpi=dpi)
    print(f'Pages: {len(input_images)}')

    output_images: list[bytes] = []
    for img in tqdm(input_images, desc=f"Compressing images at {quality}% quality", unit="pages"):
        # Convert image to JPEG format at the specified quality
        img_bytes = io.BytesIO()
        img.save(img_bytes, format="JPEG", quality=quality)
        output_images.append(img_bytes.getvalue())

    print(f'Saving compressed PDF to {output_file}')
    with open(output_file, "wb") as outf:
        img2pdf.convert(*output_images, outputstream=outf)

if __name__ == "__main__":
    parser = ArgumentParser(description="Compress a PDF by reducing image quality and DPI")
    parser.add_argument('-i', '--input', help="Input PDF filename", dest="input_file", required=True)
    parser.add_argument('-o', '--output', help="Output PDF filename", dest="output_file", required=True)
    parser.add_argument('-q', '--quality', type=int, default=75,
                        help="Quality of the output images (1-100). Default is 75.")
    parser.add_argument('--dpi', type=int, default=100,
                        help="DPI for rendering the PDF images. Default is 100 DPI.")
    
    args = parser.parse_args()
    
    compress_pdf(args.input_file, args.output_file, args.quality, args.dpi)
