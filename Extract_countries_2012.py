import pandas as pd
import numpy as np
import pyreadstat
import os
import re

batches_path = "Data/2012/Students/Batches/"

# Extract Germany, Austria, Greece and France
target_countries = ["Germany", "Austria", "Greece", "France"]

data_dict = {'Germany': [],
             "Austria": [],
             "Greece": [],
             "France": []
             }

for file in os.listdir(batches_path):
    filename = os.fsdecode(file)
    if filename.endswith(".csv"):
        batch_num = re.findall(r'\d+', filename)[0]
        print('processing batch number {}'.format(batch_num))
        df = pd.read_csv(batches_path + filename)
        df.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1, inplace=True)

        # first screen:
        countries = list(df["CNT"].unique())
        if any(x in countries for x in target_countries):

            # if yes, iterate through and save rows:
            for index, row in df.iterrows():
                row_country = row['CNT']
                if row_country in target_countries:
                    data_dict[row_country].append(row)
                else:
                    continue

        else:
            continue

DEU_df = pd.DataFrame(data_dict['Germany'])
AUT_df = pd.DataFrame(data_dict['Austria'])
GRC_df = pd.DataFrame(data_dict['Greece'])
FRA_df = pd.DataFrame(data_dict['France'])

# save to .csv
countries_path = "Data/2012/Students/Countries/"

DEU_df.to_csv(countries_path+"Germany.csv")
AUT_df.to_csv(countries_path+"Austria.csv")
GRC_df.to_csv(countries_path+"Greece.csv")
FRA_df.to_csv(countries_path+"France.csv")

print('done')