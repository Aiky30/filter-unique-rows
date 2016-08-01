import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, 'data')

INPUT_FILENAME = os.path.join(DATA_DIR, 'in.csv')

OUTPUT_FILENAME = os.path.join(DATA_DIR, 'out.csv')

INPUT_HEADINGS = [
    'PEN_ND10',
    'PEN_NM',
    'CRO_ND30',
    'CRO_NM',
    'CFM_ND5',
    'CFM_NM',
    'SPT_ND100',
    'SPT_NM',
    'CIP_ND5',
    'CIP_NM',
    'TCY_ND30',
    'TCY_NM',
]

OUTPUT_HEADINGS = INPUT_HEADINGS