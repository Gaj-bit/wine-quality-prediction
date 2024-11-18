import os
from pathlib import Path

project_name = "wine-quality"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/main.py",
    f"src/{project_name}/__init__.py",
    "setup.py",
    f"config",
    f"notebooks/EDA_{project_name}.ipynb",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
