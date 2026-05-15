import os
from mutagen import File


music_folder = "/storage/6FDF-A3E6/Music/Hires"
output_file = "songs_list.txt"


music_extensions = ['.mp3', '.flac', '.wav', '.ogg', '.m4a', '.aac']

def get_song_title(filepath):
    audio = File(filepath, easy=True)
    if audio:
        title = audio.get("title", [None])[0]
        artist = audio.get("artist", [None])[0]
        if title and artist:
            return f"{artist} - {title}"
        elif title:
            return title

    return os.path.splitext(os.path.basename(filepath))[0]

songs = []

for root, _, files in os.walk(music_folder):
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in music_extensions:
            full_path = os.path.join(root, file)
            song_info = get_song_title(full_path)
            songs.append(song_info)


with open(output_file, "w", encoding="utf-8") as f:
    for song in songs:
        f.write(song + "\n")

print(f"Song list saved to {output_file}")