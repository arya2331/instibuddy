import csv
import requests
from bs4 import BeautifulSoup
URL='http://www.csre.iitb.ac.in/faculty.php'
page=requests.get(URL)
soup=BeautifulSoup(page.content,'html.parser')
containers=soup.find_all("div",{"class":"col s12 m12"})







with open('csre_faculty.csv' , 'w' ,newline='')as f:
    f.write("CSRE FACULTY"+"\n"+"\n")

    for container in containers:
        faculty=container.find("div",{"class":"card-content"}).text.strip()
        print(faculty)
        f.write(faculty)
        f.write('\n'+'\n')
        f.write('\n')
            