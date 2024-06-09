import os
import shutil
from ..logging import LOGGER
from config import EXTRA_PLUGINS_FOLDER


def dirr():
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
        elif file.endswith(".jpeg"):
            os.remove(file)
        elif file.endswith(".png"):
            os.remove(file)

    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")

    if EXTRA_PLUGINS_FOLDER in os.listdir():
        shutil.rmtree(EXTRA_PLUGINS_FOLDER)

    LOGGER(__name__).info("Directories Updated.")
