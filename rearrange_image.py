"""
A Python script for formatting 128x160 bitmap images into 160x128 bitmap images for upload to a Baofeng UV21.
"""

__author__ = "Ewan Radford"
__license__ = "AGPL-3.0"

from PIL import Image
import numpy as np
from math import floor
from pathlib import Path
import argparse

def rearrange_image(original_image: Path, output_path: Path, output_filetype: str = "bmp",output_width: int = 160, output_height: int = 128) -> None:
    """
    Re-arranges an image line by line

    Arguments:
        original_image: A Path object to the original image
        output_path: A Path object to where the result should be outputted
        output_width: An integer containing the width the output image should have
        output_height: An integer containing the height the output image should have

    No Return

    Raises:
        ValueError: If input and output image do not have the same number of pixels
    """
    original = Image.open(original_image)
    original_numpy = np.asarray(original)

    original_pixel_no = original_numpy.shape[0] * original_numpy.shape[1]

    #checking original number of pixels matches the number of output pixels
    if original_pixel_no != (output_width * output_height) :
        raise ValueError("Input image must have same number of pixels as desired output image")

    #creating output as 2 dimensional array in desired dimensions
    output = [[] for i in range(output_height)]
    i = 0
    #read through each pixel row by row and store into the output
    for current_row in original_numpy :
        for current_pixel in current_row :
            output[floor(i/output_width)].append(current_pixel)
            i+= 1

    #if output directory doesn't exist create it
    output_path.parent.mkdir(parents=True, exist_ok=True)

    output_numpy = np.array(output)
    output_image = Image.fromarray(output_numpy)
    output_image.save(output_path, output_filetype)

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description="Re-arrange an image for upload to a Baofeng UV-21")
    parser.add_argument("input_file", type=str, help="The input file to be re-arranged.")
    parser.add_argument("-o", "--output_file", dest="output_file", type=str, default="out.bmp", help="The path of the output image.")
    parser.add_argument("-t", "--output_filetype", dest="output_filetype", type=str, default="bmp", metavar="FILETYPE", choices=Image.registered_extensions().keys(),help="The filetype extension of the output image, defaults to bmp, must be a filetype extension supported by pillow.")
    parser.add_argument("-w", "--output_width", dest="output_width", type=int, default=160, help="The desired width of the output image, no need to change if using software described in readme.")
    parser.add_argument("-d", "--output_height", dest="output_height", type=int, default=128, help="The desired height of the output image, no need to change if using software described in readme.")
    args = parser.parse_args()
    rearrange_image(Path(args.input_file), Path(args.output_file), output_width=args.output_width, output_height=args.output_height)