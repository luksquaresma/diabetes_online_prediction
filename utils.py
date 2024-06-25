import numpy as np
import pandas as pd

def balance_bin(df, cols):
    for col in cols:
        x = len(df[df[col] == 0])/len(df[df[col] == 1])
        alpha = int(np.ceil(x)) if x >= 0 else int(np.ceil(1/x))
        
        print((col, alpha))

        # for _ in range(alpha - 1):
            # df = pd.concat([df, df[df[col] == 1]], ignore_index=True)
    return df