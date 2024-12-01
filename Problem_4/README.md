## Problem Description

This notebook uses OpenCV to detect drawn digits in an image using template matching. The program matches digit templates (1–9) with the main image, scales the image to find the optimal match, and highlights detected digits with bounding boxes and labels.

### Key Steps:
1. **Load and Binarize Images**:
   - The main image containing digits is binarized.
   - Templates for digits 1–9 are also binarized.
2. **Mask Creation for Specific Digits**:
   - Masks are created for digits 4, 5, and 6 by filling their interiors with black.
3. **Scale Optimization**:
   - A pyramid of scales is applied to the main image to find the scale with the highest template correlation.
4. **Template Matching**:
   - All matching positions with a correlation score ≥ 0.95 are recorded for the optimal scale.
5. **Visualization**:
   - The program highlights detected digits with rectangles and labels the bounding boxes with the corresponding digit.

---

## Usage

1. Place your main image (e.g., `digits_main_image.png`) and digit templates (e.g., `template_1.png`, `template_2.png`, ...) in the project directory.

2. Modify the image and template paths in the script:
   ```python
   main_image_path = "digits_main_image.png"
   template_path = f"template_{digit}.png"
   ```
3. The output will display the detected digits on the image using matplotlib.

---

## File Structure

- **digit_detection.py**: Main script to run the detection.
- **template_<num>**: images for digit templates (1–7).
- **digits_main_image.png**: Main image containing digits to analyze.

---

## Example Output

The program processes the main image and marks all detected digits with bounding boxes. Each bounding box is labeled with the corresponding digit.

---

## Dependencies

- Python 3.8+
- OpenCV
- NumPy
- Matplotlib

---

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you want to enhance the project.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

--- 

