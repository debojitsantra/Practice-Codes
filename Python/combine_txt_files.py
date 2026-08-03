import os

folder_path = "/storage/6FDF-A3E6/Music"  
output_file = "combined.txt"

with open(output_file, "w", encoding="utf-8") as outfile:
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())
                outfile.write("\n\n")  

print("All text files combined successfully.")