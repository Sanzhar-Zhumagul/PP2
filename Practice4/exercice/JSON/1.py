import json
with open("sample-data.json") as f:
    data = json.load(f)
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("{:<50} {:<20} {:<8} {:<6}".format("-" * 50, "-" * 20, "-" * 8, "-" * 6))
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, descr, speed, mtu))