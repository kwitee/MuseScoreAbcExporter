import sys

from common import *


def convert_to_abc(directory_path):
    subprocess_arguments = [sys.executable, "xml2abc\\xml2abc.py"]

    for file_name in os.listdir(directory_path):
        if file_name.endswith(".musicxml"):
            subprocess_arguments.append(os.path.join(directory_path, file_name))

    subprocess_arguments.append("-o")
    subprocess_arguments.append(directory_path)
    subprocess.call(subprocess_arguments)


def clean_temporary_files(directory_path):
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".musicxml"):
            os.remove(os.path.join(directory_path, file_name))


def main(muse_score_path, directory_path):
    muse_score_export(muse_score_path, directory_path, OutputFormat.music_xml)
    convert_to_abc(directory_path)
    clean_temporary_files(directory_path)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
