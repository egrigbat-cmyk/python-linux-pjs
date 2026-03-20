
def number_host(host):
     host_cc = 32-host
     print(f"the total host bit is {host_cc}")

     total_host = (2**host_cc)
     print(f"the total number of address is {total_host}")

     usable_host = (total_host-2)
     print(f"the number of usable host is {usable_host}")

     print(f"block size of address is {total_host}")


devices = [24, 26, 27, 29]

for device in devices:
    number_host(device)
