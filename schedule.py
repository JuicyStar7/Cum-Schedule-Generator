import time
import config as cfg
import pandas as pd
import numpy as np
import random
import utils


def schedule(n, days):
    sch_list = random.choices(['Cum', 'Edge', 'Deny'], weights=[cfg.cum, cfg.edge, cfg.deny], k=days)
    if n < 2:
        subs = [utils.random_sub_for_schedule(n) if i == "Cum" else utils.random_sub_for_schedule(
            n + 1) if i == "Edge" else "Nothing!" for i in sch_list]
    else:
        subs = [utils.random_sub_for_schedule(n) if i == "Cum" or i == "Edge" else "Nothing!" for i in sch_list]
    schedule_df = pd.DataFrame(sch_list, index=np.arange(1, days + 1), columns=['Task'])
    schedule_df['Subs'] = subs
    return schedule_df


def lines(df):
    for i in range(1, len(df)+1):
        if df['Task'][i] != "Deny":
            print(f"On day {i}, you will be allowed to {df['Task'][i].lower()}. You will have access to r/{df['Subs'][i]}.")
        else:
            print(f"On day {i}, you will deny yourself. You will have access to nothing.")
        time.sleep(cfg.sleep)
