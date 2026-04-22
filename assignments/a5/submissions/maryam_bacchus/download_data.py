import os
import urllib.request


def download_instruction_data(filename="instruction-data.json"):
    url = (
        "https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/main/ch07/01_main-chapter-code/instruction-data.json"
    )
    if not os.path.exists(filename):
        print("Downloading instruction data...")
        urllib.request.urlretrieve(url, filename)
    return filename
