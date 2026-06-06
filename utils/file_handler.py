import os
import shutil
from pathlib import Path

class FileHandler:
    def __init__(self, base_dir: str = "data"):
        self.base_dir = Path(base_dir)

    def save_upload(self, file_content: bytes, filename: str) -> Path:
        upload_path = self.base_dir / "uploads" / filename
        with open(upload_path, "wb") as f:
            f.write(file_content)
        return upload_path

    def clean_directory(self, directory_name: str):
        target_dir = self.base_dir / directory_name
        if target_dir.exists() and target_dir.is_dir():
            for filename in os.listdir(target_dir):
                file_path = target_dir / filename
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception:
                    pass

    def delete_file(self, filepath: str | Path):
        path = Path(filepath)
        if path.exists():
            path.unlink()
