count = {}

def error_check(device):
     if "ERROR" in device:
        print(f"{device} contains an error")

def device_count(device):
      vice_name = device.split(" ")
      nth_device = vice_name[6]
      if nth_device in count:
           count[nth_device] +=1
      else:
         count[nth_device] = 1

device1 = ("2026-3-21 08:23:41 - ERROR - Device Router1 connection failed")
device2 = ("2026-3-21 08:26:41 - ERROR - Device switch1 connection failed")
device3 = ("2026-3-21 08:29:41 - INFO - Device Router1 connected sucessfully")
device4 = ("2026-3-21 08:32:41 - INFO - Device Router2 connected sucessfully")
device5 = ("2026-3-21 08:35:41 - ERROR - Device switch4 connection failed")
devices = [device1, device2, device3, device4, device5]
for device in devices:
   error_check(device)
   device_count(device)
print (count)
