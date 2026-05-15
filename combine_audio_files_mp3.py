from pydub import AudioSegment
import os

def combine_audio_files(input_folder, output_file):
  
    supported_formats = ['.flac', '.mp3', '.m4a']
    
    
    silence = AudioSegment.silent(duration=2000) 
    
   
    combined = AudioSegment.empty()
    
    
    audio_files = [f for f in os.listdir(input_folder) 
                  if os.path.splitext(f)[1].lower() in supported_formats]
    
    if not audio_files:
        print("No supported audio files found in the folder.")
        return
    
    
    audio_files.sort()
    
    
    for i, file in enumerate(audio_files):
        file_path = os.path.join(input_folder, file)
        print(f"Processing: {file}")
        
        try:
            
            audio = AudioSegment.from_file(file_path)
            
            
            combined += audio
            
            
            if i < len(audio_files) - 1:
                combined += silence
                
        except Exception as e:
            print(f"Error processing {file}: {str(e)}")
            continue
    
    if len(combined) > 0:
       
        combined.export(output_file, format="mp3", bitrate="192k")
        print(f"Combined audio saved as: {output_file}")
    else:
        print("No audio files were successfully processed.")

def main():
   
    input_folder = input("Enter the path to the folder containing audio files: ")
    output_file = "combined_output.mp3"
    
   
    if not os.path.isdir(input_folder):
        print("Invalid folder path.")
        return
    
    combine_audio_files(input_folder, output_file)

if __name__ == "__main__":
    main()