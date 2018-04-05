import pandas as pd
from constants import ORIGINAL_DB_HEADER


def convert_tab_to_pandas(filename):
    df = pd.read_csv(filename, sep='\t', lineterminator='\r', header=None, names=ORIGINAL_DB_HEADER)
    # remove \n from ncdsid
    for index, row in df.iterrows():
        new_name = df.loc[index, 'ncdsid']
        new_name = new_name.replace('\n', '')
        df.loc[index, 'ncdsid'] = new_name

    return df
