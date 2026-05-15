import os
import subprocess
from pathlib import Path


SOURCE_FOLDER = "mp4"  
OUTPUT_FOLDER = "conv" 


AUDIO_CODEC = "flac"
FLAC_COMPRESSION_LEVEL = "0" 



def convert_mp4_to_flac(mp4_path: Path, flac_path: Path):
    """
    Runs ffmpeg to convert mp4->flac with best quality.
    """
    cmd = [
        "ffmpeg",
        "-y",                         
        "-i", str(mp4_path),         
        "-vn",                        
        "-c:a", AUDIO_CODEC,         
        "-compression_level", FLAC_COMPRESSION_LEVEL,
        str(flac_path)
    ]


    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Failed: {mp4_path.name}")
        print(result.stderr.strip())
    else:
        print(f"✅ Converted: {mp4_path.name} → {flac_path.name}")

def main():
    source = Path(SOURCE_FOLDER)
    if not source.is_dir():
        print(f"ERROR: folder not found: {SOURCE_FOLDER}")
        return


    if OUTPUT_FOLDER:
        out_base = Path(OUTPUT_FOLDER)
        out_base.mkdir(parents=True, exist_ok=True)
    else:
        out_base = source

    mp4_files = list(source.glob("*.mp4"))
    if not mp4_files:
        print("No .mp4 files found in", SOURCE_FOLDER)
        return

    print(f"Found {len(mp4_files)} MP4 files. Starting conversion...")

    for mp4 in mp4_files:
        flac_name = mp4.stem + ".flac"
        flac_file = out_base / flac_name


        if flac_file.exists():
            print(f"⚠️  Already exists, skipping: {flac_name}")
            continue

        convert_mp4_to_flac(mp4, flac_file)

    print("🎉 All done!")

if __name__ == "__main__":
    main()