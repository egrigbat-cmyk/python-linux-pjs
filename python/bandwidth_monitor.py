with open("network_logs.txt") as f:
    lines = f.readlines()

def parse_log(lines):
    totaal_download_speed = []
    totaal_upload_speed = []
    total_device_name = []
    for line in lines:
        linee = line.strip().split(" ")
        devicename = linee[4]
        total_device_name.append(devicename)
        Download_speed = linee[7]
        totaal_download_speed.append(Download_speed)
        upload_speed = linee[10]
        totaal_upload_speed.append(upload_speed)
    return total_device_name, totaal_download_speed, totaal_upload_speed

def highest_download_speed(lines):
    max_download_speed = 0
    devicename = ""
    for line in lines:
        linee = line.split(" ")
        Download_speed = int(linee[7].replace("Mbps", ""))
        if Download_speed > max_download_speed:
            max_download_speed = Download_speed
            devicename = linee[4]
    return devicename, max_download_speed

def average_download_Speed(lines):
    total_download_speed = 0
    count = 0
    for line in lines:
        linee = line.split(" ")
        Download_speed = int(linee[7].replace("Mbps", ""))
        total_download_speed += Download_speed
        count += 1
    average_speed = total_download_speed / count 
    return average_speed


def flag_devices(lines):
    flagged_devices = []
    for line in lines:
        linee = line.split(" ")
        Download_speed = int(linee[7].replace("Mbps", ""))
        device_name = linee[4]
        if Download_speed > 80:
            flagged_devices.append(device_name)
    return flagged_devices

if __name__ == "__main__":
    total_device_name, totaal_download_speed, totaal_upload_speed = parse_log(lines)
    print("Total Device Names:", total_device_name)
    print("Total Download Speeds:", totaal_download_speed)
    print("Total Upload Speeds:", totaal_upload_speed)

    devicename, max_download_speed = highest_download_speed(lines)
    print(f"Device with the highest download speed: {devicename} with {max_download_speed} Mbps")

    average_speed = average_download_Speed(lines)
    print(f"Average Download Speed: {average_speed} Mbps")

    flagged_devices = flag_devices(lines)
    print("Flagged Devices (Download Speed > 80 Mbps):", flagged_devices)

