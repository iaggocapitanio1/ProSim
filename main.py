from typing import List

import settings
from utilities.functions import process_file

ligand_files: List[str] = [settings.SAMPLES_DIR.joinpath(name).__str__() for name in
                           ["RCX_otimizado.pdbqt", "StaphylionosideA.pdbqt"]]

if __name__ == "__main__":

    for file in ligand_files:
        process_file(file)
