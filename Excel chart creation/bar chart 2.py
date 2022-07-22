import matplotlib.pyplot as plt
import pandas as pd

log_file = open("/home/murtaza/Desktop/Chart creation/disc_data", "r")

ubu_storage_data = []
filesystem = []
Used_memory = []
use_percent = []
available = []

for data in log_file:
    if data.startswith("tenivp") or data.startswith("/dev"):
        fs = data.split(" ")[0].strip("\n")
        filesystem.append(fs)

    if data.startswith("/dev"):
        u_p2 = data.split(" ")[-2].strip("\n")
        av2 = data.split(" ")[-4].strip("\n")
        av2 = int(av2) / pow(10, 12)
        u_m2 = data.split(" ")[-5].strip("\n")
        u_m2 = int(u_m2) / pow(10, 12)
        use_percent.append(u_p2)
        available.append(av2)
        Used_memory.append(u_m2)

for f in range(0, 4):
    d = filesystem[f]+filesystem[f+1]
    del filesystem[f+1]
    ubu_storage_data.append(d)

df = pd.DataFrame(ubu_storage_data, columns=['ubu storage data'])
df["available"] = available
df["Used"] = Used_memory
df["use%"] = use_percent

df['disc_storage'] = df["ubu storage data"] + " " + df["use%"]

chart = df.plot(x="disc_storage", y="Used", kind="barh", color="red")
df.plot(x="disc_storage", y="available", kind="barh", ax=chart, color="black")

for index, value in enumerate(round(df["Used"], 4)):
    plt.text(value, index,
             str(value)+" TB", color="black", ha="right", va="center", ma="right")
for index, value in enumerate(round(df["available"], 4)):
    plt.text(value, index,
             str(value)+" TB", color="white", ha="right", va="center", ma="right")

plt.title('Local Ubu Disk Space')
plt.xlabel("Space in TB")
plt.show()