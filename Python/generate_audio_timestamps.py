import os
from tinytag import TinyTag


MEDIA_FOLDER = r"Audio"
FADE_SECONDS = 3                       


EXTS = (
    ".mp3", ".flac", ".wav", ".ogg", ".opus", ".m4a", ".aac", ".wma",
    ".mp4", ".mkv", ".mov"  
)

def tag(path):
    try:
        return TinyTag.get(path)
    except:
        return None

def time_fmt(sec):
    sec = int(sec)
    m,s = divmod(sec,60)
    h,m = divmod(m,60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"

def clean_name(path, tagdata):
    filename = os.path.splitext(os.path.basename(path))[0]
    if not tagdata: return filename
    a = (tagdata.artist or "").strip()
    t = (tagdata.title  or "").strip()
    if a and t: return f"{a}-{t}"
    if t: return t
    if a: return a
    return filename

def main():

    files = sorted([
        os.path.join(MEDIA_FOLDER,f)
        for f in os.listdir(MEDIA_FOLDER)
        if f.lower().endswith(EXTS)
    ])

    if not files:
        print("No media files found in folder.")
        return

    print(f"Scanning: {MEDIA_FOLDER}")
    print(f"Crossfade applied: {FADE_SECONDS} seconds\n")

    mix_time = 0.0
    out_lines = []
    first = True

    for f in files:
        info = tag(f)
        if not info or not info.duration:
            print(f"Skipping (no duration): {f}")
            continue

        timestamp = time_fmt(mix_time)
        name = clean_name(f, info)
        out_lines.append(f"{timestamp} {name}")
        print(f"{timestamp}  {name}")

        advance = info.duration - FADE_SECONDS
        if advance < 0: advance = 0
        mix_time += advance

    with open("timestamps.txt","w",encoding="utf-8") as txt:
        txt.write("\n".join(out_lines))

    print("\nSaved → timestamps.txt")

if __name__ == "__main__":
    main()