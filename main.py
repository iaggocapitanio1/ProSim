from typing import List

from vina import Vina

import settings
from utilities.functions import process_file

v = Vina()

ligand_files: List[str] = [settings.SAMPLES_DIR.joinpath(name).__str__() for name in
                           ["RCX_otimizado.pdbqt", "StaphylionosideA.pdbqt"]]

if __name__ == "__main__":
    settings.SAMPLES_DIR.mkdir(parents=True, exist_ok=True)
    settings.RESULT_DIR.mkdir(parents=True, exist_ok=True)

    for file in ligand_files:
        process_file(file)
