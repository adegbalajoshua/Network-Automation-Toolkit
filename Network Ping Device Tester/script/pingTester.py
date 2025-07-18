from ping3 import ping
import csv
import datetime
import pytz
import os

def ping_devices(device_file, output_file):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    local_tz = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
    results = []
    with open(device_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header (IP,Device Name)
        for row in reader:
            ip = row[0]
            device_name = row[1] if len(row) > 1 else "Unknown"
            response = ping(ip, timeout=2)
            status = "UP" if response else "DOWN"
            latency = f"{round(response * 1000, 2)}ms" if response else "N/A"
            timestamp = datetime.datetime.now(local_tz).strftime("%Y-%m-%d %H:%M:%S %Z")
            results.append([ip, device_name, status, latency, timestamp])
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["IP", "Device Name", "Status", "Latency", "Timestamp"])
        writer.writerows(results)

if __name__ == "__main__":
    ping_devices("../data/deviceList.csv", "../output/pingReport.csv")