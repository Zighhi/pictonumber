import os
from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip
import numpy as np

# Specify the paths to the existing video and transparent video
existing_video_path = r"C:\Users\zglum\OneDrive\Desktop\PictoprimeVideo\exemples\Magaru\magaru_cut.mp4"
transparent_video_path = r"C:\Users\zglum\OneDrive\Desktop\PictoprimeVideo\exemples\Magaru\video.mp4"

# Load the existing video
existing_video = VideoFileClip(existing_video_path)

# Load the transparent video
transparent_video = VideoFileClip(transparent_video_path)

# Resize the transparent video to match the resolution of the existing video
transparent_video = transparent_video.resize(existing_video.size)

# Adjust the duration of the transparent video to match the existing video
transparent_video = transparent_video.set_duration(existing_video.duration)

# Set the transparency of the transparent video clip
transparent_video = transparent_video.set_opacity(0.8)  # Adjust the opacity as desired



# Overlay the transparent video onto the existing video
overlay_video = CompositeVideoClip([existing_video.set_opacity(1), transparent_video])

# Generate the final video by concatenating the overlay video with the existing video
final_video = concatenate_videoclips([overlay_video])

# Specify the output path for the final video
output_path = r"C:\Users\zglum\OneDrive\Desktop\PictoprimeVideo\exemples\Magaru\final_video.mp4"

# Export the final video to a file
final_video.write_videofile(output_path)
