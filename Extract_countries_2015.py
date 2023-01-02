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


# Extract Germany:
target_countries = ["DEU"]

data_type_list = ["Teachers", "School"]
for data_type in data_type_list:
    data_dict = {'DEU': []}
    print("\nParsing 2015 {} data...".format(data_type))
    batches_path = "Data/2015/{}/Batches/".format(data_type)

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

    # remove duplicates:
    print(DEU_df.shape)
    DEU_df.reset_index(inplace=True, drop=True)
    DEU_df.drop_duplicates(inplace=True)
    DEU_df.dropna(axis=0, how="all", inplace=True)
    print(DEU_df.shape)

    # save to .csv
    countries_path = "Data/2015/{}/Countries/".format(data_type)
    DEU_df.to_csv(countries_path+"DEU.csv")


# student level:
data_type_list = ["Students", "Bullying"]
for data_type in data_type_list:
    print("\nParsing 2015 {} data...".format(data_type))
    batches_path = "Data/2015/Students/{}/Batches/".format(data_type)
    data_dict = {'DEU': []}
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

    # remove duplicates and na rows:
    print(DEU_df.shape)
    DEU_df.reset_index(inplace=True, drop=True)
    DEU_df.drop_duplicates(inplace=True)
    DEU_df.dropna(axis=0, how="all", inplace=True)
    print(DEU_df.shape)

    # save to .csv
    countries_path = "Data/2015/Students/{}/Countries/".format(data_type)
    DEU_df.to_csv(countries_path+"DEU.csv")

print('done')