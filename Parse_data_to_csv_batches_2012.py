import pandas as pd
import numpy as np
import pyreadstat

# --
path = "Data/2012/Students/All.csv"

cnt = 0
for chunk in pd.read_csv(path, chunksize=10000):
     batch_no = cnt+1
     outpath = "Data/2012/Batches/Batch_{}.csv".format(batch_no)
     # write
     chunk.to_csv(outpath, header=True)
     cnt+=1

print('done')