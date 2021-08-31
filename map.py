# We first import the libraries. 
import pandas as pd
import folium 
from folium.plugins import StripePattern
import geopandas as gpd
import numpy as np
# Next we import the data. 
df = pd.read_csv("sample_data")


# We grab the state and wills column
df = df[["state","wills"]]
df.head()