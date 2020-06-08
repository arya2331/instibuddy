import requests
from bs4 import BeautifulSoup
import csv

URL = 'http://www.hss.iitb.ac.in/en/faculty_details'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find('table', class_='views-table cols-5')
contact_table=results.find_all('tr')
#print(contact_table[1].text)


with open('faculty_hss.csv', 'w', newline='') as f:
    thewriter=csv.writer(f)
    thewriter.writerow(['Name', 'phone', 'email', 'discipline'])

    size=len(contact_table)
    #print(size)
    for x in range (1, size):
        elems=contact_table[x].find_all('td')
        name=elems[0]
        phone=elems[3]
        email=elems[2]
        discipline=elems[4]
        thewriter.writerow([name.text.strip(), phone.text.strip(), email.text.strip(), discipline.text.strip()])
    

