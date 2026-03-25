
def flag_device(devices):
    for device in devices:
       name_vice = device["name"]
       device_port = device["open_ports"]
       dangerous = [23, 21, 80]
       for port in dangerous:
           if port in device_port:
               print(f"{name_vice} has dangerous port {port} open")

def outdated_flag(devices):
    for device in devices:
      name_vice = device["name"]
      date = device["last_updated"]
      new_date = date.split("-")
      pin_year = new_date[2]
      real_year = int(pin_year)
      if real_year < 2025:
        print(f"{name_vice} last update was {real_year}. pls upadte device")

def security_report(devices):
    print("== SECURITY REPORT ==")
    print("-- DANGEROUS PORTS --")
    flag_device(devices)
    print("-- OUTDATED DEVICES --")
    outdated_flag(devices)


device1 = {"name": "pixel",
          "ip": "192.60.24.1",
          "open_ports": [443, 23, 70, 90],
          "last_updated": "20-3-2025"}

device2 = {"name": "iphone",
          "ip": "192.60.24.1",
          "open_ports": [443, 80, 70, 90],
          "last_updated": "20-3-2023"}
device3 = {"name": "samsung",
          "ip": "192.60.24.1",
          "open_ports": [443, 23, 80, 90],
          "last_updated": "20-3-2024"}
device4 = {"name": "nokia",
          "ip": "192.60.24.1",
          "open_ports": [443, 85, 70, 90],
          "last_updated": "20-3-2026"}
device5 = {"name": "itel",
          "ip": "192.60.24.1",
          "open_ports": [443, 21, 70, 90],
          "last_updated": "20-3-2021"}


devices = [device1, device2, device3, device4, device5]

security_report(devices)
