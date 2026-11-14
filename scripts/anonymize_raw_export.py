"""
Turn the raw Resultal export into the file that is shared in this repository.

The raw export is NOT in the repository. It has exact submission timestamps
and the platform's internal IDs, and with a small sample recruited through
friends and classmates that is more than I want to put online.

What this script does:
  1. drops the columns that are not needed for the analysis
     (row id, account id, submission timestamp, platform question code)
  2. replaces the platform's visitor_id with a shuffled code (P01, P02, ...)
     so the codes do not reveal the order in which people took part
  3. writes the shareable file to data/trials_anonymized.csv
  4. writes the key (visitor_id -> code) next to the raw file, so it stays private

Usage:
    python scripts/anonymize_raw_export.py path/to/MasterData_merged.csv
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

DROP_COLUMNS = ['id', 'user_id', 'created_at', 'wid']
SEED = 2026


def main(raw_path):
    raw_path = Path(raw_path)
    out_path = Path(__file__).resolve().parent.parent / 'data' / 'trials_anonymized.csv'

    # keep_default_na=False: one of the answer options is the word "None",
    # which pandas would otherwise silently read as a missing value
    raw = pd.read_csv(raw_path, keep_default_na=False)

    visitor_ids = np.sort(raw['visitor_id'].unique())
    shuffled = np.random.default_rng(SEED).permutation(visitor_ids)
    key = {vid: 'P{:02d}'.format(i + 1) for i, vid in enumerate(shuffled)}

    raw['participant'] = raw['visitor_id'].map(key)
    raw['row_order'] = np.arange(len(raw))
    shared = (
        raw.drop(columns=DROP_COLUMNS + ['visitor_id'])
           .sort_values(['participant', 'row_order'])
           .drop(columns='row_order')
    )
    # participant first, the rest in the original column order
    shared = shared[['participant'] + [c for c in shared.columns if c != 'participant']]
    shared.to_csv(out_path, index=False)

    key_path = raw_path.parent / 'participant_key_PRIVATE.csv'
    pd.Series(key, name='participant').rename_axis('visitor_id').to_csv(key_path)

    print('Participants:', len(key))
    print('Rows:', len(shared))
    print('Shareable file:', out_path)
    print('Private key (do not upload):', key_path)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
