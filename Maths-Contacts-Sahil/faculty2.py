import csv
import requests
from bs4 import BeautifulSoup

URL = 'http://www.math.iitb.ac.in/People/faculty.php'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(class_='tab-content')
fac_elems = results.find_all('div', class_='col-md-8 col-sm-8 col-xs-12')
with open('faculty2.csv', 'w', newline='') as f:
      
      thewriter = csv.writer(f)
      thewriter.writerow(['Professor Name', 'Phone', 'Email', 'Research Interests'])

      for fac_elem in fac_elems: 

           fac_use = fac_elem.find_all('h4')
           fac_link = fac_elem.find_all('a')
           
           if(fac_use[5].text[0:4] == "Home"):
            
              thewriter.writerow([fac_link[0].text.strip(), fac_use[6].text[10:].strip(), fac_use[2].text[5:].strip(), fac_link[1].text.strip()])  

           else:

               thewriter.writerow([fac_link[0].text.strip(), fac_use[5].text[10:].strip(), fac_use[2].text[5:].strip(), fac_link[1].text.strip()])  
  
