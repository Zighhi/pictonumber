import os
import imageio
from moviepy.editor import VideoFileClip

def extract_frames(input_file, output_folder, num_frames):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load the video file
    video = VideoFileClip(input_file)

    # Get video information
    fps = video.fps
    duration = video.duration
    resolution = video.size

    # Calculate the frame interval
    frame_interval = int(duration * fps / num_frames)

    # Extract frames at specified intervals
    frame_count = 0
    for t in range(0, int(duration * fps), frame_interval):
        frame = video.get_frame(t / fps)
        frame_filename = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        imageio.imwrite(frame_filename, frame)
        print(f"Frame {frame_count + 1}/{num_frames} saved")
        frame_count += 1
        if frame_count >= num_frames:
            break

    # Print video information
    print("Video Information:")
    print(f"FPS: {fps}")
    print(f"Duration: {duration} seconds")
    print(f"Resolution: {resolution}")

if __name__ == '__main__':
    input_file = r"C:\Users\zglum\OneDrive\Desktop\PictoprimeVideo\exemples\Magaru\magaru_cut.mp4"
    output_folder = r"C:\Users\zglum\OneDrive\Desktop\PictoprimeVideo\exemples\Magaru\frames"
    num_frames = 360

    extract_frames(input_file, output_folder, num_frames)
