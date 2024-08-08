import numpy as np
import pandas as pd

def balance_bin(df, cols):
    for col in cols:
        x = len(df[df[col] == False])/len(df[df[col] == True])
        alpha = int(np.ceil(x)) if x >= 0 else int(np.ceil(1/x))
        
        print((col, alpha))

        for _ in range(alpha - 1):
            df = pd.concat([df, df[df[col] == True if x >= 0 else False]], ignore_index=True)
    return df