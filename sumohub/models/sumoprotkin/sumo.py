from models.pipelines import Pipeline, Stage
from .source import Source
from .uniprot_pdb import Uniprot_PDB
from .pdb_filter import PDB_Filter
from .uniprot_canonical import Uniprot_Canonical
from .uniprot_sumo import Uniprot_Sumo
from .uniprot_fasta import Uniprot_Fasta
from .uniprot_active_sites import Uniprot_active_sites
from .uniprot_pdb_fasta import Uniprot_PDB_Fasta
from .distances_map import Distances_Map
from .sink import Sink


def stages(debug=False):
    return [
        Source("PFAM->UNIPROT", caching=debug),
        Uniprot_PDB("UNIPROT->PRE-FILTER->PDB", caching=debug),
        # PDB_Filter("PDB-> (RES-FILTERED) PDB",caching=True),
        Uniprot_Canonical("UNIPROT->UNIPROT CANONICAL ISOFORM", caching=debug),
        Uniprot_Fasta("UNIPROT->FASTA SEQUENCE", caching=debug),
        Uniprot_Sumo("UNIPROT->PREDICTED SUMOYLATION SITES", caching=debug),
        Uniprot_active_sites("UNIPROT->SEQUENCE ACTIVE RESIDUES",caching=debug),
        Uniprot_PDB_Fasta("MERGE UNIPROT+PDB+SUMO_SITES+ACTIVE_SITES+FASTA",caching=debug),
        Distances_Map("SUMO+PDB+ACTIVE_SITES->DISTANCE BETWEEN RESIDUES AND ACTIVE SITES",caching=debug),
        Sink("GENERATE REPORTS"),
    ]

if __name__ == "__main__":
    for stage in stages:
        print(stage.get_name())
