from pathlib import Path
from datetime import datetime

DATA_DIR = Path('data')
DATA_DIR.mkdir(exist_ok=True)

def save_file(filename: str, file_bytes: bytes) -> Path:
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    path = DATA_DIR / f'{timestamp}_{filename}'
    with open(path, 'wb') as f:
        f.write(file_bytes)
    return path
