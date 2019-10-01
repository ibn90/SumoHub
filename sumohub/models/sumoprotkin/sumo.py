from models.pipelines import Pipeline, Stage
import pandas as pd
import os
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


stages = [
    Source("PFAM->UNIPROT",caching=True),
    Uniprot_PDB("UNIPROT->PRE-FILTER->PDB",caching=True),
    PDB_Filter("PDB-> (RES-FILTERED) PDB",caching=True),
    Uniprot_Canonical("UNIPROT->UNIPROT CANONICAL ISOFORM",caching=True),
    Uniprot_Fasta("UNIPROT->FASTA SEQUENCE",caching=True),
    Uniprot_Sumo("UNIPROT->PREDICTED SUMOYLATION SITES"),
    Uniprot_active_sites("UNIPROT->SEQUENCE ACTIVE RESIDUES"),
    Uniprot_PDB_Fasta("MERGE UNIPROT+PDB+SUMO_SITES+ACTIVE_SITES+FASTA"),
    Distances_Map("SUMO+PDB+ACTIVE_SITES->DISTANCE BETWEEN RESIDUES AND ACTIVE SITES"),
    Sink("GENERATE REPORTS"),
]

if __name__ == "__main__":
    for stage in stages:
        print(stage.get_name())
