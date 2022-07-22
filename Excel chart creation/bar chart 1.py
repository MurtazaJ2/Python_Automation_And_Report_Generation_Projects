from io import StringIO
import pandas as pd
import matplotlib.pyplot as plt

filesystem = []

log_file = open("//home//softnautics//Public//Murtaza//Excel chart creation//disc_data","r")
content = log_file.read()
content = content.split('*******************************************************************************')

data = content[0].strip()

df = pd.read_csv(StringIO(data),engine='python', sep=r"\s+")
new_df = df.drop(['Filesystem', '1K-blocks', 'on'], axis=1)
new_df['disc_storage'] = new_df["Mounted"]+ " " + new_df["Use%"]
new_df["Available"] = new_df["Available"] / pow(10,12)
new_df["Used"] = new_df["Used"] / pow(10,12)

chart = new_df.plot(x="disc_storage", y="Used", kind="barh", color="red")

new_df.plot(x="disc_storage", y="Available", kind="barh", ax=chart, color="black")

for index, value in enumerate(round(new_df["Used"], 4)):
    plt.text(value, index,
             str(value)+" TB",color= "black", ha= "left", va= "center", ma= "right")
for index, value in enumerate(round(new_df["Available"], 4)):
    plt.text(value, index,
             str(value)+" TB", color= "white", ha= "right", va= "center", ma= "right")

plt.title('AI SW Disk Space')
plt.xlabel("Space in TB")
plt.show()