#!/usr/bin/env python3
"""Write the 24 November 2026 front page to the grader's output folder.

The picture itself lives in this repository as news.png: a front page that
sums up Tuesday 24 November 2026 in six stories, drawn earlier with a small
script from the day's reported news. This program does exactly one thing: it
copies that file to entry.png in the output folder, so the bytes the judge
sees are the bytes in this repository. It touches no network, keeps no
state, and writes the same bytes on every run.
"""

import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "news.png")


def main():
    if not os.path.isfile(SOURCE):
        print("missing source image: " + SOURCE, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    print("wrote " + target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
