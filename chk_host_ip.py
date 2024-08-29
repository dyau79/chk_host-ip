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
