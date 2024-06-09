import glob
import os
import importlib
import logging
from os.path import dirname, isfile, join, abspath
import subprocess
from config import EXTRA_PLUGINS, EXTRA_PLUGINS_REPO, EXTRA_PLUGINS_FOLDER

ROOT_DIR = abspath(join(dirname(__file__), "..", ".."))
EXTERNAL_REPO_PATH = join(ROOT_DIR, EXTRA_PLUGINS_FOLDER)

# Convert EXTRA_PLUGINS to a boolean
extra_plugins_enabled = EXTRA_PLUGINS.lower() == "true"

if extra_plugins_enabled:
    if not os.path.exists(EXTERNAL_REPO_PATH):
        with open(os.devnull, "w") as devnull:
            clone_result = subprocess.run(
                ["git", "clone", EXTRA_PLUGINS_REPO, EXTERNAL_REPO_PATH],
                stdout=devnull,
                stderr=subprocess.PIPE,
            )
            if clone_result.returncode != 0:
                logging.exception(clone_result.stderr.decode())

    requirements_path = join(EXTERNAL_REPO_PATH, "requirements.txt")
    if os.path.isfile(requirements_path):
        with open(os.devnull, "w") as devnull:
            install_result = subprocess.run(
                ["pip", "install", "-r", requirements_path],
                stdout=devnull,
                stderr=subprocess.PIPE,
            )
            if install_result.returncode != 0:
                logging.exception(install_result.stderr.decode())


def __list_all_modules():
    main_repo_plugins_dir = dirname(__file__)
    work_dirs = [main_repo_plugins_dir]

    if extra_plugins_enabled:
        work_dirs.append(EXTERNAL_REPO_PATH)

    all_modules = []

    for work_dir in work_dirs:
        mod_paths = glob.glob(join(work_dir, "*.py"))
        mod_paths += glob.glob(join(work_dir, "*/*.py"))

        modules = [
            (
                (
                    (f.replace(main_repo_plugins_dir, "VIPMUSIC.plugins")).replace(
                        EXTERNAL_REPO_PATH, EXTRA_PLUGINS_FOLDER
                    )
                ).replace(os.sep, ".")
            )[:-3]
            for f in mod_paths
            if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
        ]
        all_modules.extend(modules)

    return all_modules


ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]
