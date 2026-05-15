import os
from pydub import AudioSegment


SOURCE_DIR = "/storage/6FDF-A3E6/Music/Lowres"         
OUTPUT_DIR = "Music_mp3/Lowres"       
BITRATE = "128k"                


def convert_flac_to_mp3():
    for root, _, files in os.walk(SOURCE_DIR):
        for file in files:
            if file.lower().endswith(".m4a"):
                flac_path = os.path.join(root, file)


                relative_path = os.path.relpath(root, SOURCE_DIR)
                mp3_folder = os.path.join(OUTPUT_DIR, relative_path)
                os.makedirs(mp3_folder, exist_ok=True)

                mp3_path = os.path.join(
                    mp3_folder,
                    file.replace(".m4a", ".mp3")
                )

                if os.path.exists(mp3_path):
                    print(f"Skipping (already exists): {mp3_path}")
                    continue

                print(f"Converting: {flac_path}")
                audio = AudioSegment.from_file(flac_path, format="m4a")
                audio.export(mp3_path, format="mp3", bitrate=BITRATE)

    print("\n✅")

if __name__ == "__main__":
    convert_flac_to_mp3()
