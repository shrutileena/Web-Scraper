# For Visualization it is necessary to run the file one by one 
# for each graph by uncommenting the code. 
# Otherwise it will not give correct results.



import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')
import squarify 
import random
from pywaffle import Waffle

df = pd.read_csv("College_Data.csv", index_col=0)

# To process the missing values
'''print(df.isnull().sum())

df['Pincode'].fillna("--", inplace=True)
df['Email_Address'].fillna("--", inplace=True)
df['Website_Link'].fillna("--", inplace=True)
df['Principal_Name'].fillna("--", inplace=True)
df['Registrar_Name'].fillna("--", inplace=True)

df.to_csv("College_Data.csv")'''


# SetUp for visualization
large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
'legend.fontsize': med,
'figure.figsize': (16,10),
'axes.labelsize': med,
'axes.titlesize': med,
'xtick.labelsize': med,
'ytick.labelsize': med,
'figure.titlesize': large}

plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")

# Version
print(mpl.__version__)
print(sns.__version__)




# Pie Chart (Minority Status)

'''df = df.groupby('Minority_Status').size().reset_index(name='counts')

fig, ax = plt.subplots(figsize=(12, 7), subplot_kw=dict(aspect="equal"))

data = df['counts']
categories = df['Minority_Status']
explode = [0,0,0,0,0,0.1,0,0,0]

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}% ({:d} )".format(pct, absolute)

wedges, texts, autotexts = ax.pie(data, 
                                  autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="black"), 
                                  colors=plt.cm.Dark2.colors,
                                  startangle=140,
                                  explode=explode)

ax.legend(wedges, categories, title="Minority Type", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.setp(autotexts, size=10, weight=700)
ax.set_title("Pie chart - Minority Status")
plt.show()'''





# Tree Map

'''df = df.groupby('Minority_Status').size().reset_index(name='counts')
labels = df.apply(lambda x: str(x[0]) + "\n (" + str(x[1]) + ")", axis=1)
sizes = df['counts'].values.tolist()
colors = [plt.cm.Spectral(i/float(len(labels))) for i in range(len(labels))]

plt.figure(figsize=(12,8), dpi= 80)
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=.8)

plt.title('Treemap of Minority Status')
plt.axis('off')
plt.show()'''




# Bar Graph

'''df = df.groupby('Minority_Status').size().reset_index(name='counts')
n = df['Minority_Status'].unique().__len__()+1
all_colors = list(plt.cm.colors.cnames.keys())
random.seed(100)
c = random.choices(all_colors, k=n)

plt.figure(figsize=(16,10), dpi= 80)
plt.bar(df['Minority_Status'], df['counts'], color=c, width=.5)
for i, val in enumerate(df['counts'].values):
    plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':12})

plt.gca().set_xticklabels(df['Minority_Status'], rotation=13, horizontalalignment= 'right')
plt.title("Minority Status", fontsize=18)
plt.ylabel('Number of Colleges')
plt.ylim(0, 800)
plt.show()'''




# pie Chart (Autonomous Status)

'''df = df.groupby('Autonomous_Status').size().reset_index(name='counts')

fig, ax = plt.subplots(figsize=(12, 7), subplot_kw=dict(aspect="equal"))

data = df['counts']
categories = df['Autonomous_Status']
#explode = [0,0,0,0,0,0.1,0,0,0]

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}% ({:d} )".format(pct, absolute)

wedges, texts, autotexts = ax.pie(data, 
                                  autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="black"), 
                                  colors=plt.cm.Dark2.colors,
                                  startangle=140)

ax.legend(wedges, categories, title="Autonomous or Non-Autonomous", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.setp(autotexts, size=10, weight=700)
ax.set_title("Pie chart of Colleges with Autonomous Status")
plt.show()'''





# pie Chart (Region type)
'''df = df.groupby('Region-Type').size().reset_index(name='counts')

fig, ax = plt.subplots(figsize=(12, 7), subplot_kw=dict(aspect="equal"))

data = df['counts']
categories = df['Region-Type']
#explode = [0,0,0,0,0,0.1,0,0,0]

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}% ({:d} )".format(pct, absolute)

wedges, texts, autotexts = ax.pie(data, 
                                  autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="black"), 
                                  colors=plt.cm.Dark2.colors,
                                  startangle=140)

ax.legend(wedges, categories, title="Region", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.setp(autotexts, size=10, weight=700)
ax.set_title("Pie chart - Region type")
plt.show()'''