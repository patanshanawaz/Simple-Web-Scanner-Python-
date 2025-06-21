import requests
from bs4 import BeautifulSoup

def scan_website(url):
    print(f"\n🔍 Scanning: {url}")
    
    try:
        response = requests.get(url)
        print(f"✅ Status Code: {response.status_code}")
        print(f"🛡 Server: {response.headers.get('Server')}")
        print(f"🔐 X-Frame-Options: {response.headers.get('X-Frame-Options')}")
        print(f"🛡 Content-Security-Policy: {response.headers.get('Content-Security-Policy')}")

        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        print(f"🔗 Found {len(links)} links")

        if response.status_code == 200:
            print("🟢 Website is reachable.")
        elif response.status_code == 403:
            print("🔴 Access is forbidden.")
        elif response.status_code == 404:
            print("🔴 Page not found.")
        else:
            print("⚠ Something else happened.")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    target_url = input("🌐 Enter a website URL (with http/https): ")
    scan_website(target_url)
