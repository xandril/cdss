import os
from pathlib import Path

ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent

WEIGHTS_PATHS: list[Path] = [ROOT_DIR / 'model' / '5_6_7.pt', ROOT_DIR / 'model' / '0_1_3.pt']
