import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
outfile = open("scrape.csv",'w',newline='')
writer= csv.writer(outfile)
URL= 'http://www.cese.iitb.ac.in/faculty-directory'
df = pd.DataFrame(columns=['Name','Post','Contact'])
page= requests.get(URL)

soup=BeautifulSoup(page.content, 'html.parser')
results=soup.find(id='datatable')
contact_elems= results.find_all('tr')
for contact_elem in contact_elems:
    title_elem= contact_elem.find('td',class_='views-field views-field-title')
    post_elem= contact_elem.find('td', class_='views-field views-field-field-faculty-designation-1')
    appoint_elem=contact_elem.find('td',headers_='view-field-employment-category-table-column')
    roomno_elem=contact_elem.find('td',headers_='view-field-room-no-table-column')
    PhoneNo_elem=contact_elem.find('td',class_='views-field views-field-field-phone-no-new')
    Email_elem=contact_elem.find('td',class_='views-field views-field-field-email-new')
    if title_elem is None:
        continue
    else:
        Title=title_elem.text
        print(title_elem.text)
    if post_elem is None:
        continue
    else:
        Post=post_elem.text
        print(post_elem.text)
    # if appoint_elem is None:
        # print("none")
    # else:
        # print(appoint_elem.text)
    # if roomno_elem is None:
        # print("none")
    # else:
        # print(roomno_elem.text)
    if PhoneNo_elem is None:
        continue
    else:
        contact=PhoneNo_elem.text
        print(PhoneNo_elem.text)
    df2=pd.DataFrame([[Title,Post,contact]],columns=['Name','Post','Contact'])
    df=df.append(df2,ignore_index=True)
df.to_csv('scrape.csv')
outfile.close()
    # if Email_elem is None:
        # print("none")
    # else:
        # print(Email_elem.text)
    

