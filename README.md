# Video to Panorama Converter

This Python script converts a video into a panorama image by extracting frames and stitching them together using OpenCV.

## Features
- Extract frames from a video at regular intervals.
- Stitch the extracted frames into a single panorama image.
- Saves the final panorama as a `.jpg` file.

## Requirements
- Python 3.x
- OpenCV library

Install the required Python library using pip:
```bash
pip install opencv-python
```

## Usage

### 1. Clone or Download the Repository
Download or clone this repository to your local machine:
```bash
git clone https://github.com/shakauthossain/AI_Based_Video_To_Panorama.git
cd video-to-panorama
```

### 2. Replace the Video File
Place your video file in the root directory and update the path in the script:
```python
video_path = "input_video.mp4"  # Replace with your video file path
```

### 3. Run the Script
Run the Python script:
```bash
python video_to_panorama.py
```

### 4. Output Files
- Extracted frames are saved in the `frames/` directory.
- The stitched panorama is saved as `panorama.jpg` in the root directory.

## Script Overview

### Extract Frames
The `extract_frames` function extracts frames from the video at a specified interval and saves them as `.jpg` files in the `frames/` directory:
```python
def extract_frames(video_path, output_dir, frame_interval=30):
```

### Create Panorama
The `create_panorama` function stitches the frames together into a single panorama image using OpenCV's `Stitcher_create`:
```python
def create_panorama(image_dir, output_panorama):
```

### Main Workflow
The `main` function orchestrates the workflow:
1. Extract frames from the video.
2. Stitch the extracted frames into a panorama.
```python
if __name__ == "__main__":
    main()
```

## Customization
- **Frame Interval**: Adjust the `frame_interval` in `extract_frames` to control how often frames are extracted. Lower values produce more frames and potentially smoother panoramas.
- **Video Path**: Update `video_path` to the location of your video file.
- **Output Paths**: Change the `frame_output_dir` and `panorama_output_path` to save the frames and panorama to different locations.

## Troubleshooting
- **Stitching Errors**: If stitching fails, it may be due to:
  - Insufficient overlap between frames.
  - Poor quality video.
  - Non-linear camera motion.

  Try reducing the `frame_interval` or using a video with smoother motion.

- **Performance**: For long videos, extracting and stitching can take significant time. Optimize by limiting the video length or resizing frames.

## Contact
For questions or suggestions, contact [Shakaut Hossain](mailto:shakauthossain0@gmail.com).
