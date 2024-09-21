import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            # filepath.name takes only the filename as the filepath and removes everything before that
            archive.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    print("This is the backend module for creating a zip file.")

