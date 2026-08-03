import os
import threading
import yt_dlp
import tkinter as tk
from tkinter import ttk, messagebox


output_dir = "Downloaded_Songs"
os.makedirs(output_dir, exist_ok=True)
song_list_file = "songs_list.txt"


with open(song_list_file, "r", encoding="utf-8") as f:
    songs = [line.strip() for line in f if line.strip()]


def get_ydl_opts(song_name):
    return {
        'format': 'bestaudio[ext=m4a]/bestaudio[ext=webm]',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
        'postprocessors': [],
        'match_filter': yt_dlp.utils.match_filter_func('!is_video')
    }


root = tk.Tk()
root.title("Song Downloader")
root.geometry("400x120")

song_var = tk.StringVar()
progress = ttk.Progressbar(root, maximum=len(songs), length=380)
label = tk.Label(root, textvariable=song_var)
button = ttk.Button(root, text="Start Download")

label.pack(pady=10)
progress.pack(pady=5)
button.pack(pady=5)

def download_all():
    button.config(state=tk.DISABLED)
    for index, song in enumerate(songs):
        song_var.set(f"Downloading: {song}")
        progress["value"] = index
        root.update_idletasks()
        try:
            with yt_dlp.YoutubeDL(get_ydl_opts(song)) as ydl:
                ydl.download([f"ytsearch1:{song}"])
        except Exception as e:
            print(f"Failed: {song} -> {e}")
    song_var.set("All downloads complete!")
    progress["value"] = len(songs)
    button.config(state=tk.NORMAL)


def start_thread():
    thread = threading.Thread(target=download_all)
    thread.start()

button.config(command=start_thread)

root.mainloop()