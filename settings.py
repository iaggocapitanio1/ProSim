from pathlib import Path
import os

BASE_DIR: Path = Path(__file__).resolve().parent

SAMPLES_DIR: Path = Path(os.environ.get("SAMPLES_DIR", BASE_DIR.joinpath('samples')))

RESULT_DIR: Path = Path(os.environ.get("RESULTS_DIR", BASE_DIR.joinpath('results')))


