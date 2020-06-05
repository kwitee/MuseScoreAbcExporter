import os
import subprocess
import sys

muse_score_path = sys.argv[1]
muse_score_file_path = sys.argv[2]
music_xml_file_path = F"{os.path.splitext(muse_score_file_path)[0]}.musicxml"

subprocess.call([muse_score_path, muse_score_file_path, "--export-to", music_xml_file_path])
