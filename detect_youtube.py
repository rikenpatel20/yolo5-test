import os
from pytube import YouTube
import subprocess

# Function to download YouTube video
def download_youtube_video(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
    stream.download(output_path=output_path, filename='input_video.mp4')
    return os.path.join(output_path, 'input_video.mp4')

# Function to run YOLOv5 inference
def run_yolov5_inference(video_path):
    command = [
        'python', 'detect.py',
        '--weights', 'runs/train/exp/weights/best.pt',
        '--img', '640',
        '--conf', '0.25',
        '--source', video_path,
        '--save-txt',
        '--save-conf',
        '--save-crop'
    ]
    subprocess.run(command)

# Main function
if __name__ == '__main__':
    # YouTube video URL
    # https://www.youtube.com/watch?v=y0kmA9zLvRo
    # https://www.youtube.com/watch?v=XFYc23Ii-7Y
    # https://www.youtube.com/watch?v=rZD1aqiViwo
    # https://www.youtube.com/watch?v=C50QMeYl8j8
    youtube_url = 'https://www.youtube.com/watch?v=y0kmA9zLvRo'
    output_path = '.'  # Current directory

    # Step 1: Download the YouTube video
    video_path = download_youtube_video(youtube_url, output_path)
    print(f'Downloaded video to {video_path}')

    # Step 2: Run YOLOv5 inference on the downloaded video
    run_yolov5_inference(video_path)
    print('YOLOv5 inference completed')
