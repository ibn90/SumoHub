# -*- coding: utf-8 -*-
# ====================================================================================================
# JASSA written by Beauclair Guillaume 2017-09-28
# ====================================================================================================

# =================================
# import ...
import argparse

# =================================
## Import arguments from command line
if __name__ == "__main__":  # to excecute only as main process
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--Fasta_file", help="File containing sequence(s) in FASTA format."
    )
    args = parser.parse_args()

# =================================
# Analyse du 29/07/2014
table_beauclair2014_sim = [
    [
        0.0098,
        0.0196,
        0.0098,
        0.0294,
        0.0294,
        0.0001,
        0.0001,
        0.2059,
        0.0001,
        0.0686,
        0.0098,
        0.0001,
        0.0588,
        0.0001,
        0.0001,
        0.0001,
        0.0098,
        0.5294,
        0.0001,
        0.0196,
        0,
    ],
    [
        0.0294,
        0.0001,
        0.0196,
        0.0196,
        0.0001,
        0.0001,
        0.0001,
        0.5098,
        0.0001,
        0.0588,
        0.0001,
        0.0098,
        0.0196,
        0.0294,
        0.0001,
        0.0294,
        0.0294,
        0.2451,
        0.0001,
        0.0001,
        0,
    ],
    [
        0.0098,
        0.0098,
        0.3137,
        0.0882,
        0.0001,
        0.0196,
        0.0001,
        0.1961,
        0.0001,
        0.0588,
        0.0001,
        0.0098,
        0.0098,
        0.0001,
        0.0098,
        0.0098,
        0.0294,
        0.2255,
        0.0001,
        0.0098,
        0,
    ],
    [
        0.0001,
        0.0001,
        0.0001,
        0.0001,
        0.0001,
        0.0001,
        0.0001,
        0.2843,
        0.0001,
        0.4510,
        0.0001,
        0.0001,
        0.0001,
        0.0001,
        0.0001,
        0.0001,
        0.0001,
        0.2647,
        0.0001,
        0.0001,
        0,
    ],
]
# Analyse du 04/02/2013
table_beauclair2012_f3_all = [
    [
        0.0570,
        0.0091,
        0.0673,
        0.1026,
        0.0319,
        0.0604,
        0.0228,
        0.0410,
        0.1026,
        0.0753,
        0.0114,
        0.0479,
        0.0525,
        0.0525,
        0.0490,
        0.0753,
        0.0570,
        0.0593,
        0.0034,
        0.0205,
        0,
    ],
    [
        0.0319,
        0.0080,
        0.0148,
        0.0251,
        0.0456,
        0.0148,
        0.0023,
        0.2668,
        0.0365,
        0.1266,
        0.0365,
        0.0194,
        0.0422,
        0.0080,
        0.0228,
        0.0308,
        0.0217,
        0.2395,
        0.0011,
        0.0057,
        0,
    ],
    [
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        1.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0,
    ],
    [
        0.0627,
        0.0103,
        0.0262,
        0.1288,
        0.0388,
        0.0228,
        0.0125,
        0.0319,
        0.0787,
        0.0730,
        0.0342,
        0.0239,
        0.0490,
        0.1095,
        0.0388,
        0.0718,
        0.0867,
        0.0821,
        0.0057,
        0.0125,
        0,
    ],
    [
        0.0274,
        0.0046,
        0.0547,
        0.6887,
        0.0160,
        0.0228,
        0.0011,
        0.0125,
        0.0296,
        0.0205,
        0.0068,
        0.0057,
        0.0388,
        0.0046,
        0.0148,
        0.0217,
        0.0103,
        0.0137,
        0.0023,
        0.0011,
        0,
    ],
]
table_beauclair2012_f3_con = [
    [
        0.0602,
        0.0084,
        0.0435,
        0.0886,
        0.0234,
        0.0702,
        0.0268,
        0.0502,
        0.1204,
        0.0635,
        0.0050,
        0.0368,
        0.0468,
        0.0635,
        0.0518,
        0.0786,
        0.0652,
        0.0719,
        0.0033,
        0.0201,
        0,
    ],
    [
        0.0184,
        0.0008,
        0.0008,
        0.0008,
        0.0468,
        0.0084,
        0.0008,
        0.3645,
        0.0008,
        0.1522,
        0.0401,
        0.0008,
        0.0485,
        0.0008,
        0.0008,
        0.0008,
        0.0008,
        0.3161,
        0.0017,
        0.0033,
        0,
    ],
    [
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        1.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0,
    ],
    [
        0.0569,
        0.0100,
        0.0284,
        0.1438,
        0.0151,
        0.0151,
        0.0117,
        0.0318,
        0.0786,
        0.0635,
        0.0435,
        0.0151,
        0.0301,
        0.1438,
        0.0351,
        0.0786,
        0.1171,
        0.0686,
        0.0067,
        0.0067,
        0,
    ],
    [
        0.0008,
        0.0008,
        0.0619,
        0.9381,
        0.0008,
        0.0008,
        0.0008,
        0.0008,
        0.0008,
        0.0008,
        0.0008,
        0.0008,
        0.0008,
        0.0008,
        0.0008,
        0.0008,
        0.0008,
        0.0008,
        0.0008,
        0.0008,
        0,
    ],
]
table_beauclair2012_f3_inv = [
    [
        0.0250,
        0.0125,
        0.0875,
        0.4125,
        0.0375,
        0.0125,
        0.0063,
        0.0250,
        0.1375,
        0.0125,
        0.0063,
        0.0063,
        0.1125,
        0.0063,
        0.0125,
        0.0500,
        0.0125,
        0.0375,
        0.0125,
        0.0063,
        0,
    ],
    [
        0.1500,
        0.0063,
        0.0063,
        0.0063,
        0.1250,
        0.0125,
        0.0063,
        0.0625,
        0.0063,
        0.0625,
        0.0875,
        0.0063,
        0.2250,
        0.0063,
        0.0063,
        0.0063,
        0.0063,
        0.2500,
        0.0063,
        0.0250,
        0,
    ],
    [
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        1.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0.0000,
        0,
    ],
    [
        0.0250,
        0.0063,
        0.0250,
        0.0375,
        0.0500,
        0.0125,
        0.0063,
        0.1625,
        0.0750,
        0.0875,
        0.0250,
        0.0250,
        0.0375,
        0.0250,
        0.0375,
        0.1500,
        0.0750,
        0.1375,
        0.0063,
        0.0125,
        0,
    ],
    [
        0.0063,
        0.0063,
        0.4500,
        0.5500,
        0.0063,
        0.0063,
        0.0063,
        0.0063,
        0.0063,
        0.0063,
        0.0063,
        0.0063,
        0.0063,
        0.0063,
        0.0063,
        0.0063,
        0.0063,
        0.0063,
        0.0063,
        0.0063,
        0,
    ],
]
# For aa to id
list_aa = [
    "A",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "K",
    "L",
    "M",
    "N",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "V",
    "W",
    "Y",
    "-",
]
# List motif SUMO
liste_seq_consensus_sumo_default = ":LIKKE:NFKSI:PLKIE:TLKYP:NPKAN:IMKCD:NPKAN:GFKAE:GFKAE:GFKAE:GFKAE:GFKAE:PIKME:HLKTE:IVKRE:AMKGL:NVKYE:KIKEE:VIKVE:KVKEE:EIKME:TVKKE:TVKQE:VAKQE:KLKWE:KLKLE:ILKEE:LIKGE:SVKVE:IGKVE:VEKVD:AEKEE:QIKSE:LCKQE:QIKCE:RIKLE:RPKEE:SVKVE:HLKDE:VIKQE:NTKVE:KTKQE:EMKTE:QVKEE:EVKVE:RLKNE:QVKPE:TVKQE:ALKKI:PLKRE:PGKIV:GEKLA:LAKVM:QEKPA:KYKFE:LRKIK:EAKPE:SIKEE:MVKFG:AVKTD:PVKRP:EIKLP:KIKEE:VIKQE:IEKNL:MLKHK:KHKRQ:RLKDE:FLKAE:YIKAE:GVKLE:FIKTE:SMKLE:IIKTE:AIKQE:RIKKE:NFKQE:VIKQE:LVKVE:QVKSD:QFKPD:RFKQE:FPKGE:LVKAP:MVKKR:ICKEE:SIKVE:RVKAE:TVKEP:VVKQE:TLKTE:PIKTE:HPKPE:PWKRE:IVKTE:ETKYP:ARKVH:EEKVE:WFKNR:RAKWR:SSKAS:KMKSE:TVKKE:IVKLE:IIKEE:EIKQE:NFKTE:KRKGF:PAKVN:GIKED:GIKED:NDKSE:NVKME:ALKKD:ALKKD:SIKID:EIKME:EFKME:KVKED:HVKMD:DIKME:VVKFE:ELKEE:IIKQE:QIKQE:LLKEE:NVKVE:VIKEE:GLKKE:LKKER:RNKEI:SCKEE:DLKNM:HIKQE:TIKNE:TIKEE:PIKSE:ALKEE:RIKAE:AFKEE:RIKVE:TLKAE:NNKFA:NNKFA:NNKFA:NNKFA:NNKFA:NNKFA:NNKFA:NNKFA:NNKFA:QFKQD:LRKVD:QVKEE:KIKQE:QIKTE:FIKQE:PVKLE:NNKFA:NNKFA:NNKFA:KLKTE:FIKEE:VLKEE:YRKLL:YRKLL:YRKLL:FAKAG:DKKLP:RIKRP:DKKLP:EVKKE:KVKRE:AIKTE:DVKEE:QVKQE:SVKQE:RPKNG:SIKSE:SIKDE:EVKSE:NIKRE:IIKQE:DMKSE:VVKKE:VKKEE:YVKKE:HVKAE:GVKVE:LVKAE:LIKFP:LLKPG:EFKPE:SIKQE:GVKHE:YIKQE:QIKRE:DKKIG:VIKTE:VVKQE:KIKTE:ELKME:ALKVE:IIKTE:TVKRE:KIKAD:KVKVE:HIKEE:FKKQE:GIKTE:SIKVE:LGKLP:YLKLE:GMKLE:LMKFE:EVKEE:PPKVE:VFKKT:FKKTE:SPKKT:PKKTK:GVKSE:EVKAE:AIKQE:IVKTE:KFKLE:PLKGE:EQKAE:AVKEE:TVKKE:FRKPI:AVKLE:DIKPF:EPKFE:KAKGP:VLKEG:TLKQE:LSKRR:WVKEE:PIKEE:KLKVE:EVKLP:TPKKE:FTKKE:VRKNL:SFKKI:PPKFV:KVKNL:KAKEK:SFKGK:KGKSL:KKKKE:VPKPE:TLKME:KVKEE:EVKSE:PLKAE:QIKQE:DSKVK:ESKVE:DSKVK:HRKAE:ESKVE:DSKVK:SVKLE:KIKEE:GIKPE:KIKQE:LPKGD:ELKGE:DIKPP:DIKRI:FTKLF:MDKLW:LGKDV:SAKRS:EQKEE:TCKSE:PVKEE:VVKRE:TCKSE:PVKEE:VVKRE:DIKPI:EIKIE:ENKYL:KVKEE:DVKIE:KMKTE:PKKLA:GYKVL:IIKKE:IKKES:SVKQE:KLKME:FVKKD:LGKNE:VVKQE:KVKKE:TPKTE:QVKTE:GIKNE:QVKDE:FRKLS:SFKKR:IIKTD:DKKEG:KPKEG:KMKLE:VVKTE:EVKSE:KLKIE:AVKEE:EMKDS:EMKAE:AVKVE:QVKAE:RIKQE:IVKEE:ETKPV:DLKEE:QEKLS:EDKAD:DTKFS:KVKQE:NVKNE:DFKAE:YEKRV:ENKAC:TPKDE:LLKYE:FFKPP:PVKQP:NIKAE:IIKME:DTKFK:YIKQE:SLKIE:HLKQE:QIKQE:EIKTE:PFKCS:QKKYL:SVKQE:KVKDE:EGKTE:SFKCE:SIKNK:RIKEE:KIKDE:IVKSE:DQKFR:GIKEE:SIKTE:TIKTE:KVKVE:PIKVE:SLKIP:RIKEE:FEKGE:MFKFE:FIKQE:SFKHE:NIKRE:IIKQE:NIKRE:VVKQE:EPKFE:TIKDE:RIKEE:KLKKE:ALKLE:LLKSE:CLKME:PIKTE:EIKSE:ALKAE:EVKEE:VVKSE:IPKNR:RLKPL:QAKKF:NLKSE:EVKVE:GPKEE:PIKDE:GFKLE:AIKSE:TLKTE:FLKIE:ITKET:LVKME:AIKTE:TVKQE:LTKED:HVKME:LEKLM:LMKAF:SLKSF:RIKLE:CVKSE:HVKYC:MVKDE:IVKQE:KVKTE:TVKEE:GVKEE:QIKQE:AEKEE:QIKSE:LCKQE:QIKCE:SGKSS:VAKQE:IYKAD:KIKVE:AVKPE:GLKKE:YIKTE:SIKVE:YLKLE:EVKTE:SKKEE:DIKTE:YIKPE:PIKQE:GIKQE:ALKVE:QVKSD:KIKEE:ELKTE:EIKEE:ELKAE:KIKME:TVKPE:SLKEE:SIKQD:QIKQE:DVKVE:IAKSD:LAKLE:LQKSE:SVKNE:TVKQE:LAKDK:SMKME:TMKKE:TVKQE:RVKEE:VIKQE:KIKQE:GIKEE:GVKTE:KVKDE:ARKRE:RKKKE:SIKLE:KVKVE:VIKQE:DLKMD:KIKKE:QIKDE:KIKTE:KIKEE:RIKGE:RVKTE:GVKEE:TVKKE:IGKVE:VEKVD:LIKTE:LLKRE:PCKKS:CKKSR:QVKTE:VIKQE:IVKRE:KIKLE:KIKKE:DIKKE:NIKYE:SIKEE:TIKQE:TEKEE:QVKQE:MFKTE:ALKEE:RIKAE:DIKKE:PIKTE:PFKDE:QVKQE:EAKCP:FLKHE:VIKME:PIKEE:KLKIE:KIKQE:EIKQE:SIKTE:LIKQE:DIKPE:QIKAP:SVKSE:CKKQE:GVKRE:RIKQE:IVKQE:TLKLE:TIKSE:DVKFT:EIKKQ:SSKTG:AVKAL:EFKEV:GLKLE:AIKSE:NIKQE:PVKQE:KIKIE:AVKEE:SIKPE:AVKLE:PQKQE:VVKFE:PFKKT:EPKEE:KPKEE:YEKNE:KVKQE:SYKVI:MVKNV:LLKMG:SMKTE:SIKSE:AIKTE:SIKSE:NVKVE:VIKEE:DLKFK:LIKIE:ELKKF:PKKRE:GHKAE:DLKID:SVKKG:ELKFP:SSKCL:DRKED:LSKPE:PEKMS:GLKHE:QAKVG:KIKRE:GFKQE:GIKQE:KVKQE:KIKTE:FIKKE:ELKTE:VVKAE:ELKKE:HIKTE:KVKKE:QVKTE:CVKNE:EMKTE:QVKEE:EVKVE:GTKME:LLKWE:NVKKE:EVKEE:YLKWE:NLKEE:LLKDE:NVKRE:VAKQE:KLKWE:KLKLE:VIKLE:SVKVE:LVKEE:PVKQE:VVKQE:IIKTE:AIKQE:KIKME:QAKAE:RLKME:DIKIE:DIKQE:NIKSE:RPKTG:ESKVE:DSKVK:ATKLK:EEKAK:KAKAD:GDKKE:HFKVK:KVKMT:LKKLK:GIKVE:YIKKE:SVKME:IAKLA:ERKAW:GKKGT:SIKQE:FSKLG:GMKSE:RAKPT:AMKIP:TDKIV:EAKPS:KLKVI:FKKLF:KIKEE:TIKQE:IVKEE:ETKPV:DLKEE:QEKLS:EDKAD:DTKFS:GTKE-:AVKEE:LIKME:VVKSE:GPKDE:FPKGE:LVKAP:AVKLE:RVKEE:VVKTE:KIKED:TVKKE:VIKQE:WMKHE:SLKSE:VIKTE:QPKTE:GLKSE:SIKKE:YIKAE:GVKLE:EFKFP:LPKVE:QIKLD:DVKKE:KVKCE:VVKIE:PLKEE:RVKAE:RIKKE:SFKQE:VIKQE:DIKQE:ALKAE:AKKSA:NMKHF:TFKEE:SVKLE:KIKSE:TIKKE:DIKVE:DPKAD:SIKAE:KIKTE:SVKEE:LPKVE:DVKDE:EVKKE:QVKKE:TIKSE:HIKTE:FIKQE:NIKTE:EVKMD:PLKDE:LVKLE:PVKKP:VKKPK:KPKME:HLKGD:PAKIE:KMKIE:LLKAG:EVKED:KLKEE:FIKLE:KIKRE:KKKKE:TPKPE:TLKME:TIKEE:RIKHE:LIKSE:TLKYP:IMKCD:IVKTE:ELKSE:KLKAE:LIKLE:QLKEE:SIKME:HLKTE:VVKRE:GMKLE:TMKEE:PLKSD:CAKHE:ADKSA:DVKPS:DDKDD:KIKKE:DIKPF:AIKVE:LLKVE:GSKK-:CAKLE:LFKPE:GLKDP:QVKLE:KIKLE:QMKTE:EVKKE:AIKQE:LLKST:DMKSE:VVKKE:VKKEE:YVKKE:HVKAE:VVKIE:SVKKE:RLKTE:DYKPP:HLKHL:TQKQR:KRKAN:GVKSA:LQKPL:ERKPD:KRKGF:PDKKE:EGKKE:SLKID:RVKRE:AIKKE:LVKPE:PIKVF:EIKQE:YIKHP:FFKND:GDKIA:ATKSG:TTKNR:EIKEE:AIKEE:FIKVP:RMKRP:ELKQE:NIKTE:DMKKR:MKKRK:KRKYD:VMKEF:ANKFV:TVKIG:EVKKE:RIKER:EEKEG:DEKTA:FAKRQ:LPKFE:LPKFE:AIKVE:KVKTE:LLKSE:QVKTE:VIKQE:GVKTE:NVKYE:AVKEE:LLKSE:IIKTE:DEKPK:GVKTE:LSKLM:VIKQE:KIKQE:CAKDG:RDKSS:SSKVP:DGKLI:ETKNV:MLKTS:TSKAE:EEKSK:KSKPI:LSKLM:HIKTE:GFKLE:AIKVE:EVKKE:AIKSE:NNKFA:ESKVE:DSKVK:ESKVE:DSKVK:GVKTD:GVKTE:VVKEE:DVKEE:GIKSE:EIKEE:SIKKE:LVKQE:KIKNE:EMKAE:KPKSE:LIKSE:EIKKE:ELKRD:LVKIE:DEKKP:EKKPV:VVKIE:SVKEE:DVKVE:RIKEE:PIKED:RIKVE:TPKVE:LIKTE:DIKPE:SGKEG:PDKQP:EVKSE:RVKVE:QLKSE:QVKPE:HVKLE:IPKVE:EKKPD:KKKGK:KVKGQ:LKKLM:-MKSE:KVKGE:DIKRK:PVKQE:NDKVP:SPKEE:TVKSE:SVKLE:QSKQY:NIKSE:RLKEE:RSKLS:RLKEE:DFKRE:LSKGL:FGKIC:EVKEC:ERKVF:SRKGL:LPKPD:EKKPA:ATKAS:DIKNS:DLKRE:KQKVS:MYKRD:LAKHE:AIKQE:TIKVE:RVKTE:AVKQE:RLKLE:KQKRK:KRKME:QYKDD:ETKAK:KAKRK:KRKRK:KRKLI:SVKEL:DSKTI:PTKKL:TKKLM:MWKET:VEKLF:LLKLF:LRKRR:RRKGG:FLKEF:SVKEE:PIKQE:ALKAP:GDKVG:DIKPE:FPKTL:LMKFE:EVKKE:HLKQE:KVKQE:DLKGD:LVKYD:QLKLE:TLKVE:KVKLD:RLKRD:TVKAE:FKKTH:AEKKP:RHKKT:KRKLE:PPKFT:FIKTE:IIKQD:FHKFQ:QTKAY:LYKMF:YPKAG:YQKRM:ILKEE:KQKRE:ILKEL:IFKNE:AVKTN:NHKKE:HKKEK:KEKSK:KSKKD:SKKDK:KDKSR:SRKHY:QLKGE:GIKQE:LWKGE:KIKTE:KIKKE:ALKEE:KVKLE:QIKYE:RAKQD:PNKRR:LVKDE:LIKKE:LVKEE:TVKAE:GIKME:ELKGD:EVKSE:TLKYP:IMKCD:FIKRS:PMKDE:DNKDS:RPKTE:APKIE:KVKVE:DLKSE:KVKNE:RPKVE:FFKDG:IAKKD:EIKRE:GGKAR:LNKPP:DIKPT:LEKPS:GIKQE:LMKKE:FIKYE:DRKTR:RLKPY:RVKRN:NVKKA:VKKAP:GVKNM:FDKNY:SGKSR:GKKHD:TRKMS:KEKYE:QHKIT:TSKGG:DAKEE:TKKQK:KQKCG:HGKVK:GVKDR:LIKTE:WFKKG:QLKRE:RKKKE:FVKEE:EVKPD:KFKLE:MEKRE:DHKSF:TLKDE:ERKFA:TLKQE:EPKFD:IFKAE:EPKDE:GGKPE:PNKLE:VSKIL:MLKAE:FVKDD:SSKNG:GVKVE:LVKAE:LLKGE:EGKEA:PWKRE:DLKLE:GLKDE:AVKME:QVKAE:TQKQE:PIKKE:TLKRP:ELKVE:QSKLL:ASKTN:NEKSP:TVKKE:NLKLG:AVKSE:FFKRE:LFKNE:EFKDI:INKLD:ILKHE:ELKKE:DVKKE:DIKPF:EPKFE:QIKTE:CAKKE:FAKKE:AVKIF:PIKIE:QIKPE:LVKAG:QVKKE:NIKLD:MAKID:IAKFA:YVKPQ:QIKQV:VVKGQ:MKKYK:KYKKM:REKSE:KSKKK:KKKRE:EQKRE:KPKRE:TLKQE:LIKSE:SLKVE:DVKEE:QMKTE:EVKKE:QAKRE:QAKQY:YSK--:YVKPQ:QIKQV:TVKAS:GVKID:ETKPT:AQKKA:AFKPE:DIKQE:VIKME:VVKGD:LNKKE:NKKER:STKKK:TKKKK:KKKKE:KKKES:EVKRE:TVKEE:IVKVD:KVKSE:DIKVE:MLKKD:SEKVE:LLKVD:EVKLK:KLKVD:LGKGG:TGKTI:PVKKR:VKKRK:KRKRK:KRKCL:QYKRE:ATKAA:NMKHF:SIKSE:EIKPA:PLKME:ALKPE:HFKDE:RVKLE:GIKTE:RYKCE:CVKKR:VKKRD:IVKHE:EIKLE:SAKVL:AIKTE:QLKRE:ERKVQ:IEKEA:DAKTR:KIKNE:FIKLE:HIK--:DIKTE:VPKIE:IVKTE:PLKEE:PVKAE:AIKAE:EEKLP:LVKHS:VIKKE:IIKEE:EAKTE:GPKKG:EPKKE:MIKTE:ALKSE:PRKDE:VLKIE:FLKNE:KFKRP:KLKVE:ELKIE:EVKKE:QMKVE:SVKEE:TSKPV:VIKKE:AVKSE:LIKGE:QPKYE:FKKEN:ERKFM:EPKPE:YFKEE:DAKLY:DVKRR:GPKVE:VFKKT:FKKTE:KRKKH:RKKHS:VIKNS:SIKLR:SVKQE:KVKDE:EHKLI:EVKTE:TIKND:TIKSE:AIKEE:PIKIE:ELKHV:LVKDE:IPKIE:WVKRE:EFKKE:GIKEE:YIKEE:RYKIE:KTKVE:KLKIE:PTKIS:PAKEE:DLKPD:TLKPE:TVKKV:GVKME:KIKSE:IIKCE:ATKEE:PVKSE:FVKTE:RPKEK:KEKSL:LVKLE:TIKSE:KPKME:RFKN-:DSKPG:TVKHL:SMKRK:KRKDV:DEKQP:DIKPE:VKKEK:VIKSE:ITKVE:RIKVE:DVKIE:GDKVG:SCKMA:LVKAE:PIKPE:QIKVD:PVKAD:LLKKV:LKKVL:SIKDL:FTKAT:EYKVA:APKIE:QRKVD:DIKED:AIKTE:TVKQE:VIKKE:RLKEE:YLKKE:FSKRI:ETKPD:WAKYL:WRKRK:QVKRE:RIKQE:WIKQE:DLKKE:NIKIE:SIKQE:YLKTE:TLKPD:KPKDE:YVKVE:FVKEE:SVKHE:ALKEE:GVKQE:QEKTE:HVKIE:DLKPD:LSKKE:FTKKE:FAKRE:LHKME:DAKPE:DVKKE:KVKCE:AVKQE:AEKEK:KIKKE:IKKED:"
# =================================

##Functions
def aa_to_id(aa):
    """..."""
    return list_aa.index(aa)


def score_sumo(aa1, aa2, aa3, aa4, aa5, tbs, tbs_id):
    """..."""
    score_con = (
        tbs[1][aa_to_id(aa2)] * tbs[2][aa_to_id(aa3)] * tbs[4][aa_to_id(aa5)] * 100
    )
    score_inv = (
        tbs[1][aa_to_id(aa4)] * tbs[2][aa_to_id(aa3)] * tbs[4][aa_to_id(aa1)] * 100
    )
    if tbs_id == "all":
        # Con
        if score_con >= 12.78:
            str_con = "High"
        elif score_con >= 2.46:
            str_con = "Low "
        else:
            str_con = "None"
            # Inv
        if score_inv >= 12.78:
            str_inv = "High"
        elif score_inv >= 2.46:
            str_inv = "Low "
        else:
            str_inv = "None"
    elif tbs_id == "con":
        # Con
        if score_con >= 21.14:
            str_con = "High"
        elif score_con >= 2.94:
            str_con = "Low "
        else:
            str_con = "None"
            # Inv
        if score_inv >= 21.14:
            str_inv = "High"
        elif score_inv >= 2.94:
            str_inv = "Low "
        else:
            str_inv = "None"
    elif tbs_id == "inv":
        # Con
        if score_con >= 10.21:
            str_con = "High"
        elif score_con >= 2.72:
            str_con = "Low "
        else:
            str_con = "None"
            # Inv
        if score_inv >= 10.21:
            str_inv = "High"
        elif score_inv >= 2.72:
            str_inv = "Low "
        else:
            str_inv = "None"
    else:
        str_con = "Error_001"
        str_inv = "Error_001"
    return score_con, score_inv, str_con, str_inv


print("\n====================\n===== JASSA.v1 =====\n====================\n")
print("* Reading file...")
multi_fasta_seq = []
nb_seq_tot = 0
with open(args.Fasta_file, "r") as f:
    for l in f:
        if l.startswith(">"):
            if nb_seq_tot > 0:
                dic.update({name: dic[name] + "--"})
            dic = {}
            multi_fasta_seq.append(dic)
            name = l[1:].strip()
            dic.update({name: "--"})
            nb_seq_tot += 1
        else:
            dic.update({name: dic[name] + l.strip()})
    if nb_seq_tot > 0:
        dic.update({name: dic[name] + "--"})


print("* {} sequences found:".format(nb_seq_tot))
nb_seq = 0

with open("JASSA.csv", "w") as f:
    f.write(
        "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
            "Seq_Name",
            "Pos_K",
            "Motif",
            "DB_All_Score_Cons",
            "DB_All_Score_Inv",
            "DB_All_Status_Cons",
            "DB_All_Status_Inv",
            "DB_Cons_Score_Cons",
            "DB_Cons_Score_Inv",
            "DB_Cons_Status_Cons",
            "DB_Cons_Status_Inv",
            "DB_Inv_Score_Cons",
            "DB_Inv_Score_Inv",
            "DB_Inv_Status_Cons",
            "DB_Inv_Status_Inv",
            "DB_Hit_Cons",
            "DB_Hit_Inv",
        )
    )
    for fasta_seq in multi_fasta_seq:
        name_seq = list(fasta_seq.keys())[0]
        nb_seq += 1
        print("----------")
        print(
            "** [{}/{}] Searching SUMO motif in sequence: {}".format(
                nb_seq, nb_seq_tot, name_seq
            )
        )
        seq = list(fasta_seq.values())[0].upper()
        list_K = [pos for pos, char in enumerate(seq) if char == "K"]
        if not list_K:
            print("No K found in sequence")
            f.write("{},{}\n".format(name_seq, "No K found in sequence"))
            continue
        for pos_K in list_K:
            motif_5 = (
                seq[pos_K - 2]
                + seq[pos_K - 1]
                + seq[pos_K]
                + seq[pos_K + 1]
                + seq[pos_K + 2]
            )
            score_all = score_sumo(
                seq[pos_K - 2],
                seq[pos_K - 1],
                seq[pos_K],
                seq[pos_K + 1],
                seq[pos_K + 2],
                table_beauclair2012_f3_all,
                "all",
            )
            score_con = score_sumo(
                seq[pos_K - 2],
                seq[pos_K - 1],
                seq[pos_K],
                seq[pos_K + 1],
                seq[pos_K + 2],
                table_beauclair2012_f3_con,
                "con",
            )
            score_inv = score_sumo(
                seq[pos_K - 2],
                seq[pos_K - 1],
                seq[pos_K],
                seq[pos_K + 1],
                seq[pos_K + 2],
                table_beauclair2012_f3_inv,
                "inv",
            )
            # Con
            score_best_con = "None"
            if (
                score_all[2] == "High"
                or score_con[2] == "High"
                or score_inv[2] == "High"
            ):
                score_best_con = "High"
            elif (
                score_all[2] == "Low "
                or score_con[2] == "Low "
                or score_inv[2] == "Low "
            ):
                score_best_con = "Low "
                # Inv
            score_best_inv = "None"
            if (
                score_all[3] == "High"
                or score_con[3] == "High"
                or score_inv[3] == "High"
            ):
                score_best_inv = "High"
            elif (
                score_all[3] == "Low "
                or score_con[3] == "Low "
                or score_inv[3] == "Low "
            ):
                score_best_inv = "Low "

            db_hit_con = liste_seq_consensus_sumo_default.count(motif_5[1:5] + ":")
            db_hit_inv = liste_seq_consensus_sumo_default.count(":" + motif_5[0:4])

            if (
                db_hit_con != 0
                or db_hit_inv != 0
                or score_best_con != "None"
                or score_best_inv != "None"
            ):
                print(
                    "K {:4d}\tMotif {}\tScore Cons.: {}\tScore Inv.: {}\tDB Hit Cons.: {:4d}\tDB Hit Inv.: {:4d}".format(
                        pos_K - 1,
                        motif_5,
                        score_best_con,
                        score_best_inv,
                        db_hit_con,
                        db_hit_inv,
                    )
                )
            f.write(
                "{},{},{},{:.3f},{:.3f},{},{},{:.3f},{:.3f},{},{},{:.3f},{:.3f},{},{},{},{}\n".format(
                    name_seq,
                    pos_K - 1,
                    motif_5,
                    score_all[0],
                    score_all[1],
                    score_all[2],
                    score_all[3],
                    score_con[0],
                    score_con[1],
                    score_con[2],
                    score_con[3],
                    score_inv[0],
                    score_inv[1],
                    score_inv[2],
                    score_inv[3],
                    db_hit_con,
                    db_hit_inv,
                )
            )
    print("----------")
