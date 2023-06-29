from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def cut_video(input_file, output_file, start_time, end_time):
    ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_file)

# Example usage
input_file = r'C:\Users\zglum\OneDrive\Desktop\PictoprimeVideo\exemples\Magaru\magaru_full.mp4'  # Path to the input video file
output_file = r'C:\Users\zglum\OneDrive\Desktop\PictoprimeVideo\exemples\Magaru\bagaru_cut.mp4'  # Path to the output video file
start_time = 0  # Start time in seconds
end_time = 6  # End time in seconds

cut_video(input_file, output_file, start_time, end_time)
