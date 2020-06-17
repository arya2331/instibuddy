import csv
import requests
from bs4 import BeautifulSoup
URL='https://www.aero.iitb.ac.in/home/people/faculty'
page=requests.get(URL)
soup=BeautifulSoup(page.content,'html.parser')
containers=soup.find(id="block-views-faculty-block-1")
containers3=soup.find(id="block-views-adjunct-faculty-block-1")
adjunct_faculty=containers3.find('table')
body3=adjunct_faculty.find("tbody")
rows3=body3.find_all("tr")
containers4=soup.find(id="block-views-visiting-faculty-block-1")
visiting_faculty=containers4.find('table')
body4=visiting_faculty.find("tbody")
rows4=body4.find_all("tr")


faculty_table=containers.find('table') 
body=faculty_table.find("tbody")
rows=body.find_all("tr")
containers2=soup.find(id="block-views-emeritus-faculty-block-1")
emeritus_faculty=containers2.find('table')
body2=emeritus_faculty.find("tbody")
rows2 = body2.find_all("tr")

with open('aero_faculty.csv' , 'w' ,newline='')as f:
    facwriter=csv.writer(f)
    f.write("CORE FACULTY"+"\n"+"\n")
    facwriter.writerow(['Name','Area of Expertise','Phone no.','Email'])
    

    for row in rows:
        name=row.find("td",class_="views-field views-field-title").text.strip()
        area_expertise=row.find("td",class_="views-field views-field-field-specialization").text.strip()
        phone_number=row.find("td",class_="views-field views-field-field-phone-number").text.strip()
        email=row.find("td",class_="views-field views-field-field-email").text.strip()
        print(name,area_expertise,phone_number,email,"\n")
        facwriter.writerow([name,area_expertise,phone_number,email])

    f.write('\n')
    f.write("EMERITUS PROFESSORS"+"\n"+"\n")
    facwriter.writerow(['Name','Area of Expertise','Phone no.','Email'])
    

    for row2 in rows2:
        name=row2.find("td",class_="views-field views-field-title").text.strip()
        area_expertise=row2.find("td",class_="views-field views-field-field-specialization").text.strip()
        phone_number=row2.find("td",class_="views-field views-field-field-phone-number").text.strip()
        email=row2.find("td",class_="views-field views-field-field-email").text.strip()
        print(name,area_expertise,phone_number,email,"\n")
        facwriter.writerow([name,area_expertise,phone_number,email])


    f.write('\n')
    f.write("ADJUNCT FACULTY"+"\n"+"\n")
    facwriter.writerow(['Name','Area of Expertise','Phone no.','Email'])
    

    for row3 in rows3:
        name=row3.find("td",class_="views-field views-field-title").text.strip()
        area_expertise=row3.find("td",class_="views-field views-field-field-specialization").text.strip()
        phone_number=row3.find("td",class_="views-field views-field-field-phone-number").text.strip()
        email=row3.find("td",class_="views-field views-field-field-email").text.strip()
        print(name,area_expertise,phone_number,email,"\n")
        facwriter.writerow([name,area_expertise,phone_number,email])

    f.write('\n')
    f.write("VISITING FACULTY"+"\n"+"\n")
    facwriter.writerow(['Name','Area of Expertise','Phone no.','Email'])
    

    for row4 in rows4:
        name=row4.find("td",class_="views-field views-field-title").text.strip()
        area_expertise=row4.find("td",class_="views-field views-field-field-specialization").text.strip()
        phone_number=row4.find("td",class_="views-field views-field-field-phone-number").text.strip()
        email=row4.find("td",class_="views-field views-field-field-email").text.strip()
        print(name,area_expertise,phone_number,email,"\n")
        facwriter.writerow([name,area_expertise,phone_number,email])









    





