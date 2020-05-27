import csv
import requests
from bs4 import BeautifulSoup

URL = 'https://www.chem.iitb.ac.in/people'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find('div', class_='view-content')
fac_elems = results.find_all('div', class_='col-xs-12 col-sm-6 col-md-4 col-lg-3')
with open('faculty5.csv', 'w', newline='') as f:

    thewriter = csv.writer(f)
    thewriter.writerow(['Professor Name', 'Phone', 'Email'])

    for fac_elem in fac_elems:

         fac_name = fac_elem.find('p')

         site = fac_elem.find('a')
         link = site.get('href')

         page2 = requests.get("https://www.chem.iitb.ac.in" + link)
         soup2 = BeautifulSoup(page2.content, 'html.parser')

         output = soup2.find('div', class_='panel-display panel-2col clearfix')
         
         fac_tele = output.find('div', class_='views-field views-field-field-contact-number')
         fac_email = output.find('div', class_='views-field views-field-mail')
        

         if None in(fac_name, fac_tele, fac_email):
            continue

         thewriter.writerow([fac_name.text.strip(), fac_tele.text.strip(), fac_email.text.strip()])

         