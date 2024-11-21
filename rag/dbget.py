from pathlib import Path
from typing import List, Tuple, Set, Dict, Union, Any
import numpy as np
import queries
from connector import DB
import pandas as pd


def get_labeled_dialogues_ts01(db: DB, is_en: bool = True) -> pd.DataFrame:
    """
    Generate and save datasets for  2024 from TS01.
    """
    print('Pull the data for splits...')
    cur = db.conn.cursor()
    if is_en:
        query = queries.GET_EN_CONVERSATIONS_EACL_TS1_CERTAIN_NHOT
    else:
        query = queries.GET_CONVERSATIONS_EACL_TS1_NHOT_CS
        # raise Exception("Not Implemented")
    cur.execute(query)

    # ordered list of utterances, ordered list of labels, authors, user_id, thread_id, conv_id
    allc: List[Tuple[List[str], List[List[int]], List[str], int, int, int]] = cur.fetchall()
    cur.close()

    import ipdb; ipdb.set_trace()
    df = pd.DataFrame(allc)
    import ipdb; ipdb.set_trace()
    
    print('DF loaded')
    return df

