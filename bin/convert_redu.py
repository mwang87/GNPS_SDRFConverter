import sys
import pandas as pd

accession = sys.argv[1]
output_filename = sys.argv[2]

all_metadata_df = pd.read_csv("https://redu.ucsd.edu/dump", sep="\t")
dataset_df = all_metadata_df[all_metadata_df["ATTRIBUTE_DatasetAccession"] == accession]


sdrf_df = pd.DataFrame()
print(dataset_df.head())

sdrf_df.to_csv(output_filename, sep="\t")