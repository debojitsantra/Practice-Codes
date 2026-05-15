import os
from pydub import AudioSegment


input_formats = ('.m4a', '.opus')


folder_path = input("Enter the folder path: ").strip()


for root, _, files in os.walk(folder_path):
    for file in files:
        if file.lower().endswith(input_formats):
            file_path = os.path.join(root, file)
            file_name, ext = os.path.splitext(file)
            new_file_path = os.path.join(root, f"{file_name}.mp3")

            try:
                print(f"Converting {file_path} -> {new_file_path}")
                audio = AudioSegment.from_file(file_path)
                audio.export(new_file_path, format="mp3")
                os.remove(file_path)
                print(f"Done and deleted original: {file_path}")
            except Exception as e:
                print(f"Failed to convert {file_path}: {e}")