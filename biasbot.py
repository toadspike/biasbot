import requests
from bs4 import BeautifulSoup

c = 0
total = 0
location = 0
z = 0
quotes = 0
found = False

while c < 1: 
    url = "https://en.wikipedia.org/wiki/Special:Random"
    page = requests.get(url)
    html = page.text
    soup = BeautifulSoup(html, 'html.parser')
    html = soup.get_text()
    print(page.url)
    words = ['fortunate', 'luckily', 'thankfully', 'hopefully', 'amazing']
    for n in words: 
        if n in html: 
            found = True
            location = html.index(n)
            for a in html[:location]: 
                if a == "'" or a == '"':
                    quotes += 1
        if found == True and quotes % 2 == 0:
            print("BIAS ALERT: " + n)
            c += 1
            break
        elif found == True: 
            print("QUOTE: " + n)
        else: pass
        found = False
        location = 0
        quotes = 0
    total += 1
print(total)