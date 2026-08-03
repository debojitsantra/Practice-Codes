import os
import subprocess
from pathlib import Path


AUDIO_VIDEO_EXTS = {
    ".flac", ".wav", ".aac", ".m4a", ".ogg", ".wma", ".aiff", ".alac",
    ".mp4", ".mkv", ".avi", ".mov", ".webm", ".flv", ".wmv", ".mpeg", ".mpg"
}

BITRATE = "192k"   

def convert_to_mp3(input_path: Path):
    output_path = input_path.with_suffix(".mp3")

   
    if output_path.exists():
        print(f"✅ Skipping (already exists): {output_path}")
        return

    print(f"🎵 Converting: {input_path}  -->  {output_path}")

    cmd = [
        "ffmpeg",
        "-y",                      
        "-i", str(input_path),
        "-vn",                     
        "-acodec", "libmp3lame",
        "-b:a", BITRATE,
        str(output_path)
    ]

    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"✅ Done: {output_path}")
    except subprocess.CalledProcessError:
        print(f"❌ Failed: {input_path}")

def convert_folder(folder_path: str):
    folder = Path(folder_path)

    if not folder.exists():
        print("❌ Folder not found!")
        return

    for root, _, files in os.walk(folder):
        for file in files:
            file_path = Path(root) / file
            ext = file_path.suffix.lower()

            if ext in AUDIO_VIDEO_EXTS:
                convert_to_mp3(file_path)

if __name__ == "__main__":
    folder_path = input("📂 Enter folder path: ").strip().strip('"')
    convert_folder(folder_path)
    print("\n🔥 All conversions finished!")