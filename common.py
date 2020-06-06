import os
import subprocess
from enum import Enum


class OutputFormat(Enum):
    music_xml = "musicxml"
    pdf = "pdf"


def muse_score_export(muse_score_path: str, directory_path: str, output_format: OutputFormat):

    for file_name in os.listdir(directory_path):
        if file_name.endswith(".mscz"):
            file_path = os.path.join(directory_path, file_name)
            output_file_path = F"{os.path.splitext(file_path)[0]}.{OutputFormat(output_format).value}"
            subprocess.call([muse_score_path, file_path, "--export-to", output_file_path])
