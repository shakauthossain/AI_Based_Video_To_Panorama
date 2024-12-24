import cv2
import os

def extract_frames(video_path, output_dir, frame_interval=30):
    """
    Extract frames from a video at regular intervals.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    cap = cv2.VideoCapture(video_path)
    count = 0
    saved_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        if count % frame_interval == 0:
            frame_path = os.path.join(output_dir, f"frame_{saved_count}.jpg")
            cv2.imwrite(frame_path, frame)
            saved_count += 1
        count += 1

    cap.release()
    print(f"Extracted {saved_count} frames to {output_dir}")

def create_panorama(image_dir, output_panorama):
    """
    Create a panorama from a directory of images.
    """
    # Load all images
    images = []
    for filename in sorted(os.listdir(image_dir)):
        img_path = os.path.join(image_dir, filename)
        img = cv2.imread(img_path)
        if img is not None:
            images.append(img)

    # Use OpenCV's Stitcher
    stitcher = cv2.Stitcher_create()
    status, panorama = stitcher.stitch(images)
    
    if status == cv2.Stitcher_OK:
        cv2.imwrite(output_panorama, panorama)
        print(f"Panorama saved to {output_panorama}")
    else:
        print(f"Error during stitching: {status}")

def main():
    video_path = "video.mp4"  # Replace with your video file path
    frame_output_dir = "frames"
    panorama_output_path = "panorama.jpg"
    
    # Step 1: Extract frames from video
    extract_frames(video_path, frame_output_dir, frame_interval=30)
    
    # Step 2: Create panorama
    create_panorama(frame_output_dir, panorama_output_path)

if __name__ == "__main__":
    main()
