file = open("/home/softnautics/Downloads/xnnc_data_Wheel 5_soft.txt",'r')

tc = []
data_dict = {}

content = file.read()
lines = content.split("\n")

for line in lines:
    if ' : ' in line:
        tc.append(line)

for key_value in tc:
    key, value = key_value.split(' : ', 1)
    data_dict[key.strip()] = value.strip()

print(data_dict)