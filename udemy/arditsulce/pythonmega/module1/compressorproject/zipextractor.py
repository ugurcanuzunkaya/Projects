import zipfile
import pathlib
import os
from zipcreator import make_archive


def change_dir_to_this_file():
    # getting into the current working directory
    cwd = os.getcwd()
    path_of_this_file = pathlib.Path(__file__).parent
    if cwd != path_of_this_file:
        os.chdir(path_of_this_file)

    if not os.path.exists("dest"):
        os.mkdir("dest")


def extract_archive(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, "r") as zipf:
        zipf.extractall(dest_dir)
    print("Extraction completed!")


if __name__ == "__main__":
    change_dir_to_this_file()
    if not os.path.exists("dest/archive.zip"):
        make_archive(filepaths=["zipcreator.py"], dest_dir="dest")
    extract_archive(archive_path="dest/archive.zip", dest_dir="extracted")
