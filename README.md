# binary-thresholder
A small python script for black and white image thresholding

---

This script is a small CLI utility for doing black and white image thresholding.

Takes a color image and generates a black and white image with only 2 color values (0, 0, 0) and (255, 255, 255).

In the generated image, the given color will be black, and the rest of the image will be white.

Example usage:

`
python binary-thresholder.py .\example\original.jpg 40 100,133,116 -s .\example\output.jpg
`

[Original image (original.jpg)](https://github.com/dg-Pereira/binary-thresholder/blob/main/example/original.jpg)             |  [Output image (output.jpg)](https://github.com/dg-Pereira/binary-thresholder/blob/main/example/output.jpg)
:-------------------------:|:-------------------------:
![Original image](/example/original.jpg)  |  ![Output image](/example/output.jpg)

---

Parameters: <image_path> <tolerance> <target_color> [-s [output_filename]] [-f]

- **image_path**: Path to the input image file
- **tolerance**: Range aroung target_color that will be turned to black (recommended / default value is 40)
- **target_color**: Color that will be turned to black
- **-s [output_filename]**: Use this flag if you want to save the image instead of displaying it in a window. Default name is result_image.png, but a different name can be provided after the -s flag.
- **-f**: Flips the output colors (areas with the target color will be white, and the rest will be black)

Disclaimer: Developed with assistance of AI language generation models.
