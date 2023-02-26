import json
with open("sample-data.json", "r") as read_file:
    data = json.load(read_file)
print("""Interface Status
================================================================================""")
print("""DN                                                  Description          Speed     MTU""") 
print("""--------------------------------------------------  -------------------- ------   ------""")
for s in range(18):
    for i, k in data["imdata"][s]['l1PhysIf']["attributes"].items():
        if i == 'dn':
            print("{:<73}".format(k),end="")
        if i == "fecMode":
            print("{:<10}".format(k),end="")
        if i == "mtu":
            print("{:<1}".format(k),end="")
    print("\n")