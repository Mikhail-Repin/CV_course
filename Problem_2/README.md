# Object Detection from Video Stream Using Background Subtraction

This script processes a video to detect and highlight moving objects using a background subtraction technique. It applies preprocessing, background modeling, and noise filtering to extract meaningful object information. 

## Features
- Loads a video and resizes frames to a standard size for consistency.
- Computes an average background using a specified number of initial frames.
- Corrects frame brightness to match the average background brightness.
- Detects differences between the current frame and the background.
- Applies thresholding, noise reduction, and object filtering to isolate moving objects.
- Displays the processed frame with detected objects highlighted.

## Requirements
Ensure you have the following libraries installed:
- OpenCV (`cv2`)
- NumPy (`numpy`)

Install them using pip if necessary:
```bash
pip install opencv-python-headless numpy
```

## How It Works
1. **Video Input**: The script reads a video file (`test.mp4`). If the video cannot be opened, an error message is displayed.
2. **Background Initialization**: 
   - Captures the first few frames (default: 10).
   - Resizes and converts these frames to grayscale.
   - Calculates the average background and smooths it with a Gaussian blur.
   - Computes the average brightness of the background for brightness normalization.
3. **Frame Processing**:
   - Each frame is resized and converted to grayscale.
   - Brightness is normalized using the background's average brightness.
   - Calculates the absolute difference between the current frame and the background.
   - Applies binary thresholding with Otsu's method to create a mask of moving regions.
   - Removes small noise with morphological operations.
   - Filters connected components based on size to isolate meaningful objects.
   - Applies additional morphological closing to refine object boundaries.
4. **Display**:
   - Combines the detected regions with the current frame for visualization.
   - The processed frame is displayed in a real-time window.
   - Press 'q' to exit the program.

## Parameters
- `threshold_value`: Initial threshold for binary mask creation (default: 50).
- `num_background_frames`: Number of frames used for background initialization (default: 10).
- `min_area`: Minimum area of connected components to be considered as valid objects (default: 3000 pixels).

## How to Run
1. Place the video file (`test.mp4`) in the same directory as the script.
2. Run the script using Python:
   ```bash
   python detect_objects.py
   ```
3. Press 'q' to stop the video processing and close the application.

## Notes
- Ensure `test.mp4` exists in the same directory or modify the `cv2.VideoCapture()` path to point to your video file.
- Adjust parameters like `threshold_value`, `num_background_frames`, or `min_area` to optimize detection for your video content.
- High computational resources may be required for real-time processing on large videos.

## Example Output
The program highlights moving objects in the video by isolating them against a dynamically modeled background. The resulting frames are displayed in a real-time window. 

---

Feel free to modify and expand this script for your specific use case.