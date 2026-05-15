
import os
import shutil
import subprocess

n = 10

original_file = "data.bin"

with open(original_file, "wb") as f:
    f.write(b"0" * 1024 * 1024 * 100)

print(f"Created: {original_file}")


copies = []

for i in range(1, n):
    copy_name = f"copy_{i}.bin"
    shutil.copy(original_file, copy_name)
    copies.append(copy_name)

print(f"Created {n} files")


archive_name = "final_bundle.7z"

files_to_compress = [original_file] + copies

command = [
    "7z",
    "a",
    "-t7z",
    "-mx=9",         
    "-m0=lzma2",     
    "-ms=on",        
    archive_name,
] + files_to_compress

subprocess.run(command, check=True)

print(f"Created archive: {archive_name}")


os.remove(original_file)

for file in copies:
    os.remove(file)

print("Deleted source files")

print("Done")