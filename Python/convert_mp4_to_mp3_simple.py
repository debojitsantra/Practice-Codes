from moviepy.video.io.VideoFileClip import VideoFileClip

def mp4_to_mp3(input_file, output_file=None):
    if not output_file:
        output_file = input_file.rsplit('.', 1)[0] + '.mp3'
    
    video = VideoFileClip(input_file)
    video.audio.write_audiofile(output_file)
    print(f"Conversion complete: {output_file}")


k = input("enter file name")

mp4_to_mp3(k)