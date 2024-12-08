# Card Digit Recognition

This project focuses on recognizing digits present on a card image using computer vision techniques with Python.
 vision techniques with Python.

## Overview

The script processes an image of a card, detects its boundaries, corrects its perspective, and then uses template matching to identify digits present on it.

## Dependencies

Make sure you have the following libraries installed. You can install them using pip:

```bash
pip install opencv-python numpy matplotlib
```

- **opencv-python:** For image processing tasks.
- **numpy:** For numerical operations.
- **matplotlib:** For displaying images.

## Usage

1. **Prepare the environment:** Ensure you have Python installed and the necessary libraries as mentioned in the Dependencies section.
2. **Place the image:**  Put the card image you want to process in the same directory as the script and name it `card_distors.jpg`.
3. **Place the template images:** Place the digit template images (named `tpl_1.png`, `tpl_2.png`, ..., `tpl_9.png`) in the same directory as the script. These templates should be grayscale images of individual digits.

The script will then:

- Load the card image.
- Preprocess the image to detect the card's outline.
- Identify and merge lines on the card.
- Correct the perspective of the card.
- Attempt to find digits using template matching at different scales.
- Display the detected digits on the straightened card image.

## Code Explanation

Here's a breakdown of the main steps in the code:

1. **Image Loading and Preprocessing:**
   - Loads the image `card_distors.jpg`.
   - Converts it to grayscale.
   - Applies binary thresholding to create a binary image.
   - Extracts the main card mask using connected components.

2. **Contour Detection:**
   - Finds contours in the card mask.
   - Draws the contours on a separate image.

3. **Line Detection using Hough Transform:**
   - Detects lines in the contour image using the Probabilistic Hough Transform.

4. **Line Merging and Filtering:**
   - Implements functions to:
     - Calculate the distance from a point to a line segment.
     - Determine if two line segments are close.
     - Merge close line segments.
     - Find the K longest line segments.
     - Sort line segments by their polar angle.
   - Applies these functions to refine the detected lines, merging close ones and selecting the four longest lines, sorted by angle.

5. **Intersection Point Calculation:**
   - Defines a function to calculate the intersection point of two line segments.
   - Calculates the intersection points of the four detected lines to find the corners of the card.

6. **Perspective Correction:**
   - Defines source points (the detected corners) and target points (the desired straightened rectangle).
   - Calculates the perspective transformation matrix.
   - Warps the original card image to correct its perspective.

7. **Digit Template Matching:**
   - Defines functions to:
     - Load and preprocess template images of digits.
     - Find the best scale for template matching by testing different scales.
     - Perform template matching to detect digits in the straightened card image.
   - Loads digit templates (assumes files named `tpl_1.png` to `tpl_9.png`).
   - Performs template matching at various scales to identify digits.

8. **Result Visualization:**
   - Defines a function to plot the detected digits on the image by drawing rectangles around the matched regions.
   - Displays the final image with the detected digits.

## Potential Improvements

- **Robust Template Matching:** Explore more robust template matching techniques or consider using feature-based matching methods.
- **Multiple Digit Recognition:**  Refine the digit detection to accurately identify and separate multiple digits that might be close together.
- **Automatic Template Generation:** Implement a mechanism to automatically generate or select appropriate digit templates.

Feel free to contribute to this project by submitting pull requests or opening issues for bugs and feature requests.