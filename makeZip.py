import zipfile
import os

def create_zip(zip_filename, files_to_zip):
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in files_to_zip:
            if os.path.isfile(file):
                zipf.write(file, arcname=os.path.basename(file))
                print(f"Added: {file}")
            else:
                print(f"Skipped (not found): {file}")

# Example usage
files = ["README.txt", "13ColoniesAdif.exe"]
create_zip("13ColoniesAdif-1.0.zip", files)
