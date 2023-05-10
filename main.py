from vina import Vina
from pathlib import Path
from typing import List

v = Vina()

BASE_DIR: Path = Path(__file__).resolve().parent

SAMPLES_DIR: Path = BASE_DIR.joinpath('samples')

ligand_files: List[str] = [SAMPLES_DIR.joinpath(name).__str__() for name in
                           ["RCX_otimizado.pdbqt", "StaphylionosideA.pdbqt"]]

for file in ligand_files:
    v.set_receptor(SAMPLES_DIR.joinpath("Only_prot.pdbqt").__str__())
    v.set_ligand_from_file(file)
    v.compute_vina_maps([22.854, 2.545, 30.487], [30, 30, 30])
    v.dock(exhaustiveness=16)
    path_to_save = BASE_DIR.joinpath(f"results/{Path(file).stem}-results.pdbqt").__str__()
    v.write_poses(path_to_save)
