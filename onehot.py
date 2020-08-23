import pandas as pd
import numpy as np


def encode(df):     
    one_hot1 = pd.get_dummies(df['Region'])
    one_hot2 = pd.get_dummies(df['Gender'])
    df = df.join(one_hot1)
    df = df.join(one_hot2)
    return df

def get_output_schema():       
  return pd.DataFrame({
    'ID': prep_int(),


    #...this ain't dynamic
    'America' : prep_int(),
    'Africa' : prep_int(),
    'Europe' : prep_int(),
    'Asia' : prep_int(),

    'Male' : prep_int(),
    'Female' : prep_int(),
    


})