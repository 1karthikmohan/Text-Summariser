import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO , format = '[%(asctime)s] : %(message)s:')

project_name = "text-summarizer"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/_init _. py",
    f"src/{project_name}/conponents/_init _. py",
    f"src/{project_name}/utils/_init _. py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/_init _. py",
    f"src/{project_name}/config/_init _. py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/_init _. py",
    f"src/{project_name}/entity/_init _. py",
    f"src/{project_name}/constants/_init _. py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb" 
]

for file in list_of_files:
    file_path = Path(file)
    filedir,filename = os.path.split(file_path)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, 'w') as f:
            pass
        logging.info(f"Creating file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}")
