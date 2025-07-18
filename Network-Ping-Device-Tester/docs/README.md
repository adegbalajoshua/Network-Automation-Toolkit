# Network Ping Device Tester

## Overview
The **Network Ping Device Tester** is a Python-based tool designed to monitor network device connectivity by pinging IP addresses listed in a CSV file. It checks whether devices are online (UP) or offline (DOWN), measures latency, and records results with timestamps in the local timezone. The output is saved to a CSV file.

I wrote this simple python script to monitor network resources in my office (Mainstreet Capital Limited) LAN network, instead of having to ping each resource individually.

## Features
- Reads IP addresses and device names from a CSV file (`data/deviceList.csv`).
- Pings devices with a 2-second timeout to determine UP/DOWN status.
- Measures latency in milliseconds and includes local timezone timestamps (e.g., WAT for West Africa Time).
- Outputs results to a CSV file (`output/pingReport.csv`) with columns: IP, Device Name, Status, Latency, Timestamp.
- Handles missing device names by defaulting to "Unknown".
- Automatically creates the output directory if it doesn't exist.

## Technologies
- **Python 3.13.5**: Core programming language.
- **ping3**: Library for sending ICMP ping requests.
- **pytz**: Library for accurate timezone handling.
- **csv**: Built-in Python module for reading/writing CSV files.
- **os**: Built-in Python module for file path and directory management.

## Repository Structure
```
Network-Ping-Device-Tester/
├── scripts/
│   └── pingTester.py        # Main script for pinging devices
├── data/
│   └── deviceList.csv       # Input CSV with IP addresses and device names
├── output/
│   └── pingReport.csv       # Generated CSV with ping results
├── docs/
│   └── README.md            # Project documentation
└── requirements.txt         # List of Python dependencies
```
## Setup Instructions
### Prerequisites
- **Python 3.13.5**: Download and install from [python.org](https://www.python.org/downloads/). Ensure Python and pip are added to your system PATH.
- A working network connection to ping devices.
- Administrative privileges may be required to allow ICMP (ping) requests through the firewall.

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/adegbalajoshua/Network-Automation-Toolkit/Network-Ping-Device-Tester.git
   cd Network-Ping-Device-Tester
   ```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Prepare the input CSV. (This is where you add the IP Addresses of all the Network Resources you want to monitor)**
   - Create (`data/deviceList.csv`) with the following format:
   ```csv
   IP,Device Name
   192.168.1.1,Router
   192.168.1.2,Server
   192.168.1.3,Printer
   ```
   - Please note that these are dummy entries
   - Ensure the CSV includes a header row (IP,Device Name). Device names are optional; missing names will be recorded as "Unknown".
4. **Run the script**
   ```
   cd scripts
   python pingTester.py
   ```
   - The script pings each device and generates (`output/pingReport.csv`).

### Example Output
The output file (`output/pingReport.csv`) will look like:
```
  IP,Device Name,Status,Latency,Timestamp
  192.168.1.1,Router,UP,5.23ms,2025-07-18 16:41:23 WAT
  192.168.1.2,Server,DOWN,N/A,2025-07-18 16:41:23 WAT
  192.168.1.3,Printer,UP,7.45ms,2025-07-18 16:41:23 WAT
```

## Usage
1. Ensure (`data/deviceList.csv`) contains valid IP addresses and optional device names.
2. Run the script from the (`scripts/`) directory using `python pingTester.py`.
3. Check (`output/pingReport.csv`) for the results, which include:
   - **IP**: Device IP Address
   - **Device Name**: Name from the input CSV or "Unknown" if not provided
   - **Status**: UP (device responded) or DOWN (no response)
   - **Latency**: Round-trip time in milliseconds or "N/A" if DOWN
   - **Timestamp**: Local date, time, and timezone (e.g., WAT)

## Troubleshooting
1. **ModuleNotFoundError**: Install missing dependencies with `pip install ping3 pytz`.
2. **FileNotFoundError**: Verify (`data/deviceList.csv`) exists and (`output/`) is writable.
3. **Ping failures**: Ensure network connectivity and check firewall settings (Windows may block ICMP).
   Run Command Prompt as Administrator:
   ```bash
   python pingTester.py
   ```
5. **Timezone issues**: The script uses the system's local timezone. To specify a timezone (e.g., WAT), modify the script to use `pytz.timezone("Africa/Lagos")` or whatever timezone you currently reside in.

## Dependencies
Listed in `requirements.txt`
