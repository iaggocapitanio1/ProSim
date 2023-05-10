from pathlib import Path
from typing import Union

from vina import Vina

import settings

v = Vina()


def process_file(file: Union[str, Path]):
    v.set_receptor(settings.SAMPLES_DIR.joinpath("Only_prot.pdbqt").__str__())
    v.set_ligand_from_file(file)
    v.compute_vina_maps([22.854, 2.545, 30.487], [30, 30, 30])
    v.dock(exhaustiveness=16)
    path_to_save = settings.BASE_DIR.joinpath(f"results/{Path(file).stem}-results.pdbqt").__str__()
    v.write_poses(path_to_save)
