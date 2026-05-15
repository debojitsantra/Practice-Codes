import os
from pydub import AudioSegment


SOURCE_DIR = "flac"           
OUTPUT_DIR = "Musicmp3"       
BITRATE = "192k"               


def convert_flac_to_mp3():
    for root, _, files in os.walk(SOURCE_DIR):
        for file in files:
            if file.lower().endswith(".flac"):
                flac_path = os.path.join(root, file)

             
                relative_path = os.path.relpath(root, SOURCE_DIR)
                mp3_folder = os.path.join(OUTPUT_DIR, relative_path)
                os.makedirs(mp3_folder, exist_ok=True)

                mp3_path = os.path.join(
                    mp3_folder,
                    file.replace(".flac", ".mp3")
                )

                if os.path.exists(mp3_path):
                    print(f"Skipping (already exists): {mp3_path}")
                    continue

                print(f"Converting: {flac_path}")
                audio = AudioSegment.from_file(flac_path, format="flac")
                audio.export(mp3_path, format="mp3", bitrate=BITRATE)

    print("\n✅ Conversion complete. Originals untouched.")

if __name__ == "__main__":
    convert_flac_to_mp3()

