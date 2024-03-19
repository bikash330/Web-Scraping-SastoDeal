from bs4 import BeautifulSoup
import requests
import pandas as pd

# importing sys for removing UnicodeEncodeError
import sys
sys.stdout.reconfigure(encoding='utf-8')

#url for the  web page to be scraped
url = 'https://www.sastodeal.com/default/sd-fast/sd-liquors/beer.html'

http_request = requests.get(url).text
soup = BeautifulSoup(http_request,'html.parser')
# print(soup.prettify())

data = {'Name': [], 'Price': [], 'Link': []}

beers = soup.find_all('div',{'class':'product-item-info type1'})

for beer in beers:
    Beer_Name = beer.find('a',{'class':'product-item-link'}).text
    data['Name'].append(Beer_Name) #appending the beer name into dictionary
    print(Beer_Name)

    Beer_Price = beer.find('span',{'class':"price-wrapper"}).span.text
    data['Price'].append(Beer_Price) #appending the beer price into dictionary
    print(Beer_Price)

    Link = beer.find('a',{'class':'product-item-link'}).get('href')
    data['Link'].append(Link) #appending the beer details link into dictionary
    print(Link)

df = pd.DataFrame.from_dict(data)
print(df)

df.to_excel('data.xlsx',index=False,header=True) #exporting the data into excel