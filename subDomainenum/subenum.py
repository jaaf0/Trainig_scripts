import requests

url = "https://hackthebox.eu"

fd = open('/usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-20000.txt', 'r')
subs = fd.read()
fd.close()

subdomains = list(subs.split('\n'))

for i in subdomains:
    url2 = "https://{}.hackthebox.eu".format(i)
    try:
        r = requests.get(url2)
        if r.status_code != 404:  # Fixed typo: 'statues_code' -> 'status_code'
            print(url2)
    except:
        pass
