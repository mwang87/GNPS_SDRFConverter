import sys
import uuid
import os
import pandas as pd
import uuid

accession = sys.argv[1]
output_filename = sys.argv[2]

all_metadata_df = pd.read_csv("https://redu.ucsd.edu/dump", sep="\t")
dataset_df = all_metadata_df[all_metadata_df["ATTRIBUTE_DatasetAccession"] == accession]

sdrf_df = pd.DataFrame()
sdrf_df["source name"] = "1"
sdrf_df["characteristics[organism part]"] = dataset_df["UBERONBodyPartName"]
sdrf_df["characteristics[organism]"] = dataset_df["NCBITaxonomy"].apply(lambda x: x.split("|")[-1])
sdrf_df["characteristics[disease]"] = dataset_df["DOIDCommonName"]
sdrf_df["characteristics[cell type]"] = dataset_df["SampleType"]

sdrf_df["assay name"] = dataset_df["filename"]
sdrf_df["comment[data file]"] = dataset_df["filename"].apply(lambda x: os.path.basename(x))
sdrf_df["comment[instrument]"] = dataset_df["MassSpectrometer"]
sdrf_df["comment[fraction identifier]"] = str(uuid.uuid4())
sdrf_df["comment[label]"] = "AC=MS:1002038;NT=label free sample"
sdrf_df["comment[separation]"] = dataset_df["ChromatographyAndPhase"]
sdrf_df["comment[ionization]"] = dataset_df["IonizationSourceAndPolarity"]
sdrf_df["comment[internalstandard]"] = dataset_df["InternalStandardsUsed"]
sdrf_df["comment[extraction]"] = dataset_df["SampleExtractionMethod"]


# Customization
sdrf_df["source name"] = range(1, len(sdrf_df) + 1)
sdrf_df["comment[instrument]"] = sdrf_df["comment[instrument]"].apply(lambda x: "NT={};AC={}".format(x.split("|")[0], x.split("|")[1]))



sdrf_df.to_csv(output_filename, sep="\t", index=False)