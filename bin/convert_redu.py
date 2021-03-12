import sys
import uuid
import os
import pandas as pd

accession = sys.argv[1]
output_filename = sys.argv[2]

all_metadata_df = pd.read_csv("https://redu.ucsd.edu/dump", sep="\t")
dataset_df = all_metadata_df[all_metadata_df["ATTRIBUTE_DatasetAccession"] == accession]

sdrf_df = pd.DataFrame()
sdrf_df["source name"] = dataset_df["filename"].apply(lambda x: os.path.basename(x))
sdrf_df["characteristics[organism part]"] = "not applicable"
sdrf_df["characteristics[organism]"] = dataset_df["NCBITaxonomy"].apply(lambda x: x.split("|")[-1])
sdrf_df["characteristics[disease]"] = "not applicable"
sdrf_df["characteristics[cell type]"] = "not applicable"

sdrf_df["assay name"] = dataset_df["filename"]
sdrf_df["comment[data file]"] = dataset_df["filename"]
sdrf_df["comment[instrument]"] = dataset_df["MassSpectrometer"]
sdrf_df["comment[fraction identifier]"] = str(uuid.uuid4())

sdrf_df.to_csv(output_filename, sep="\t", index=False)