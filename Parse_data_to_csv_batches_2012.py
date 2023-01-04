import pandas as pd
import numpy as np
import pyreadstat

# --
data_type_list = ["School", "Parents", "Students"]

for data_type in data_type_list:
     print("Parsing 2012 {} data...".format(data_type))
     path = "Data/2012/{}/All.csv".format(data_type)
     cnt = 0
     for chunk in pd.read_csv(path, chunksize=10000):
          batch_no = cnt+1
          outpath = "Data/2012/{}/Batches/Batch_{}.csv".format(data_type, batch_no)
          # write
          chunk.to_csv(outpath, header=True)
          print("Batch {} saved".format(batch_no))
          cnt+=1

print('done')