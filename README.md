# Baofeng UV21 load image formatter

This is an unofficial Python script for formatting 128x160 bitmap images into 160x128 bitmap images for upload to a Baofeng UV21.

The official CPS software only supports 160x128 images but the Baofeng UV21 has a 128x160 screen. So this script is needed to convert an image designed for the UV21 into a format suitable for upload.

## Required libraries
See requirements.txt
- [Numpy](https://numpy.org/install/)
- [Pillow](https://pypi.org/project/pillow/)

## Required software

- Python
- Upload software for Baofeng, T6UV v1.1.8

The software required to upload to the UV21 is available at https://www.miklor.com/COM/UV_Software.php, listed as T6UV v1.1.8

## Required Hardware

- Baofeng programming cable

## Usage

### Re-arrange image
- Design image as 128x160 image 
- Run script on image e.g. ```python .\rearrange_image.py example_image.bmp```
- Take now re-arranged image from out.bmp 

You can change the output path with the --output-file or -o command line option, run ```python .\rearrange_image.py -h``` for all options.

### Uploading to Baofeng UV21
- Run T6UV CPS
- Power on Baofeng and turn volume all the way up
- Connect Baofeng to your computer with the programming cable
- Select Setting and then the port of the Baofeng
- Click the read button (not strictly needed but good practice to check everything is setup), your programmed channels should appear
- Select tools and then power on picture
- Ensure correct port for Baofeng is selected
- Select open image and open the re-arranged image
- Click import and wait for image to upload, your Baofeng should restart and show the new boot up image

## Troubleshooting

### The upload was successful but I cannot see the logo
Ensure your baofeng power on message is set to logo (menu option 40)

### The image is not uploading/I cannot read my current channels
Attempt to use CHIRP to upload a known good image


## Author
Made by Ewan Radford, M7FTU