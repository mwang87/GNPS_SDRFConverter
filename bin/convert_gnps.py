import sys
import uuid
import os
import pandas as pd
import uuid

output_filename = sys.argv[1]

df = pd.read_csv("https://gnps-external.ucsd.edu/massiveftpproxy?ftppath=MSV000086206/metadata/metadata.txt", sep="\t")

print(df)

sdrf_df = pd.DataFrame()
sdrf_df["source name"] = df["ATTRIBUTE_Sample_Name"]
sdrf_df["characteristics[organism part]"] = "not applicable"
sdrf_df["characteristics[organism]"] = "Escherichia coli"
sdrf_df["characteristics[disease]"] = "not applicable"
sdrf_df["characteristics[cell type]"] = "not applicable"
sdrf_df["characteristics[biological replicate]"] = df["ATTRIBUTE_Mutant"]
sdrf_df["characteristics[technical replicate]"] = range(1, len(sdrf_df) + 1)


sdrf_df["assay name"] = df["filename"]
sdrf_df["comment[data file]"] = df["filename"]
sdrf_df["comment[instrument]"] = "Q Exactive"
sdrf_df["comment[fraction identifier]"] = str(uuid.uuid4())
sdrf_df["comment[label]"] = "AC=MS:1002038;NT=label free sample"
sdrf_df["comment[ionization]"] = "ESI Positive"
sdrf_df["comment[injection volumn]"] = df["Injection Volume"]

sdrf_df["factor value[mutant]"] = df["ATTRIBUTE_Mutant"]


sdrf_df.to_csv(output_filename, sep="\t", index=False)