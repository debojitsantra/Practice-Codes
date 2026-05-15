import os
from mutagen import File


FOLDER_PATH = 'Music' 
OUTPUT_FILE = 'songs.txt'


AUDIO_EXTENSIONS = ['.mp3', '.flac', '.m4a', '.wav', '.opus']

def get_song_info(file_path):
    try:
        audio = File(file_path, easy=True)
        if audio is None:
            return None
        title = audio.get('title', [None])[0]
        artist = audio.get('artist', [None])[0]
        if title and artist:
            return f"{title} - {artist}"
        elif title:
            return title
        else:
            return None
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def main():
    songs = []
    for filename in os.listdir(FOLDER_PATH):
        filepath = os.path.join(FOLDER_PATH, filename)
        ext = os.path.splitext(filename)[1].lower()
        if os.path.isfile(filepath) and ext in AUDIO_EXTENSIONS:
            song_info = get_song_info(filepath)
            if song_info:
                songs.append(song_info)
            else:
                songs.append(f"Unknown title in {filename}")


    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        for song in songs:
            f.write(song + '\n')
    
    print(f"✅ Done! Song list saved to '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    main()