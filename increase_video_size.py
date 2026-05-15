import subprocess
import os

def increase_video_size(input_path):
    if not os.path.isfile(input_path):
        print("File not found:", input_path)
        return


    base, ext = os.path.splitext(input_path)
    output_path = f"{base}_bigger{ext}"


    if ext.lower() == '.webm':
        video_codec = 'libvpx-vp9'
        audio_codec = 'libopus'
        bitrate = '6M'
    else:
        video_codec = 'libx264'
        audio_codec = 'aac'
        bitrate = '10M'

    command = [
        'ffmpeg',
        '-i', input_path,
        '-vf', 'scale=iw*1.5:ih*1.5',
        '-b:v', bitrate,
        '-c:v', video_codec,
        '-c:a', audio_codec,
        '-preset', 'slow',
        output_path
    ]

    print("Increasing video size...")
    subprocess.run(command)
    print("Done! Saved as", output_path)


increase_video_size("video.webm") 
