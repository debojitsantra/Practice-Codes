import os
from tinytag import TinyTag

MUSIC_FOLDER = r"Lowres"   
OUTPUT_FILE = r"2songs_list.txt"

def collect_songs(folder):
    songs = []
    for root, _, files in os.walk(folder):
        for name in files:

            if not name.lower().endswith((".mp3", ".m4a", ".flac", ".wav", ".ogg", ".wma")):
                continue

            filepath = os.path.join(root, name)
            try:
                tag = TinyTag.get(filepath)
                title = tag.title or os.path.splitext(name)[0]
                artist = tag.artist or "Unknown Artist"
                songs.append(f"{artist} - {title}")
            except Exception as e:

                title = os.path.splitext(name)[0]
                songs.append(f"{title} - Unknown Artist")
    return songs

def main():
    songs = collect_songs(MUSIC_FOLDER)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for line in songs:
            f.write(line + "  \n" )

if __name__ == "__main__":
    main()
