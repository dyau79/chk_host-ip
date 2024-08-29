"""
This script does the following:

We import necessary modules: subprocess for running the ping command, platform for determining the operating system, and time for adding a delay between checks.
The ping() function uses the appropriate ping command based on the operating system (Windows or Unix-based) to check if an IP is reachable.
The check_uptime() function reads IP addresses from a file, pings each one, and returns a dictionary with the status of each IP.
The main() function runs an infinite loop that checks the uptime every 60 seconds and prints the results.
To use this script:

Create a text file (e.g., ip_addresses.txt) with one IP address per line.
Save the Python script (e.g., as uptime_checker.py).
Run the script using python uptime_checker.py.
The script will continuously check the uptime of the IP addresses every 60 seconds and print the results.
"""

import subprocess
import platform
import time

def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

def check_uptime(ip_file):
    with open(ip_file, 'r') as file:
        ip_addresses = file.read().splitlines()

    results = {}
    for ip in ip_addresses:
        if ping(ip):
            results[ip] = "Up"
        else:
            results[ip] = "Down"

    return results

def main():
    ip_file = 'ip_addresses.txt'  # Replace with your file name
   
    while True:
        print("\nChecking uptime of IP addresses...")
        results = check_uptime(ip_file)
       
        for ip, status in results.items():
            print(f"{ip}: {status}")
       
        time.sleep(60)  # Wait for 60 seconds before next check

if __name__ == "__main__":
    main()
