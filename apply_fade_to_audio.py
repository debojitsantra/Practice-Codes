import argparse
import os
from pydub import AudioSegment

def fade_and_save(file_path, fade_in_ms, fade_out_ms, output_path):

    song = AudioSegment.from_file(file_path)
    
  
    faded_song = song.fade_in(fade_in_ms).fade_out(fade_out_ms)

    
    faded_song.export(output_path, format="mp3")
    print(f" Saved faded audio as: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="🎧 Apply fade-in/out and save as MP3")
    parser.add_argument("file", help="Input audio file (.mp3, .wav, .flac, etc.)")
    parser.add_argument("--fadein", type=int, default=1000, help="Fade-in duration in milliseconds")
    parser.add_argument("--fadeout", type=int, default=1000, help="Fade-out duration in milliseconds")
    parser.add_argument("--output", help="Output filename (default: inputname_faded.mp3)")

    args = parser.parse_args()

   
    if args.output:
        output_path = args.output
    else:
        base, _ = os.path.splitext(args.file)
        output_path = f"{base}_faded.mp3"

    fade_and_save(args.file, args.fadein, args.fadeout, output_path)

if __name__ == "__main__":
    main()