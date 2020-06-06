import sys

from common import *


def main(muse_score_path, directory_path):
    muse_score_export(muse_score_path, directory_path, OutputFormat.pdf)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
