import cv2
import numpy as np
from os import path, makedirs

def detect_leaf(image_name='StrawberryHealthy(1).JPG'):
    # Read image
    image = cv2.imread(image_name)

    # Apply Gaussian blurring
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # Convert to grayscale
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

    # Apply Otsu's thresholding
    _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Apply dilation to connect parts of the leaf
    kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(thresholded, kernel, iterations=2)

    # Find contours
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours based on area, for example
    min_area = 1000 # You may need to adjust this value
    filtered_contours = [c for c in contours if cv2.contourArea(c) > min_area]

    # Draw bounding boxes
    for contour in filtered_contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Get the filename without the directory
    filename = path.basename(image_name)

    # Create the output filename
    output_filename = 'leaves_detected_on_' + filename + '.png'

    # Path to the output directory
    output_folder = 'output'

    # Create the output directory if it doesn't exist
    if not path.exists(output_folder):
        makedirs(output_folder)

    # Join the output folder path with the output filename
    full_output_path = path.join(output_folder, output_filename)

    # Save the image as a PNG file
    cv2.imwrite(full_output_path, image)

    # Print the number of leaves detected
    print(f'Number of leaves detected on {image_name}: {len(filtered_contours)}')

if __name__ == '__main__':
    detect_leaf()