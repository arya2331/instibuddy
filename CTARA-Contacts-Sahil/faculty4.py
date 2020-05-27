import csv
import requests
from bs4 import BeautifulSoup

URL = 'http://www.ctara.iitb.ac.in/en/faculty-details'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find('div', class_='view-content')
fac_elems = results.find_all('div', class_='group-right')
with open('faculty4.csv', 'w', newline='') as f:
     
     thewriter = csv.writer(f)
     thewriter.writerow(['Professor Name', 'Phone', 'Email', 'Research Interests'])

     for fac_elem in fac_elems:

             fac_name = fac_elem.find('div', class_='field field-name-title field-type-ds field-label-hidden')
             fac_tele = fac_elem.find('div', class_='field field-name-field-emp-phone field-type-text field-label-inline clearfix')
             fac_email = fac_elem.find('div', class_='field field-name-field-emp-email field-type-email field-label-inline clearfix')
             fac_interests = fac_elem.find('div', class_='field field-name-field-emp-role field-type-text-long field-label-inline clearfix')
             if None in(fac_name, fac_tele, fac_email, fac_interests):
                continue

             thewriter.writerow([fac_name.text.strip(), fac_tele.text[13:].strip(), fac_email.text[7:].strip(), fac_interests.text[20:].strip()])   
      