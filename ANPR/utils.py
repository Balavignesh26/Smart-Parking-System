import os

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

ensure_directory_exists("data/")
ensure_directory_exists("models/")
