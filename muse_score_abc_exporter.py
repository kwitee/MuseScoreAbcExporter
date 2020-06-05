import os
import subprocess
import sys

muse_score_path = sys.argv[1]
muse_score_file_path = sys.argv[2]
music_xml_file_path = F"{os.path.splitext(muse_score_file_path)[0]}.musicxml"
output_dir = os.path.dirname(os.path.abspath(muse_score_file_path))

print("Exporting muse score file to musicxml format...")
subprocess.call([muse_score_path, muse_score_file_path, "--export-to", music_xml_file_path])

print("Converting musicxml format to abc...")
subprocess.call([sys.executable, "xml2abc\\xml2abc.py", music_xml_file_path, "-o", output_dir])

print("Removing musicxml file...")
os.remove(music_xml_file_path)
