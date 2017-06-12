import requests
from bs4 import BeautifulSoup
url = 'https://github.com/simonkrol'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
#print(soup)
#tree = html.fromstring(response.content)
#buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#contributions=tree.xpath('//*[@id="js-pjax-container"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/svg')
#print(contributions)
contributions=[]
for link in soup.find_all('rect'):
    contributions.append(link.get('data-count'))
print(contributions[-1])
