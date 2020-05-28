import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://www.cse.iitb.ac.in/page14'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='main')
contact_table=results.find('div', class_='mpart')
contact_elem_1=contact_table.find_all('tr', class_='row1')
contact_elem_2=contact_table.find_all('tr', class_='row2')
#print(len(contact_elem_2))
#print(len(contact_elem_2))

#print(contact_elem_2[0])
#contact_elem_1 and contact_elem_2 are two arrays containing details of the faculties.

with open('faculty_cse.csv', 'w', newline='') as f:
    thewriter=csv.writer(f)
    thewriter.writerow(['Name', 'phone', 'email', 'address', 'research'])

    for x in contact_elem_2:
        elems=x.find_all('tr')
        name_email=elems[1].find_all('td')
        name=name_email[0]
        email=name_email[1]
        area=elems[2].find('td')
        try:
            office_address=elems[3].find('td')
            phone=elems[4].find('td')
        except IndexError:
            break
        if None in (name, email, area, office_address, phone):
            continue
        thewriter.writerow([name.text.strip(), phone.text.strip(), email.text.strip(), office_address.text.strip(),area.text.strip()])
    for x in contact_elem_1:
        elems=x.find_all('tr')
        name_email=elems[1].find_all('td')
        name=name_email[0]
        email=name_email[1]
        area=elems[2].find('td')
        try:
            office_address=elems[3].find('td')
            phone=elems[4].find('td')
        except IndexError:
            break
        if None in (name, email, area, office_address, phone):
            continue
        thewriter.writerow([name.text.strip(), phone.text.strip(), email.text.strip(), office_address.text.strip(),area.text.strip()])
    




