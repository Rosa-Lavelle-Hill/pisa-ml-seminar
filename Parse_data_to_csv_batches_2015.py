import pandas as pd
import numpy as np
import pyreadstat
from tqdm import tqdm
# --

# chunksize determines how many rows to be read per chunk
data_type_list = ["Students", "Bullying"]

for data_type in data_type_list:
    print("Parsing 2015 {} data...".format(data_type))
    fpath = "Data/2015/Students/{}/All.sav".format(data_type)

    reader = pyreadstat.read_file_in_chunks(pyreadstat.read_sav, fpath, chunksize=10000,
                                            disable_datetime_conversion=True,  multiprocess=True, num_processes=4)
    cnt = 0
    for df, meta in tqdm(reader):
        batch_no = cnt+1
        outpath = "Data/2015/Students/{}/Batches/Batch_{}.csv".format(data_type, batch_no)
        # write
        df.to_csv(outpath, header=True)
        print("Batch {} saved".format(batch_no))
        cnt+=1

# teacher and schools
data_type_list = ["School", "Teachers"]

for data_type in data_type_list:
    print("Parsing 2015 {} data...".format(data_type))
    fpath_1 = "Data/2015/{}/All.sav".format(data_type)
    fpath_2 = "Data/2015/{}/All.sav".format(data_type)

    reader = pyreadstat.read_file_in_chunks(pyreadstat.read_sav, fpath_1, chunksize=10000,
                                            disable_datetime_conversion=True,  multiprocess=True, num_processes=4)

    cnt = 0
    for df, meta in tqdm(reader):
        batch_no = cnt+1
        outpath = "Data/2015/{}/Batches/Batch_{}.csv".format(data_type, batch_no)
        # write
        df.to_csv(outpath, header=True)
        print("Batch {} saved".format(batch_no))
        cnt+=1

print('done')