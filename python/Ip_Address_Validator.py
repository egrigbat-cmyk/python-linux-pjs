
def address_validator(address):
    new_address = address.split(".")
    if len(new_address) != 4:
        return "invalid"

    for ip in new_address:
      try:
        if int(ip) > 255:
          return "invalid"
      except ValueError:
          return "invalid"


    return "valid"

ip_address = ["100.68.1.1", "192.169.30", "192.155.46.87", "A34.647.66.38"]
for address in ip_address:
     print(address_validator(address))

