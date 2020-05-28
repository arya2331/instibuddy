import requests
from bs4 import BeautifulSoup
import csv

URL = 'http://www.phy.iitb.ac.in/en/faculty'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find('div', class_='view-content')
contact_table=results.find_all('tr')


with open('faculty_phy.csv', 'w', newline='') as f:
    thewriter=csv.writer(f)
    thewriter.writerow(['Name', 'phone', 'email', 'address'])

    for x in contact_table:
        elems=x.find_all('td')
        for y in elems:
            name=y.find('div', class_='views-field views-field-title')
            phone=y.find('div', class_='views-field views-field-field-emp-phone')
            email=y.find('div', class_='views-field views-field-field-emp-email')
            address=y.find('div' , class_='views-field views-field-field-address')
            #print(email.text)
            thewriter.writerow([name.text.strip(), phone.text.strip(), email.text.strip(), address.text.strip()])
    
