import urllib.request as urlnes
from bs4 import BeautifulSoup

url = "https://www.reddit.com/top/"
#request = urllib.request.Request(url)
#html = urllib.request.urlopen(request).read()

request = urlnes.Request(url)
html = urlnes.urlopen(request).read()

soup = BeautifulSoup(html,'html.parser')
main_table = soup.find("div", attrs={'id':'t3_8vkwjw'})
links = main_table.find_all("a",class_="scrollerItem yj3st6-5 fUvsWd Post t3_8vkwjw  s18unrpv-0 itoCnT")

extracted_records = []
for link in links:
    title = link.textT
    url = link['href']
    record = {
        'title': title,
        'url': url
    }
    extracted_records.append(record)
print(extracted_records.count)
