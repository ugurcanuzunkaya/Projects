import pathlib
import zipfile
import os


def change_dir_to_this_file():
    # getting the current working directory
    cwd = os.getcwd()
    path_of_this_file = pathlib.Path(__file__).parent
    if cwd != path_of_this_file:
        os.chdir(path_of_this_file)

    if not os.path.exists("dest"):
        os.mkdir("dest")


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "archive.zip")
    with zipfile.ZipFile(dest_path, "w") as zipf:
        for file in filepaths:
            filepath = pathlib.Path(file)
            zipf.write(file, arcname=filepath.name)
    print("Archive created!")


if __name__ == "__main__":
    change_dir_to_this_file()
    make_archive(filepaths=["zipcreator.py"], dest_dir="dest")
