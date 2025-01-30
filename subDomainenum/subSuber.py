import aiohttp
import asyncio

# Read subdomains from file
with open('/usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-20000.txt', 'r') as fd:
    subdomains = fd.read().splitlines()

domain = "hackthebox.eu"

# Asynchronous function to check subdomain
async def check_subdomain(session, sub):
    url = f"https://{sub}.{domain}"
    try:
        async with session.get(url, timeout=10) as response:
            if response.status != 404:
                print(f"Found: {url} - Status: {response.status}")
    except:
        pass  # Ignore errors

# Main async function
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [check_subdomain(session, sub) for sub in subdomains]
        await asyncio.gather(*tasks)

# Run async function
asyncio.run(main())
