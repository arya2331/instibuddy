import csv 
import requests
from bs4 import BeautifulSoup

URL = 'http://www.et.iitb.ac.in/Faculty.html'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(class_='col-lg-12 bg-part faculty')
fac_elems = results.find_all(class_='col-lg-9 col-md-9 col-sm-9 faculty-brief')
with open('faculty3.csv', 'w', newline='' ) as f:

       thewriter = csv.writer(f)
       thewriter.writerow(['Professor Name', 'Phone', 'Email', 'Research Interests'])

       for fac_elem in fac_elems:
             
             fac_use = fac_elem.find_all('p')
             fac_extra = fac_elem.find_all('strong')
             if None in(fac_use):
                  continue

             thewriter.writerow([fac_use[0].text.strip(), fac_use[2].text[11:].strip(), fac_use[1].text[9:].strip(), fac_use[-1].text[20:].strip()])   
