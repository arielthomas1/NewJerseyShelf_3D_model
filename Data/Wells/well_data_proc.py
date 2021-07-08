# -*- coding: utf-8 -*-
"""
Script to combine well data and perform sea level correction.
"""

# Import dependencies
import numpy as np
import pandas as pd

pd.set_option('precision', 2)

# Import data
# Load single wells
por_data_m27 = pd.read_csv("m27_por_method2.csv")
por_data_m28 = pd.read_csv("m28_por_method2.csv")
por_data_m29 = pd.read_csv("m29_por_method2.csv")

# Sea level correction
por_data_m27["Z"]=por_data_m27["Z"]-33 
por_data_m28["Z"]=por_data_m28["Z"]-35
por_data_m29["Z"]=por_data_m29["Z"]-36

# combine in single df, sort for n-score transform
df = pd.concat([por_data_m27, por_data_m28, por_data_m29],ignore_index=True)
df = df.sort_values(by=['Porosity'])

# Add well information
def derive_well(row):
    if row['X'] == por_data_m27.values[0,0]:
        return 'm27'
    elif row['X'] == por_data_m28.values[0,0]:
              return 'm28'
    elif row['X'] == por_data_m29.values[0,0] :
              return 'm29'
    return 'Other'

df["Well"] = df.apply(lambda row: derive_well(row), axis=1)

# correct coordinates (0=landwards, 134000=oceanward)
df["Y"]=134000-df["Y"]
df["X"]=69000-df["X"]

df.to_csv("Complete_set_corrected.csv", index=False)