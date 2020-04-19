import csv
import requests
from bs4 import BeautifulSoup

URL = 'https://www.me.iitb.ac.in/?q=full-time-faculty'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('table', class_='views-table cols-5')
fac_elems = table.find_all('tr')
with open('faculty.csv', 'w', newline='') as f:

          thewriter = csv.writer(f)
          thewriter.writerow(['Professor Name', 'Phone', 'Email', 'Research Interests'])

          for fac_elem in fac_elems:

              fac_name = fac_elem.find('h4', class_='bluecolor')
              fac_tele = fac_elem.find_all('td')
              fac_email = fac_elem.find('td', class_='views-field views-field-field-display-email bluecolor')
              fac_interests = fac_elem.find_all('p')
              if None in(fac_name, fac_tele, fac_email, fac_interests):
                continue

              thewriter.writerow([fac_name.text.strip(), fac_tele[2].text.strip(), fac_email.text.strip(), fac_interests[1].text.strip()])

             
        

