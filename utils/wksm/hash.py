import os
import subprocess


def process_sha(hash):
    return subprocess.check_output(["git", "diff", hash]).decode()