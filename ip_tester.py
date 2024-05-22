import requests
from concurrent.futures import ThreadPoolExecutor

def test_ip(ip):
    url = f"http://{ip}"
    try:
        response = requests.get(url, timeout=3)  # 3 seconds timeout for each request
        if response.status_code == 200:
            print(f"Working IP: {ip}")
    except requests.RequestException:
        pass  # Ignore IPs that do not respond or have errors

def generate_ip_range(base_ip):
    base_parts = base_ip.split('.')
    base_parts[-1] = '0'
    base_ip = '.'.join(base_parts)
    for i in range(255):
        yield f"{base_ip[:-1]}{i}"

if __name__ == "__main__":
    base_ip = "103.209.173.0"
    ip_range = generate_ip_range(base_ip)
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(test_ip, ip_range)
