import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv((r"D:\Project\SEM5\logs.csv"))

plt=df1['Date and Time'].value_counts().plot.bar()