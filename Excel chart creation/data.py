# def convert_bytes(bytes_number):
#     tags = [ "Byte", "Kilobyte", "Megabyte", "Gigabyte", "Terabyte" ]
 
#     i = 0
#     double_bytes = bytes_number
 
#     while (i < len(tags) and  bytes_number >= 1024):
#             double_bytes = bytes_number / 1024.0
#             i = i + 1
#             bytes_number = bytes_number / 1024
 
#     return str(round(double_bytes, 2)) + " " + tags[i]

#raw = new_df.to_string(index=False)

# ax = df.plot(x="Mounted", y="Used", kind="barh", color="red")
# df.plot(x="Mounted", y="Available", kind="barh", ax=ax, color="black")

# df.plot(x="Name", y=["Age", "Height(in cm)"], kind="bar")

# ax = df.plot(x="Name", y="Height(in cm)", kind="bar")
# # plotting age on the same axis
# df.plot(x="Name", y="Age", kind="bar", ax=ax, color="maroon")

# chart = plt.subplot()
# chart.barh(new_df["disc_storage"], new_df["Used"], color="red")
# chart.barh(new_df["disc_storage"], new_df["Available"], color="black")
