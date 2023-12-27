import sys

import cv2
import numpy as np


def color_to_black_and_white(image, target_color, tolerance=40, flip_colors=False):
    lower_bound = np.array([c - tolerance for c in target_color])
    upper_bound = np.array([c + tolerance for c in target_color])

    # Create a binary mask for the target color range
    mask = np.all((image >= lower_bound) & (image <= upper_bound), axis=-1)

    # Convert the original image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a binary threshold to create a black-and-white image
    _, result = cv2.threshold(gray_image, 1, 255, cv2.THRESH_BINARY)

    # Set pixels with the target color to black
    result[mask] = 0

    # Invert the colors if flip_colors is True
    if flip_colors:
        result = cv2.bitwise_not(result)

    return result


def save_image(image, filename):
    cv2.imwrite(filename, image)
    print(f"Result image saved as {filename}")


def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) < 4:
        print("Usage: python binary-thresholder.py <image_path> <tolerance> <target_color> [-s [output_filename]] [-f]")
        sys.exit(1)

    # Load the image
    image = cv2.imread(sys.argv[1])

    # Parse command-line arguments
    tolerance = int(sys.argv[2])
    target_color = [int(c) for c in sys.argv[3].split(',')]
    flip_colors = '-f' in sys.argv

    # Convert the specified color to black and the rest to white
    result_image = color_to_black_and_white(image, target_color, tolerance, flip_colors)

    if '-s' in sys.argv:
        # Save the result image if the -s flag is provided

        # Find the index of the -s flag
        output_index = sys.argv.index('-s') + 1 if sys.argv.index('-s') + 1 < len(sys.argv) else None

        if output_index is not None and output_index < len(sys.argv) and not sys.argv[output_index].startswith('-'):
            # -s flag with output filename provided
            output_filename = sys.argv[output_index]
        else:
            # -s flag without output filename or -f flag
            output_filename = 'result_image.jpg'

        # Save the result image
        save_image(result_image, output_filename)
    else:
        # Display the original and result images
        cv2.imshow('Original Image', image)
        cv2.imshow('Result Image', result_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
