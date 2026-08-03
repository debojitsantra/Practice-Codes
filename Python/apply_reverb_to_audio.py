import argparse
import os
import subprocess
from pydub import AudioSegment
import tempfile

REVERB_MAP = {
    "auditorium": "reverb 50",
    "echo": "echo 0.8 0.88 60 0.4",
    "great hall": "reverb 90",
    "light reverb": "reverb 20",
    "scene": "reverb 30",
    "small room": "reverb 10",
    "stadium": "reverb 100",
    "studio": "reverb 40"
}

def apply_fade(input_file, fadein, fadeout):
    audio = AudioSegment.from_file(input_file)
    faded = audio.fade_in(fadein).fade_out(fadeout)

    temp_wav = tempfile.mktemp(suffix=".wav")
    faded.export(temp_wav, format="wav")
    return temp_wav

def apply_reverb(input_file, effect_name, output_file):
    effect = REVERB_MAP.get(effect_name.lower())
    if not effect:
        raise ValueError(f"Unknown reverb effect: {effect_name}")
    
    cmd = f"sox \"{input_file}\" \"{output_file}\" {effect}"
    subprocess.run(cmd, shell=True, check=True)

def convert_to_mp3(input_wav, output_mp3):
    AudioSegment.from_file(input_wav).export(output_mp3, format="mp3")

def main():
    parser = argparse.ArgumentParser(description="🎵 Add fade and reverb to audio")
    parser.add_argument("input", help="Input audio file (mp3, wav, etc.)")
    parser.add_argument("--fadein", type=int, default=1000, help="Fade-in in ms")
    parser.add_argument("--fadeout", type=int, default=1000, help="Fade-out in ms")
    parser.add_argument("--reverb", choices=[k.lower() for k in REVERB_MAP.keys()], required=True, help="Reverb preset name")
    parser.add_argument("--output", default="output_reverb.mp3", help="Output MP3 file")

    args = parser.parse_args()

    print(" Applying fade...")
    faded_wav = apply_fade(args.input, args.fadein, args.fadeout)

    print(f" Applying reverb: {args.reverb}")
    reverbed_wav = tempfile.mktemp(suffix=".wav")
    apply_reverb(faded_wav, args.reverb, reverbed_wav)

    print(f" Saving MP3: {args.output}")
    convert_to_mp3(reverbed_wav, args.output)

    print(" Done!")

if __name__ == "__main__":
    main()