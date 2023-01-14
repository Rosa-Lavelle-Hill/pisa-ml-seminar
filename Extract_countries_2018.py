import pandas as pd
import os
import re
from tqdm import tqdm

# Extract Germany, Austria, Greece and France
# target_countries = ["DEU", "AUT", "GRC", "FRA"]
# data_dict = {'DEU': [],
#              "AUT": [],
#              "GRC": [],
#              "FRA": []
#              }


# Extract Germany and Ireland:
target_countries = ["DEU", "IRL"]

data_type_list = ["School", "Teachers", "Students"]
for data_type in data_type_list:
    print("\nParsing 2018 {} data...".format(data_type))
    batches_path = "Data/2018/{}/Batches/".format(data_type)
    data_dict = {'DEU': [],
                 'IRL': []}

    for file in tqdm(os.listdir(batches_path)):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"):
            batch_num = re.findall(r'\d+', filename)[0]
            print('processing batch number {}'.format(batch_num))
            df = pd.read_csv(batches_path + filename, index_col=[0])

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

    DEU_df = pd.DataFrame(data_dict['DEU'])
    IRL_df = pd.DataFrame(data_dict['IRL'])

    # remove any duplicates and na rows:
    print(DEU_df.shape)
    DEU_df.drop_duplicates(inplace=True)
    DEU_df.dropna(axis=0, how="all", inplace=True)
    print(DEU_df.shape)

    print(IRL_df.shape)
    IRL_df.drop_duplicates(inplace=True)
    IRL_df.dropna(axis=0, how="all", inplace=True)
    print(IRL_df.shape)

    # save to .csv
    countries_path = "Data/2018/{}/Countries/".format(data_type)
    DEU_df.to_csv(countries_path + "DEU.csv")
    IRL_df.to_csv(countries_path + "IRL.csv")


print('done')