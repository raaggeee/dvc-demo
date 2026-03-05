import pandas as pd
import numpy as np
import os

df = pd.read_csv("/data2/dvc-demo/data/smile-annotations-final.csv")
df.columns = ["id", "tweets", "label"]

df = df.iloc[:, 1:]
df = df[df["tweets"].str.len() < 100]
os.makedirs("/data2/dvc-demo/data/raw", exist_ok=True)
os.chdir("/data2/dvc-demo/data/raw")
df.to_csv("new_data.csv")