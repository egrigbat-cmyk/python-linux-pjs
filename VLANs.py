vlans = []

def new_vlan(vlan_id, name):
    vlan = {"vlan_id":vlan_id, "name": name, "assigned_devices": []}
    vlans.append(vlan)

def assign_device(vlan_id, device):
    for vlan in vlans:
        if vlan["vlan_id"] == vlan_id:
            vlan["assigned_devices"].append(device)
    print(vlans)

def display_vlans():
    for vlan in vlans:
      print(vlan)

def find_device(name_search):
    for vlan in vlans:
        if name_search in vlan["assigned_devices"]:
            print(vlan)

new_vlan(10, "management")

new_vlan(12, "HR")

new_vlan(16, "ground_floor")

assign_device(10, "iphone")

assign_device(12, "pixel")

assign_device(16, "samsung")

assign_device(16, "Nokia")

assign_device(10, "itel")

assign_device(12, "tecno")

display_vlans()

find_device("iphone")
    

