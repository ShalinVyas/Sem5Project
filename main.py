import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# open the file in read mode
filename = open('logs.csv', 'r')

# creating dictreader object
file = csv.DictReader(filename)

# creating empty lists
DnT = []


# iterating over each row and append
# values to empty list
for col in file:
    DnT.append(col['Date and Time'])

# printing lists
i=0
while i<len(DnT):
    print(DnT[i],"\n")
    i+=1