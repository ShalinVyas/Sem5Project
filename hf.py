import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as py

df = pd.read_csv("./application.csv")
#print(df)
#datatype = df.dtypes
#print(datatype)

# resizeplot(10, 6, 100)
# fig, (a1) = plt.subplots(ncols=1)
# u, df["label_num"] = np.unique(df['Source'], return_inverse=True)
# a1.scatter(df['Time Created'],df['Source'],c=df["label_num"])
# plt.show()

# plt.bar(df['Source'],df['Time Created'])
# plt.xlabel("Source")
# plt.ylabel("Time Created")
# plt.savefig("graph.png")
# plt.show()

# sns.lineplot(x='Event ID', y='Time Created', data=df)
# sns.despine()
# plt.show()

# sns.countplot(x='Source', data=df)
# plt.show()
from matplotlib.pyplot import figure

# figure(num=None, figsize=(20, 18), dpi=80, facecolor='w', edgecolor='r')
# sns.barplot(x="Source", y="Event ID", data=df)
# plt.show()


#fig = px.pie(df['Source'])
#plt.title("Apps Used")
#fig.savefig('pie graph.jpg', bbox_inches='tight')
#df['FT'] = df['FT'].astype(int)
fig = px.pie(df, names='Source')
py.write_image(fig, 'pie graph1.png')
fig.show()
