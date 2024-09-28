
from argparse import ArgumentParser
import io

from PIL import ImageEnhance
import img2pdf
import pdf2image
from tqdm import tqdm


def pdf_adjust(input_file: str, contrast: float, brightness: float, output_file: str):
    """
    Create a new pdf adjusting contrast and brightness.
    `input_file`: name the of the input_file
    `contrast`: contrast multiplier. 1 corresponds to no change
    `brightness`: brightness multiplier. 1 corresponds to no change
    `output_file`: name of the file to be saved
    """

    print(f'Loading pdf {input_file}')
    input_images = pdf2image.convert_from_path(input_file)
    print(f'Pages: {len(input_images)}')

    output_images: list[bytes] = []
    for img in tqdm(input_images,
                    desc=f"Contrast x{contrast}, Brightness x{brightness}",
                    unit="pages"
                    ):
        # Adjust contrast
        contrast_enhancer = ImageEnhance.Contrast(img)
        contrast_img = contrast_enhancer.enhance(contrast)

        # Adjust brightness
        brightness_enhancer = ImageEnhance.Brightness(contrast_img)
        final_img = brightness_enhancer.enhance(brightness)

        out_img_bytes = io.BytesIO()
        final_img.save(out_img_bytes, format="JPEG")
        output_images.append(out_img_bytes.getvalue())

    print(f'Saving pdf to {output_file}')
    with open(output_file, "wb") as outf:
        img2pdf.convert(*output_images, outputstream=outf)


if __name__ == "__main__":
    input_file = "in.pdf"
    contrast = 1.2
    brightness = 1.0
    output_file = f"out_adjusted_contrast{contrast}_brightness{brightness}.pdf"

    parser = ArgumentParser(description="Modify contrast and brightness of PDFs")
    parser.add_argument('-i', '--input',
                        help="Input filename",
                        dest="input_file")
    parser.add_argument('-o', '--output',
                        help="Output file name",
                        dest="output_file")
    parser.add_argument('contrast', type=float,
                        help="""
                             Contrast multiplier, must be a float.
                             1 corresponds to no change (1x).
                             2 corresponds to double (2x).
                             0.5 corresponds to half (0.5x).
                             """)
    parser.add_argument('brightness', type=float,
                        help="""
                             Brightness multiplier, must be a float.
                             1 corresponds to no change (1x).
                             2 corresponds to double (2x).
                             0.5 corresponds to half (0.5x).
                             """)
    
    args = parser.parse_args()
    pdf_adjust(args.input_file, args.contrast, args.brightness, args.output_file)