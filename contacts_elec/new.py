import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://www.ee.iitb.ac.in/web/people/faculty'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='wrapper')

job_elems = results.find_all('div', class_='auxunder')
#print(job_elems[0])

list_elems=job_elems[0].find_all('ul', class_='facultyview')
#print(list_elems[0].text) //bgf details

detail_elems=list_elems[1].find_all('li')
list_name=[]
list_phone_number=[]
list_email=[]
list_area=[]
# so we have 1,3,5... as area of interest. so we have detail_elems[2n+1] as area
#name_elem=detail_elems.find_all('div', class_='faculty_name')
for detail_elem in detail_elems:
    name_elem=detail_elem.find('div', class_='faculty_name')
    if name_elem is None:
        continue
    else:
        list_name.append(name_elem.text)
    contact_elem=detail_elem.find('div', class_='ppe')
    #print(contact_elem.text)
    phone_and_email=contact_elem.find_all("span")
    #print(phone_and_email[0])
    for contact_number in phone_and_email[0]:
        list_phone_number.append(contact_number)
    for email_detail in phone_and_email[1]:
        list_email.append(email_detail)
    area_elem=detail_elem.find('div', class_='row faculty_box')
    if area_elem is None:
        continue
    else:
        list_area.append(area_elem.text)
list_name = list(map(lambda s: s.strip(), list_name) )
list_phone_number = list(map(lambda s: s.strip(), list_phone_number) )    
list_email = list(map(lambda s: s.strip(), list_email) )
list_area = list(map(lambda s: s.strip(), list_area) )


df = pd.DataFrame({'name':list_name,'list_phone_number':list_phone_number,'list_email':list_email,'list_area':list_area})
df.to_csv('final_direc.csv')



