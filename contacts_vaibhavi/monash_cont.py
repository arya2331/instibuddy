import requests
from bs4 import BeautifulSoup
import csv

URL = 'http://www.iitbmonash.org/iitb/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find('div', class_='vc_tta-panels-container')
#print(results)
contact_table=results.find_all('div', class_='vc_tta-panel')
#contact_table2=results.find_all('div', class_='vc_tta-panel')
#print(contact_table2[2].text)
#print(contact_table[0].text)
#print(contact_table[2].text)

with open('faculty_monash.csv', 'w', newline='') as f:
    thewriter=csv.writer(f)
    thewriter.writerow(['Name', 'email', 'Research Interest'])
    for x in contact_table:
        #print(x.text)
        y1=x.find_all('tr', class_='odd')
        y2=x.find_all('tr', class_='even')
        for z in y1:
            elem=z.find_all('td')
            name=elem[0]
            email=elem[1]
            speciality=elem[2]
            thewriter.writerow([name.text.strip(), email.text.strip(), speciality.text.strip()])
        for z in y2:
            elem=z.find_all('td')
            name=elem[0]
            email=elem[1]
            speciality=elem[2]
            thewriter.writerow([name.text.strip(), email.text.strip(), speciality.text.strip()])
        #print('hello')
        #print(y[0].text)
        
        #y=x.find_all('div', )
        
          #  thewriter.writerow([name.text.strip(), phone.text.strip(), email.text.strip(), address.text.strip()])
    
