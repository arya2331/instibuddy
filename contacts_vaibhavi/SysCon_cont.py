import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://www.sc.iitb.ac.in/coreFaculty.html'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find('div', class_='content')
#print(results.text)
contact_table=results.find_all('tr')


with open('faculty_SysCon.csv', 'w', newline='') as f:
    thewriter=csv.writer(f)
    thewriter.writerow(['Name', 'contact', 'research area'])
    size=len(contact_table)
    for x in range (1, size):
        elems=contact_table[x].find_all('td')
        name=elems[1].find('a')
        area=elems[1].find('span' , class_='researchArea')
        contact=elems[1].find('span', class_='profContact')
        
        thewriter.writerow([name.text.strip(), contact.text.strip(), area.text.strip()])
    
