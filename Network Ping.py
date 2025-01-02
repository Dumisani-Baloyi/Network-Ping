import subprocess

def ping_host(host):
    try:
        response = subprocess.run(["ping", "-n", "1", host], stdout=subprocess.PIPE, text=True)
        if "TTL=" in response.stdout:
            return True
        return False
    except Exception as e:
        print(f"Error pinging {host}: {e}")
        return False

def monitor_network(hosts):
    for host in hosts:
        status = "Online" if ping_host(host) else "Offline"
        print(f"{host} is {status}.")

if __name__ == "__main__":
    hosts_to_check = ["8.8.8.8", "google.com", "192.168.1.1"]
    monitor_network(hosts_to_check)
