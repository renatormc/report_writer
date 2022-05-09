from __future__ import absolute_import
from pathlib import Path
from typing import Union
import os
import zipfile
import shutil
from report_writer.config import TEMPFOLDER
from uuid import uuid4


def zip_folder(folder_path: str|Path, output_path: str|Path) -> None:
    folder_path, output_path = str(folder_path), str(output_path)
    print(folder_path, output_path)
    contents = os.walk(folder_path)
    try:
        zip_file = zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED)
        for root, folders, files in contents:
            for folder_name in folders:
                if folder_name == "__pycache__":
                    continue
                absolute_path = os.path.join(root, folder_name)
                relative_path = absolute_path.replace(folder_path + os.sep, '')
                zip_file.write(absolute_path, relative_path)
            for file_name in files:
                absolute_path = os.path.join(root, file_name)
                if "__pycache__" in absolute_path:
                    continue
                relative_path = absolute_path.replace(folder_path + os.sep, '')

                zip_file.write(absolute_path, relative_path)
    finally:
        zip_file.close()


def unzip_file(file: Path | str, dest: Path | str | None = None, subfolder=False) -> Path:
    """Unzip a zip file to a folder. If dest is not especified it will be extracted to a temporary folder"""
    if dest is None:
        dest = TEMPFOLDER / str(uuid4())
    file, dest = Path(file), Path(dest)
    if dest.exists():
        shutil.rmtree(dest)
    if subfolder:
        dest = dest / file.name
    dest.mkdir(parents=True)

    with zipfile.ZipFile(str(file)) as zip_ref:
        zip_ref.extractall(str(dest))
    return dest
