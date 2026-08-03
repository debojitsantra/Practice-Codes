import os
from pathlib import Path
from typing import List, Tuple

from pydub import AudioSegment
from tinytag import TinyTag 


INPUT_FOLDER = "Audio"  
OUTPUT_AUDIO = "mixed_output.mp3"
OUTPUT_TIMESTAMPS = "timestamps.txt"

AUDIO_EXTENSIONS = (".mp3", ".wav", ".flac", ".ogg", ".m4a")

CROSSFADE_SECONDS = 3.0
PER_TRACK_FADE_OUT_MS = 5000



def get_audio_files(folder: str) -> List[Path]:
    folder_path = Path(folder)
    if not folder_path.exists():
        raise FileNotFoundError(f"Input folder does not exist: {folder}")

    files = [
        f for f in sorted(folder_path.iterdir())
        if f.is_file() and f.suffix.lower() in AUDIO_EXTENSIONS
    ]
    return files


def format_timestamp(ms: int) -> str:
    total_seconds = ms // 1000
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes}:{seconds:02d}"


def get_track_label(path: Path) -> str:
    """
    Build a label like: ArtistName-AudioTitle

    Falls back to filename if tags are missing / unreadable.
    """
    try:
        tag = TinyTag.get(str(path))
        title = (tag.title or path.stem).strip()
        artist = (tag.artist or "Unknown Artist").strip()

        return f"{artist}-{title}"
    except Exception:

        return path.stem


def join_songs_with_crossfade(
    folder: str,
    output_audio: str,
    output_timestamps: str,
    crossfade_seconds: float = 5.0,
) -> None:
    audio_files = get_audio_files(folder)

    if not audio_files:
        print("No audio files found in the folder.")
        return

    print(f"Found {len(audio_files)} audio files:")
    for f in audio_files:
        print(" -", f.name)

    crossfade_ms_default = int(max(0.0, crossfade_seconds) * 1000)

    mixed: AudioSegment = None
    timestamps: List[Tuple[int, str]] = []
    current_mix_length_ms = 0

    for index, audio_path in enumerate(audio_files):
        print(f"\nLoading track {index + 1}/{len(audio_files)}: {audio_path.name}")
        segment = AudioSegment.from_file(audio_path)


        fade_out_ms = min(PER_TRACK_FADE_OUT_MS, len(segment))
        if fade_out_ms > 0:
            segment = segment.fade_out(fade_out_ms)


        title = get_track_label(audio_path)

        if mixed is None:

            start_time_ms = 0
            timestamps.append((start_time_ms, title))

            mixed = segment
            current_mix_length_ms = len(mixed)
            print(f" -> Start time: {format_timestamp(start_time_ms)} [{title}]")
        else:
            crossfade_ms = min(
                crossfade_ms_default,
                len(segment),
                current_mix_length_ms
            )

            start_time_ms = current_mix_length_ms - crossfade_ms
            timestamps.append((start_time_ms, title))
            print(
                f" -> Start time: {format_timestamp(start_time_ms)} "
                f"(crossfade {crossfade_ms} ms) [{title}]"
            )

            mixed = mixed.append(segment, crossfade=crossfade_ms)
            current_mix_length_ms = len(mixed)


    output_path = Path(output_audio)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"\nExporting mixed audio to: {output_audio}")
    mixed.export(output_audio, format=output_path.suffix.lstrip(".") or "mp3")


    print(f"Writing timestamps to: {output_timestamps}")
    with open(output_timestamps, "w", encoding="utf-8") as f:
        for start_ms, title in timestamps:
            ts_str = format_timestamp(start_ms)
            line = f"{ts_str} {title}\n"
            f.write(line)

    print("\nDone!")
    print("Example timestamps:")
    with open(output_timestamps, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            print(" ", line.strip())
            if i >= 4:
                break


if __name__ == "__main__":
    join_songs_with_crossfade(
        folder=INPUT_FOLDER,
        output_audio=OUTPUT_AUDIO,
        output_timestamps=OUTPUT_TIMESTAMPS,
        crossfade_seconds=CROSSFADE_SECONDS,
    )